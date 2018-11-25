from node import Node
from entities_generated import *
from interpretation_constants import *
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
    def __init__(self,car_rep, clinvar_variant_title=None):
        self.data={}
        self.data[DMWG_ID_KEY] = car_rep[ALLELE_REGISTRY_ID_KEY]
        self.data[DMWG_TYPE_KEY] = 'CanonicalAllele'
        self.data['canonicalAlleleType'] = car_rep['type']
        if clinvar_variant_title is not None:
            self.data[DMWG_A200_LABEL_KEY] = clinvar_variant_title
        #todo: double check this?
        self.data['complexity'] = 'simple'

        if 'externalRecords' in car_rep:
            car_external_ids = car_rep['externalRecords']
            if 'ClinVarVariations' in car_external_ids:
                for cva in car_external_ids['ClinVarVariations']:
                    self.add_external_identifier('ClinVar', cva['variationId'], clinvar_variant_title)
            if 'dbSNP' in car_external_ids:
                for rsid in car_external_ids['dbSNP']:
                    self.add_external_identifier('dbSNP', rsid['rs'])
        preferred_sequence = extract_accession(clinvar_variant_title)
        self.data['relatedContextualAllele'] = []
        for gen_ctx_allele in car_rep['genomicAlleles']:
            self.data['relatedContextualAllele'].append( ContextualAllele( gen_ctx_allele, car_rep[ALLELE_REGISTRY_ID_KEY], 'genomic',preferred_sequence) )
        for trx_ctx_allele in car_rep['transcriptAlleles']:
            self.data['relatedContextualAllele'].append( ContextualAllele( trx_ctx_allele, car_rep[ALLELE_REGISTRY_ID_KEY], 'transcript',preferred_sequence) )

    def add_external_identifier(self,source,value,display=None):
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
    def __init__(self,ctx_allele_rep,canonical_allele_id, allele_type, preferred_sequence=None):
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
        if 'referenceGenome' in ctx_allele_rep:
            self.ref_genome = ctx_allele_rep['referenceGenome']
            if (preferred_sequence is None) and (ctx_allele_rep['referenceGenome'] == 'GRCh38'):
                self.data['preferred'] = True
        bestname = seqnames[0]
        if (preferred_sequence is not None) and (preferred_sequence == bestname):
            self.data['preferred'] = True
        ref_sequence = {'id': ctx_allele_rep['referenceSequence'], 'label': bestname}
        start = {'index': ctx_allele_rep['coordinates'][0]['start'] }
        end = {'index': ctx_allele_rep['coordinates'][0]['end'] }
        ref_allele = ctx_allele_rep['coordinates'][0]['referenceAllele']
        ref_coord = {'referenceSequence': ref_sequence, 'start':start, 'end':end, 'refState': ref_allele }
        self.data['referenceCoordinate'] = ref_coord
        if 'chromosome' in ctx_allele_rep:
            self.data['chromosome'] = ctx_allele_rep['chromosome']
        if 'gene' in ctx_allele_rep:
            self.data['gene'] = {'id': 'NCBIGene:'+str(ctx_allele_rep['geneNCBI_id']), 'label': ctx_allele_rep['geneSymbol']}

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
        for ref in ['GRCh38','GRCh37']:
            if ref in vci_rep['hgvsNames']:
                self.data['relatedContextualAllele'].append(ClinVarContextualAllele(cvid, 'genomic', vci_rep['hgvsNames'][ref], preferred_sequence, gene_symbol, ref))
        if 'others' in vci_rep['hgvsNames']:
            for hgvs in vci_rep['hgvsNames']['others']:
                if hgvs.startswith(('NC', 'NG')):
                    alleleType = 'genomic'
                elif hgvs.startswith(('NM', 'NR', 'XM')):
                    alleleType = 'transcript'
                elif hgvs.startswith(('NP', 'XP')):
                    alleleType = 'protein'
                else:
                    alleleType = None
                self.data['relatedContextualAllele'].append(ClinVarContextualAllele(cvid, alleleType, hgvs, preferred_sequence, gene_symbol))
    def add_external_identifier(self,source,value,display=None):
        if 'relatedIdentifier' not in self.data:
            self.data['relatedIdentifier'] = []
        ext_identifier = { "id": "%s:%s" % (source,value)  }
        if display is not None:
            ext_identifier = { "label" : display }
        self.data['relatedIdentifier'].append(ext_identifier)

class ClinVarContextualAllele(Node):
    def __init__(self,canonical_allele_id,allele_type,hgvs,preferred_sequence,gene_symbol,ref_genome=None):
        self.data = {}
        self.data[DMWG_TYPE_KEY] = 'ContextualAllele'
        self.data['relatedCanonicalAllele'] = canonical_allele_id
        if allele_type is not None:
            self.data['contextualAlleleType'] = allele_type
        nm = { 'nameType':'hgvs', 'name':hgvs }
        self.data['alleleName'] = []
        self.data['alleleName'].append(nm)
        if ref_genome is not None:
            self.ref_genome = ref_genome
        sequence = hgvs.split(':')[0]
        if (sequence is not None) and (sequence == preferred_sequence):
            self.data['preferred'] = True
            if gene_symbol is not None:
                self.data['gene'] = {'label': gene_symbol}
        chr = derive_chromosome(sequence)
        if chr is not None:
            self.data['chromosome'] = chr
