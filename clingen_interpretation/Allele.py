from clingen_interpretation.node import Node
from clingen_interpretation.entities_generated import *
from clingen_interpretation.interpretation_constants import *
import re


'''
class Coding(Node):
    """We need Coding because Allele is defined in terms of it"""
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = 'Coding'
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

# this method attempts to extract the NM_ or NC_ accession from
# a clinvar formatted variant title.
def extract_accession(clinvar_variant_title):
    acxn = None
    m = re.search('^(N[MC]_[0-9]+\.[0-9]+).*$', clinvar_variant_title)
    if m is not None:
        acxn = m.group(1)
    return acxn

# attempt to derive the chromosome from the NCBI NC_* refseq accession.
def derive_chromosome(sequence):
    chr = None
    m = re.search('^NC_0+([1-2]{0,1}[0-9]{1}|12920)\.[0-9]+$', sequence)
    if m is not None:
        val = m.group(1)
        if (val >= '1') and (val <= '22'):
            chr = val
        elif val == '23':
            chr = 'X'
        elif val == '24':
            chr = 'Y'
        elif val == '12920':
            chr = 'M'
    return chr

# this method attempts to extract the gene symbol from
# a clinvar formatted variant title.
def extract_gene_symbol(clinvar_variant_title):
    gene_symbol = None
    m = re.search('^N[MC]_[0-9]+\.[0-9]+\(([A-Z0-9]+)\).*$', clinvar_variant_title)
    if m is not None:
        gene = m.group(1)
    return gene

#This is not necessarily useful outside of the DMWG Interpretation Library because we are keeping the
# data in the format expected for the InterpretationEncoder. In particular, rather than having
# data members, we just shove all the data into the self.data element.
#
# TODO Fix all the type names and stuff.
class Variant(Node):
    def __init__(self, car_rep, clinvar_variant_title=None):
        self.data={}
        self.data[DMWG_ID_KEY] = car_rep[ALLELE_REGISTRY_ID_KEY]
        self.data[DMWG_TYPE_KEY] = 'CanonicalAllele'
        self.data['canonicalAlleleType'] = car_rep['type']
        #todo: double check this?
        self.data['complexity'] = 'simple'

        # the preferred sequence is the accession in the clinvar_variant_title
        preferred_sequence = None
        if clinvar_variant_title is not None:
            self.data[DMWG_A200_LABEL_KEY] = clinvar_variant_title
            preferred_sequence = extract_accession(clinvar_variant_title)
        if 'externalRecords' in car_rep:
            car_external_ids = car_rep['externalRecords']
            if 'ClinVarVariations' in car_external_ids:
                for cva in car_external_ids['ClinVarVariations']:
                    self.add_external_identifier('ClinVar', cva['variationId'], clinvar_variant_title)
            if 'dbSNP' in car_external_ids:
                for rsid in car_external_ids['dbSNP']:
                    self.add_external_identifier('dbSNP', rsid['rs'])
        self.data['relatedContextualAllele'] = []
        for gen_ctx_allele in car_rep['genomicAlleles']:
            ctx_allele = ContextualAllele( gen_ctx_allele, car_rep[ALLELE_REGISTRY_ID_KEY], 'genomic', preferred_sequence)
            if 'referenceGenome' in gen_ctx_allele:
                ctx_allele.set_referenceGenome(gen_ctx_allele['referenceGenome'])
                # if no preferred sequence then set GRCh38 as the preferred sequence by default
                if (preferred_sequence is None) and (gen_ctx_allele['referenceGenome'] == 'GRCh38'):
                    ctx_allele.set_preferred(True)
            if 'chromosome' in gen_ctx_allele:
                ctx_allele.set_relatedChromosome(gen_ctx_allele['chromosome'])
            self.data['relatedContextualAllele'].append( ctx_allele )
        for trx_ctx_allele in car_rep['transcriptAlleles']:
            ctx_allele = ContextualAllele( trx_ctx_allele, car_rep[ALLELE_REGISTRY_ID_KEY], 'transcript', preferred_sequence)
            if 'gene' in trx_ctx_allele:
                ctx_allele.set_relatedGene({'id': 'NCBIGene:'+str(trx_ctx_allele['geneNCBI_id']), 'label': trx_ctx_allele['geneSymbol']})
            self.data['relatedContextualAllele'].append( ctx_allele )
    def add_external_identifier(self, source, value, display=None):
        if 'relatedIdentifier' not in self.data:
            self.data['relatedIdentifier'] = []
        #if source == 'ClinVar':
        #    system = 'http://www.ncbi.nlm.nih.gov/clinvar/variation/'
        #elif source == 'dbSNP':
        #    system = 'http://www.ncbi.nlm.nih.gov/snp/'
        ext_identifier = { "id": "%s:%s" % (source,value)  }
        if display is not None:
            ext_identifier = { "label" : display }
        self.data['relatedIdentifier'].append(ext_identifier)
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

class ContextualAllele(Node):
    def __init__(self, ctx_allele_rep, canonical_allele_id, allele_type, preferred_sequence=None):
        self.data = {}
        self.data[DMWG_TYPE_KEY] = 'ContextualAllele'
        self.data['relatedCanonicalAllele'] = canonical_allele_id
        self.data['contextualAlleleType'] = allele_type
        self.data['state'] = ctx_allele_rep['coordinates'][0]['allele']
        self.data['alleleName'] = []
        seqnames = []
        for hgvs in ctx_allele_rep['hgvs']:
            nm = { 'nameType':'hgvs', 'name':hgvs }
            self.data['alleleName'].append(nm)
            seqnames.append( hgvs.split(':')[0] )
        bestname = seqnames[0]
        if (preferred_sequence is not None) and (preferred_sequence == bestname):
            self.set_preferred(True)
        ref_sequence = {'id': ctx_allele_rep['referenceSequence'], 'label': bestname}
        start = {'index': ctx_allele_rep['coordinates'][0]['start'] }
        end = {'index': ctx_allele_rep['coordinates'][0]['end'] }
        ref_allele = ctx_allele_rep['coordinates'][0]['referenceAllele']
        ref_coord = {'referenceSequence': ref_sequence, 'start':start, 'end':end, 'refState': ref_allele }
        self.data['referenceCoordinate'] = ref_coord
    @get_factory_entity('SEPIO-CG:65906')
    def set_referenceGenome(self, x):
        self.data[DMWG_A952_REFERENCEGENOME_KEY] = x
    def get_referenceGenome(self):
        return self.data[DMWG_A952_REFERENCEGENOME_KEY]
    def set_preferred(self, x):
        self.data[DMWG_A921_PREFERRED_KEY] = x
    def get_preferred(self):
        return self.data[DMWG_A921_PREFERRED_KEY]
    @get_factory_entity('SEPIO-CG:65905')
    def set_relatedChromosome(self,x):
        self.data[DMWG_A950_RELATEDCHROMOSOME_KEY] = x
    def get_relatedChromosome(self):
        return self.data[DMWG_A950_RELATEDCHROMOSOME_KEY]
    @get_factory_entity('SEPIO:0000396')
    def set_relatedGene(self,x):
        self.data[DMWG_A951_RELATEDGENE_KEY] = x
    def get_relatedGene(self):
        return self.data[DMWG_A951_RELATEDGENE_KEY]

class ClinVarVariant(Node):
    """In the case when we have something like a structural variant, CAR won't handle it, so we need to make an allele
    from just the ClinVar allele."""
    def __init__(self, vci_rep, clinvar_variant_title=None ):
        self.data={}
        cvid="ClinVar:"+vci_rep['clinvarVariantId']
        self.data[DMWG_ID_KEY] = cvid
        self.data[DMWG_TYPE_KEY] = 'CanonicalAllele'
        if clinvar_variant_title is not None:
            self.data[DMWG_A200_LABEL_KEY] = clinvar_variant_title
        preferred_sequence = extract_accession( clinvar_variant_title )
        gene_symbol = extract_gene_symbol( clinvar_variant_title )
        self.add_external_identifier('ClinVar', vci_rep['clinvarVariantId'], clinvar_variant_title)
        self.data['relatedContextualAllele'] = []
        for ref in ['GRCh38','GRCh37','NCBI36']:
            if ref in vci_rep['hgvsNames']:
                hgvs = vci_rep['hgvsNames'][ref]
                clinvar_ctx_allele = ClinVarContextualAllele(cvid, 'genomic', hgvs, preferred_sequence)
                clinvar_ctx_allele.set_referenceGenome(ref)
                sequence = hgvs.split(':')[0]
                if (sequence is not None) and (sequence == preferred_sequence):
                    clinvar_ctx_allele.set_preferred(True)
                    # only set gene symbol on preferred because it is linked in the clinvar_variant_title
                    if gene_symbol is not None:
                        clinvar_ctx_allele.set_relatedGene(gene_symbol)
                chr = derive_chromosome(sequence)
                if chr is not None:
                    clinvar_ctx_allele.set_relatedChromosome(chr)
                self.data['relatedContextualAllele'].append(clinvar_ctx_allele)
        if 'others' in vci_rep['hgvsNames']:
            for hgvs in vci_rep['hgvsNames']['others']:
                if re.search('^((NC|NG)_[0-9]+\.[0-9]{1,2}|LRG_[0-9]+):g\..*$', hgvs):
                    alleleType = 'genomic'
                elif re.search('^((NM|NR|XM|XR)_[0-9]+\.[0-9]{1,2}|LRG_[0-9]+t[0-9]+|ENST[0-9]+\.[0-9]+):(c|n|r)\..*$', hgvs):
                    alleleType = 'transcript'
                elif re.search('^((NP|XP)_[0-9]+\.[0-9]{1,2}|LRG_[0-9]+p[0-9]+|ENSP[0-9]+\.[0-9]+):p\..*$', hgvs):
                    alleleType = 'protein'
                else:
                    alleleType = None
                clinvar_ctx_allele = ClinVarContextualAllele(cvid, alleleType, hgvs, preferred_sequence)
                sequence = hgvs.split(':')[0]
                if (sequence is not None) and (sequence == preferred_sequence):
                    clinvar_ctx_allele.set_preferred(True)
                    # only set gene symbol on preferred because it is linked in the clinvar_variant_title
                    if gene_symbol is not None:
                        clinvar_ctx_allele.set_relatedGene(gene_symbol)
                self.data['relatedContextualAllele'].append(clinvar_ctx_allele)
    def add_external_identifier(self,source,value,display=None):
        if 'relatedIdentifier' not in self.data:
            self.data['relatedIdentifier'] = []
        ext_identifier = { "id": "%s:%s" % (source,value)  }
        if display is not None:
            ext_identifier = { "label" : display }
        self.data['relatedIdentifier'].append(ext_identifier)

class ClinVarContextualAllele(Node):
    def __init__(self, canonical_allele_id, allele_type, hgvs, preferred_sequence):
        self.data = {}
        self.data[DMWG_TYPE_KEY] = 'ContextualAllele'
        self.data['relatedCanonicalAllele'] = canonical_allele_id
        if allele_type is not None:
            self.data['contextualAlleleType'] = allele_type
        nm = { 'nameType':'hgvs', 'name':hgvs }
        self.data['alleleName'] = []
        self.data['alleleName'].append(nm)
    @get_factory_entity('SEPIO-CG:65906')
    def set_referenceGenome(self, x):
        self.data[DMWG_A952_REFERENCEGENOME_KEY] = x
    def get_referenceGenome(self):
        return self.data[DMWG_A952_REFERENCEGENOME_KEY]
    def set_preferred(self, x):
        self.data[DMWG_A921_PREFERRED_KEY] = x
    def get_preferred(self):
        return self.data[DMWG_A921_PREFERRED_KEY]
    @get_factory_entity('SEPIO-CG:65905')
    def set_relatedChromosome(self,x):
        self.data[DMWG_A950_RELATEDCHROMOSOME_KEY] = x
    def get_relatedChromosome(self):
        return self.data[DMWG_A950_RELATEDCHROMOSOME_KEY]
    @get_factory_entity('SEPIO:0000396')
    def set_relatedGene(self,x):
        self.data[DMWG_A951_RELATEDGENE_KEY] = x
    def get_relatedGene(self):
        return self.data[DMWG_A951_RELATEDGENE_KEY]
