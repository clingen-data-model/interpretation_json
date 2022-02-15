import requests
import json
import re
from clingen_interpretation.node import Node
from clingen_interpretation.entities_generated import *
from clingen_interpretation.interpretation_constants import *

'''
class Coding(Node):
    """We need Coding because Allele is defined in terms of it"""
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = 'Coding'
    def set_code(self,x):
        self.data['code'] = x
    def get_code(self):
        return self.data['code']
    def set_system(self,x):
        self.data['system'] = x
    def get_system(self):
        return self.data['system']
    def set_display(self,x):
        self.data['display'] = x
    def get_display(self):
        return self.data['display']
'''

def get_car_canonical_allele_by(param, value):

    query_by_param = { 'hgvs' : 'http://reg.genome.network/allele?hgvs=', \
                       'caid' : 'http://reg.genome.network/allele/' }
    # send a GET request with parameter
    if param not in query_by_param:
        raise Exception ('Invalid param %s passed to get_car_canonical_allele_by methdod.' % param)

    # convert symbols like > to special code %3E
    url = query_by_param[param]+requests.utils.quote(value)
    res = requests.get(url)
    txt = res.text
    cardata = json.loads(txt)
    # todo error handling. check for 'errorType' attribute and handle ...
    return cardata

def get_car_hgvs_ctx_allele_dict(hgvs_38, ca_id):
    """ returns a dictionary of hgvs_name to CAR contextual allele objects """

    #We want to get the id/representation from the Baylor Allele Registry.
    car_rep = None
    decurried_ca_id = None
    hgvs_ctx_dict = None
    external_recs = None
    hgvs38_ca_id = None

    if hgvs_38:
        car_rep = get_car_canonical_allele_by('hgvs', hgvs_38)
        if 'errorType' in car_rep:
            car_rep = None
        else:
            hgvs38_ca_id = car_rep['@id'] if '@id' in car_rep else None
            decurried_hgvs38_ca_id = hgvs38_ca_id.split('/')[-1] if hgvs38_ca_id is not None else None

        #Make sure it's the same id, if ca_id was provided
        if ca_id:
            # de-curie before compare
            decurried_ca_id = ca_id.split(':')[-1]
            if decurried_hgvs38_ca_id != decurried_ca_id:
                logging.error('Original ID: %s.  Final ID: %s' % (decurried_ca_id, decurried_hgvs38_ca_id) )
                raise Exception
    elif ca_id:
        decurried_ca_id = ca_id.split(':')[-1]
        car_rep = get_car_canonical_allele_by('caid', decurried_ca_id)
        if 'errorType' in car_rep:
            car_rep = None

    if car_rep:
        hgvs_ctx_dict = {}
        for ref in ['genomicAlleles', 'transcriptAlleles']:
            if ref in car_rep:
                for ctx_allele in car_rep[ref]:
                    # always add the hgvs_38 key to the ctx_allele dict if available,
                    # which likely originated from the ClinVar hgvs representation,
                    # The ClinVar and CAR hgvs representations do not use the same
                    # alignment and precise hgvs del/ins/dup representations.
                    # This will ensure that the CAR ctx-allele will always be
                    # findable later when needed to build the interp json output.
                    if hgvs_38 and ref == 'genomicAlleles' and 'referenceGenome' in ctx_allele and ctx_allele['referenceGenome'] == 'GRCh38':
                        hgvs_ctx_dict.update( {hgvs_38: ctx_allele} )
                    for hgvs in ctx_allele['hgvs']:
                        hgvs_ctx_dict.update( { hgvs: ctx_allele} )

        # also return external records info
        external_recs = car_rep['externalRecords'] if 'externalRecords' in car_rep else None

    # return a dict to get multiple values back
    return {'hgvs38_ca_id':hgvs38_ca_id, 'hgvs_ctx_dict':hgvs_ctx_dict, 'external_recs':external_recs}

