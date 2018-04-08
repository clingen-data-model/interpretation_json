from interpretation_constants import *
from domain_entity_factory import get_factory_entity
from node import Node

class DomainEntity(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_DOMAINENTITY_TYPE 
    def set_description(self,x):
        self.data[DMWG_A075_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_A075_DESCRIPTION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class AssertionMethod(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ASSERTIONMETHOD_TYPE 
    def set_url(self,x):
        self.data[DMWG_A156_URL_KEY] = x
    def get_url(self):
        return self.data[DMWG_A156_URL_KEY]
    def set_version(self,x):
        self.data[DMWG_A173_VERSION_KEY] = x
    def get_version(self):
        return self.data[DMWG_A173_VERSION_KEY]
    @get_factory_entity('SEPIO-CG:65133')
    def set_scoringAlgorithm(self,x):
        self.data[DMWG_A174_SCORINGALGORITHM_KEY] = x
    def get_scoringAlgorithm(self):
        return self.data[DMWG_A174_SCORINGALGORITHM_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class Genotype(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_GENOTYPE_TYPE 
    def add_haplotype(self,x):
        if not DMWG_A068_HAPLOTYPE_KEY in self.data:
            self.data[DMWG_A068_HAPLOTYPE_KEY] = []
        self.data[DMWG_A068_HAPLOTYPE_KEY].append( x ) 
    def get_haplotype(self):
        return self.data[DMWG_A068_HAPLOTYPE_KEY]
    def set_zygosity(self,x):
        self.data[DMWG_A069_ZYGOSITY_KEY] = x
    def get_zygosity(self):
        return self.data[DMWG_A069_ZYGOSITY_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class GeneticCondition(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_GENETICCONDITION_TYPE 
    def set_name(self,x):
        self.data[DMWG_A157_NAME_KEY] = x
    def get_name(self):
        return self.data[DMWG_A157_NAME_KEY]
    @get_factory_entity('SEPIO-CG:65117')
    def add_disease(self,x):
        if not DMWG_A158_DISEASE_KEY in self.data:
            self.data[DMWG_A158_DISEASE_KEY] = []
        self.data[DMWG_A158_DISEASE_KEY].append( x ) 
    def get_disease(self):
        return self.data[DMWG_A158_DISEASE_KEY]
    @get_factory_entity('SEPIO-CG:65118')
    def add_phenotype(self,x):
        if not DMWG_A141_PHENOTYPE_KEY in self.data:
            self.data[DMWG_A141_PHENOTYPE_KEY] = []
        self.data[DMWG_A141_PHENOTYPE_KEY].append( x ) 
    def get_phenotype(self):
        return self.data[DMWG_A141_PHENOTYPE_KEY]
    @get_factory_entity('SEPIO-CG:65107')
    def set_modeOfInheritance(self,x):
        self.data[DMWG_A142_MODEOFINHERITANCE_KEY] = x
    def get_modeOfInheritance(self):
        return self.data[DMWG_A142_MODEOFINHERITANCE_KEY]
    def set_gene(self,x):
        self.data[DMWG_A143_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_A143_GENE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class Haplotype(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_HAPLOTYPE_TYPE 
    def add_allele(self,x):
        if not DMWG_A067_ALLELE_KEY in self.data:
            self.data[DMWG_A067_ALLELE_KEY] = []
        self.data[DMWG_A067_ALLELE_KEY].append( x ) 
    def get_allele(self):
        return self.data[DMWG_A067_ALLELE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class SequenceLocation(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_SEQUENCELOCATION_TYPE 
    @get_factory_entity('SEPIO-CG:65119')
    def set_referenceSequence(self,x):
        self.data[DMWG_A052_REFERENCESEQUENCE_KEY] = x
    def get_referenceSequence(self):
        return self.data[DMWG_A052_REFERENCESEQUENCE_KEY]
    def set_start(self,x):
        self.data[DMWG_A053_START_KEY] = x
    def get_start(self):
        return self.data[DMWG_A053_START_KEY]
    def set_stop(self,x):
        self.data[DMWG_A054_STOP_KEY] = x
    def get_stop(self):
        return self.data[DMWG_A054_STOP_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class ReferenceSequence(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REFERENCESEQUENCE_TYPE 
    def set_accession(self,x):
        self.data[DMWG_A144_ACCESSION_KEY] = x
    def get_accession(self):
        return self.data[DMWG_A144_ACCESSION_KEY]
    @get_factory_entity('SEPIO-CG:65119')
    def add_produces(self,x):
        if not DMWG_A168_PRODUCES_KEY in self.data:
            self.data[DMWG_A168_PRODUCES_KEY] = []
        self.data[DMWG_A168_PRODUCES_KEY].append( x ) 
    def get_produces(self):
        return self.data[DMWG_A168_PRODUCES_KEY]
    @get_factory_entity('SEPIO-CG:65119')
    def add_producedBy(self,x):
        if not DMWG_A169_PRODUCEDBY_KEY in self.data:
            self.data[DMWG_A169_PRODUCEDBY_KEY] = []
        self.data[DMWG_A169_PRODUCEDBY_KEY].append( x ) 
    def get_producedBy(self):
        return self.data[DMWG_A169_PRODUCEDBY_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class IdentifierSystem(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_IDENTIFIERSYSTEM_TYPE 
    def set_description(self,x):
        self.data[DMWG_A147_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_A147_DESCRIPTION_KEY]
    def set_oid(self,x):
        self.data[DMWG_A151_OID_KEY] = x
    def get_oid(self):
        return self.data[DMWG_A151_OID_KEY]
    def set_iri(self,x):
        self.data[DMWG_A152_IRI_KEY] = x
    def get_iri(self):
        return self.data[DMWG_A152_IRI_KEY]
    def set_prefix(self,x):
        self.data[DMWG_A154_PREFIX_KEY] = x
    def get_prefix(self):
        return self.data[DMWG_A154_PREFIX_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class ContextualAllele(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONTEXTUALALLELE_TYPE 
    def set_relatedCanonicalAllele(self,x):
        self.data[DMWG_A137_RELATEDCANONICALALLELE_KEY] = x
    def get_relatedCanonicalAllele(self):
        return self.data[DMWG_A137_RELATEDCANONICALALLELE_KEY]
    def set_alleleName(self,x):
        self.data[DMWG_A138_ALLELENAME_KEY] = x
    def get_alleleName(self):
        return self.data[DMWG_A138_ALLELENAME_KEY]
    def add_legacyNames(self,x):
        if not DMWG_A139_LEGACYNAMES_KEY in self.data:
            self.data[DMWG_A139_LEGACYNAMES_KEY] = []
        self.data[DMWG_A139_LEGACYNAMES_KEY].append( x ) 
    def get_legacyNames(self):
        return self.data[DMWG_A139_LEGACYNAMES_KEY]
    def add_produces(self,x):
        if not DMWG_A170_PRODUCES_KEY in self.data:
            self.data[DMWG_A170_PRODUCES_KEY] = []
        self.data[DMWG_A170_PRODUCES_KEY].append( x ) 
    def get_produces(self):
        return self.data[DMWG_A170_PRODUCES_KEY]
    def add_producedBy(self,x):
        if not DMWG_A171_PRODUCEDBY_KEY in self.data:
            self.data[DMWG_A171_PRODUCEDBY_KEY] = []
        self.data[DMWG_A171_PRODUCEDBY_KEY].append( x ) 
    def get_producedBy(self):
        return self.data[DMWG_A171_PRODUCEDBY_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class Criterion(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CRITERION_TYPE 
    @get_factory_entity('SEPIO-CG:65116')
    def set_defaultStrength(self,x):
        self.data[DMWG_A153_DEFAULTSTRENGTH_KEY] = x
    def get_defaultStrength(self):
        return self.data[DMWG_A153_DEFAULTSTRENGTH_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class CanonicalAllele(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CANONICALALLELE_TYPE 
    def set_preferredCtxAllele(self,x):
        self.data[DMWG_A135_PREFERREDCTXALLELE_KEY] = x
    def get_preferredCtxAllele(self):
        return self.data[DMWG_A135_PREFERREDCTXALLELE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

