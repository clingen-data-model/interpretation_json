from node import Node
from entities_generated import *
from interpretation_constants import *


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

#This is not necessarily useful outside of the DMWG Interpretation Library because we are keeping the
# data in the format expected for the InterpretationEncoder. In particular, rather than having
# data members, we just shove all the data into the self.data element.
#
# TODO Fix all the type names and stuff.
class Variant(Node):
    def __init__(self,car_rep,preferred_sequence=None):
        self.data={}
        self.data[DMWG_ID_KEY] = car_rep[ALLELE_REGISTRY_ID_KEY]
        self.data[DMWG_TYPE_KEY] = 'CanonicalAllele'
        self.data['canonicalAlleleType'] = car_rep['type']
        #todo: double check this?
        self.data['complexity'] = 'simple'
        if 'externalRecords' in car_rep:
            car_external_ids = car_rep['externalRecords']
            if 'ClinVarVariations' in car_external_ids:
                label = None
                if (len(car_external_ids['ClinVarVariations']) == 1) and \
                    ('ClinVarAlleles' in car_external_ids) and \
                    ( len(car_external_ids['ClinVarAlleles']) == 1) :
                    label=car_external_ids['ClinVarAlleles'][0]['preferredName']
                for cva in car_external_ids['ClinVarVariations']:
                    self.add_external_identifier('ClinVar', cva['variationId'], label)
            if 'dbSNP' in car_external_ids:
                for rsid in car_external_ids['dbSNP']:
                    self.add_external_identifier('dbSNP', rsid['rs'])
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
            if (preferred_sequence is None and ctx_allele_rep['referenceGenome'] == 'GRCh38'):
                self.data['preferred'] = True
        bestname = seqnames[0]
        if preferred_sequence is not None and preferred_sequence == bestname:
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
    def __init__(self,vci_rep):
        self.data={}
        cvid="ClinVar:"+vci_rep['clinvarVariantId']
        self.data[DMWG_ID_KEY] = cvid
        self.data[DMWG_TYPE_KEY] = 'CanonicalAllele'
        label = vci_rep['clinvarVariantTitle']
        self.add_external_identifier('ClinVar', vci_rep['clinvarVariantId'], label)
        self.data['relatedContextualAllele'] = []
        for ref in ['GRCh38','GRCh37']:
            if ref in vci_rep['hgvsNames']:
                self.data['relatedContextualAllele'].append(ClinVarContextualAllele(cvid,'genomic',vci_rep['hgvsNames'][ref],ref))
        if 'others' in vci_rep['hgvsNames']:
            for hgvs in vci_rep['hgvsNames']['others']:
                self.data['relatedContextualAllele'].append(ClinVarContextualAllele(cvid,'transcript',hgvs))
    def add_external_identifier(self,source,value,display=None):
        if 'relatedIdentifier' not in self.data:
            self.data['relatedIdentifier'] = []
        ext_identifier = { "id": "%s:%s" % (source,value)  }
        if display is not None:
            ext_identifier = { "label" : display }
        self.data['relatedIdentifier'].append(ext_identifier)


class ClinVarContextualAllele(Node):
    def __init__(self,canonical_allele_id,allele_type,hgvs,ref_genome=None):
        self.data = {}
        self.data[DMWG_TYPE_KEY] = 'ContextualAllele'
        self.data['relatedCanonicalAllele'] = canonical_allele_id
        self.data['contextualAlleleType'] = allele_type
        self.data['alleleName'] = [hgvs]
        seqnames = []
        nm = { 'nameType':'hgvs', 'name':hgvs }
        self.data['alleleName'].append(nm)
        seqnames.append( hgvs.split(':')[0] )
        if ref_genome is not None:
            self.ref_genome = ref_genome
 