def extract_accession_and_type(hgvs):
    """This method attempts to extract the RefSeq, LRG or Ensembl accession from the
       beginning of an hgvs string with or without an embedded gene symbol after the accession
       and returns it along with the sequence type (genomic, transcript, protein)"""
    accession = None
    type = None
    m = re.search('^((NC|NG)_[0-9]+\.[0-9]+|LRG_[0-9]+)[^0-9]*:g\..*$', hgvs)
    if m:
        type = 'genomic'
        accession = m.group(1)
    else:
        m = re.search('^((NM|NR|XM|XR)_[0-9]+\.[0-9]+|LRG_[0-9]+t[0-9]+|ENST[0-9]+\.[0-9]+)[^0-9]*(\([A-Z0-9]+\)){0,1}:(c|n|r)\..*$', hgvs)
        if m:
            type = 'transcript'
            accession = m.group(1)
        else:
            m = re.search('^((NP|XP)_[0-9]+\.[0-9]+|LRG_[0-9]+p[0-9]+|ENSP[0-9]+\.[0-9]+)[^0-9]*:p\..*$', hgvs)
            if m:
                type = 'protein'
                accession = m.group(1)
    return accession, type

# attempt to derive the chromosome from the NCBI NC_* refseq accession.
def derive_chromosome(sequence):
    chr = None
    m = re.search('^NC_0+([0-9]+|12920)\.[0-9]+$', sequence) if sequence is not None else None
    if m is not None:
        val = m.group(1)
        if val == '23':
            chr = 'X'
        elif val == '24':
            chr = 'Y'
        elif val == '12920':
            chr = 'M'
        else:
            chr = val
    return chr

# this method attempts to extract the gene symbol from
# a clinvar formatted variant title.
def extract_gene_symbol(preferred_name):
    gene_symbol = None
    m = re.search('^N[MC]_[0-9]+\.[0-9]+\(([A-Z0-9]+)\).*$', preferred_name)
    if m is not None:
        gene_symbol = m.group(1)
    return gene_symbol

def lookup_car_ctx_rep(hgvs, hgvs_ctx_dict):
    """looks up the hgvs expression in the dictionary built from the CAR representations.
       the CAR hgvs representation of deletions 'del' truncates the fully qualified
       representations that include the deleted basepairs. So c.1234delG is represented
       in the CAR as c.1234del. Since ClinVar does not do this we must make a consideration
       when doing the lookup by the CAR hgvs key in the dictionary argument.
    """

    if hgvs and hgvs_ctx_dict and hgvs in hgvs_ctx_dict:
        car_ctx_rep = hgvs_ctx_dict[hgvs]
    else:
        # if not found then strip off explicit bases after the del
        m = re.search('(^.*del)([ACTG]*$)', hgvs)
        if m is not None:
            hgvs = m.group(1)
        car_ctx_rep = hgvs_ctx_dict[hgvs] if hgvs_ctx_dict and hgvs in hgvs_ctx_dict else None
    return car_ctx_rep

class CanonicalAllele(Node):
    """# build the following structure to initialize any VCI canonical allele
       # 1. 'identifier' 'CAR:CA999999' (CAid) or 'ClinVar:9999999' (variationId)
       # 2. 'hgvs_names' <array of entries, some genome build-specific + 'others' nested array)
       # 3. 'dbsnp_ids'  <array of dbsnp ids in rs form without rs prefix>
       # 4. 'preferred_name' <clinvar variant title if available, if blank the b38 hgvs will be used if found>
       NOTE: we could move the constructor to a class method 'fromVCI' in the future if we wanted to support
          additional constructor data sets. For now the constructor is VCI data specific.
    """
    def __init__(self, **kwargs):
        Node.__init__(self, **kwargs)
        self.data[TYPE_KEY] = 'CanonicalAllele'

        # the preferred sequence is the accession in the preferred_name
        preferred_name = kwargs.get('preferred_name',None)
        self.preferred_sequence = None
        if preferred_name is not None:
            self.data[PROP_A200_LABEL_KEY] = preferred_name
            self.preferred_sequence, seq_type = extract_accession_and_type(preferred_name)

        # initialize
        self.data['relatedContextualAllele'] = []

        identifier = kwargs.get('identifier',None)
        hgvs_names = kwargs.get('hgvs_names',[])
        dbsnp_ids = kwargs.get('dbsnp_ids', [])

        # is identifer a ca_id?
        ca_id = identifier if identifier and identifier.startswith('CAR:') else None
        hgvs_38 = hgvs_names['GRCh38'] if hgvs_names and 'GRCh38' in hgvs_names else None

        # CAR-related lookup and validation for external identifiers and contextual allele related data merging.
        hgvs_ctx = None
        external_recs = None
        hgvs38_ca_id = None
        if hgvs_38 or ca_id:
            # get the CAR hgvs-to-ctx_allele dictionary by using the hgvs_38 expression, and testing it matches the ca_id when available.
            # if no hgvs_38 expression is found then use the ca_id if available.
            results = get_car_hgvs_ctx_allele_dict(hgvs_38, ca_id)
            hgvs38_ca_id = results['hgvs38_ca_id']
            hgvs_ctx = results['hgvs_ctx_dict']
            external_recs = results['external_recs']

        # loop through the
        # if hgvs_ctx is returned then validate that all hgvs_names
        # ideally we'd do some type of exception handling to see if the VCI equivalent set is
        # equal to the CAR equivalent set, but that's a significant issue to deal with.
        # for now we will only pair the car_ctx_rep findings that match exactly.
        hgvs_not_found = []
        for ref_genome in ['GRCh38','GRCh37','NCBI36']:
            if ref_genome in hgvs_names:
                hgvs = hgvs_names[ref_genome]
                car_ctx_rep = lookup_car_ctx_rep(hgvs, hgvs_ctx)
                accession, seq_type = extract_accession_and_type(hgvs)
                chr = derive_chromosome(accession)
                ctx_allele = ContextualAllele( canonical_allele_id=self.data[ID_KEY], \
                                               allele_type=seq_type, \
                                               hgvs=hgvs, \
                                               car_ctx_rep=car_ctx_rep, \
                                               accession=accession, \
                                               chr=chr,
                                               preferred_sequence=self.preferred_sequence, \
                                               ref_genome=ref_genome, \
                                               preferred_name=preferred_name )
                self.data['relatedContextualAllele'].append(ctx_allele)

        if 'others' in hgvs_names:
            for hgvs in hgvs_names['others']:
                car_ctx_rep = lookup_car_ctx_rep(hgvs, hgvs_ctx)
                gene_symbol = car_ctx_rep['geneSymbol'] if car_ctx_rep and 'geneSymbol' in car_ctx_rep else None
                gene_id = "%s:%s" % ("NCBIGene", car_ctx_rep['geneNCBI_id']) if car_ctx_rep and 'geneNCBI_id' in car_ctx_rep else None
                accession, seq_type = extract_accession_and_type(hgvs)
                ctx_allele = ContextualAllele( canonical_allele_id=self.data[ID_KEY], \
                                               allele_type=seq_type, \
                                               hgvs=hgvs, \
                                               car_ctx_rep=car_ctx_rep, \
                                               accession=accession, \
                                               gene_symbol=gene_symbol, \
                                               gene_id=gene_id, \
                                               preferred_sequence=self.preferred_sequence, \
                                               preferred_name=preferred_name )
                self.data['relatedContextualAllele'].append(ctx_allele)

        # add related identifiers (ClinVar, CAR & dbSNP only - for now)
        # if source id is ClinVar then add CAR and vice versa
        if identifier.startswith('ClinVar:') and hgvs38_ca_id:
            self.add_external_identifier(hgvs38_ca_id, preferred_name)

        if external_recs:
            if 'ClinVarVariations' in external_recs and identifier.startswith('CAR:'):
                for cva in external_recs['ClinVarVariations']:
                    self.add_external_identifier("%s:%s" % ('ClinVar', cva['variationId']), preferred_name)
            if 'dbSNP' in external_recs:
                for rsid in external_recs['dbSNP']:
                    self.add_external_identifier("%s:%s" % ('dbSNP', rsid['rs']), None)
        elif dbsnp_ids:
            for rsid in dbsnp_ids:
                self.add_external_identifier("%s:%s" % ('dbSNP', rsid), None)

    def get_allele(self,ref_genome):
        for ctx_allele in self.data['relatedContextualAllele']:
            if ctx_allele.ref_genome == ref_genome:
                return ctx_allele.data['state']
        return None

    def get_ref_allele(self,ref_genome):
        for ctx_allele in self.data['relatedContextualAllele']:
            if ctx_allele.ref_genome == ref_genome:
                return ctx_allele.data['referenceCoordinate']['refState']
        return None

    def add_external_identifier(self, id, display=None):
        if 'relatedIdentifier' not in self.data:
            self.data['relatedIdentifier'] = []
        ext_identifier = { "id": id  }
        if display is not None:
            ext_identifier.update( { "label" : display } )
        if ext_identifier not in self.data['relatedIdentifier']:
            self.data['relatedIdentifier'].append(ext_identifier)

class ContextualAllele(Node):
    def __init__(self, **kwargs):
        Node.__init__(self, **kwargs)

        canonical_allele_id = kwargs.get('canonical_allele_id',None)
        allele_type = kwargs.get('allele_type',None)
        self.data[TYPE_KEY] = 'ContextualAllele'
        self.data['relatedCanonicalAllele'] = canonical_allele_id
        if allele_type is not None:
            self.data['contextualAlleleType'] = allele_type

        gene_id = kwargs.get('gene_id',None)
        gene_symbol = kwargs.get('gene_symbol',None)
        preferred_sequence = kwargs.get('preferred_sequence',None)
        accession = kwargs.get('accession', None)
        if not gene_symbol and preferred_sequence == accession:
            gene_symbol = extract_gene_symbol(kwargs.get('preferred_name',None))

        related_gene = None
        if gene_id:
            related_gene = Node(identifier=gene_id)
        if gene_symbol:
            if related_gene:
                related_gene.set_label(gene_symbol)
            else:
                related_gene = gene_symbol
        if related_gene:
            self.set_relatedGene(related_gene)

        chr = kwargs.get('chr',None)
        if chr is not None:
            self.set_relatedChromosome(chr)

        # set the ref genome if not None
        ref_genome = kwargs.get('ref_genome',None)
        if ref_genome:
            self.set_referenceGenome(ref_genome)

        car_ctx_rep = kwargs.get('car_ctx_rep',{})

        if car_ctx_rep:
            start = {'index': car_ctx_rep['coordinates'][0]['start'] }
            end = {'index': car_ctx_rep['coordinates'][0]['end'] }
            ref_allele = car_ctx_rep['coordinates'][0]['referenceAllele']
            ref_coord = {'start':start, 'end':end, 'refState': ref_allele }
            self.data['referenceCoordinate'] = ref_coord
            self.data['state'] = car_ctx_rep['coordinates'][0]['allele']

        # this is meant to be called after the car_contextual_allele data elements have been added to 'referenceCoordinate'
        # this method will overlay the items that are additional, or add them if no car_contextual_allele was found.
        self.data['alleleName'] = []
        hgvs = kwargs.get('hgvs',None)
        nm = { 'nameType': 'hgvs', 'name':hgvs }
        self.data['alleleName'].append(nm)

        if 'referenceCoordinate' not in self.data:
            self.data['referenceCoordinate'] = {}

        # if the referenceCoordinate.referenceSequence is not set then use the first accession extracted
        if 'referenceSequence' not in self.data['referenceCoordinate'] and accession:
            self.data['referenceCoordinate'].update( {'referenceSequence': {'label': accession}} )

        # now determine if this is the preferred contextual allele based on the preferred sequence
        # rule for preferred contextual variant is...
        #    if a prefered sequence exists it must match the hgvs sequence of the ctx allele
        #    else if no preferred sequence it must be the ref_genome for GRCh38.
        if (preferred_sequence is not None) and (preferred_sequence == accession):
            self.set_preferred(True)
        elif (preferred_sequence is None) and (ref_genome == 'GRCh38'):
            self.set_preferred(True)

    @get_factory_entity('SEPIO-CG:65906')
    def set_referenceGenome(self, x):
        self.data[PROP_A952_REFERENCEGENOME_KEY] = x
    def get_referenceGenome(self):
        return self.data[PROP_A952_REFERENCEGENOME_KEY]
    def set_preferred(self, x):
        self.data[PROP_A921_PREFERRED_KEY] = x
    def get_preferred(self):
        return self.data[PROP_A921_PREFERRED_KEY]
    @get_factory_entity('SEPIO-CG:65905')
    def set_relatedChromosome(self,x):
        self.data[PROP_A950_RELATEDCHROMOSOME_KEY] = x
    def get_relatedChromosome(self):
        return self.data[PROP_A950_RELATEDCHROMOSOME_KEY]
    @get_factory_entity('SEPIO:0000396')
    def set_relatedGene(self,x):
        self.data[PROP_A951_RELATEDGENE_KEY] = x
    def get_relatedGene(self):
        return self.data[PROP_A951_RELATEDGENE_KEY]
