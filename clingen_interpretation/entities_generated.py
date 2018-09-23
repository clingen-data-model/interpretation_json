from interpretation_constants import *
from interpretation_generated import Entity
from domain_entity_factory import get_factory_entity
from node import Node

class DomainEntity(Entity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_DOMAINENTITY_TYPE 
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class VariantPathogenicityInterpretationGuideline(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_VARIANTPATHOGENICITYINTERPRETATIONGUIDELINE_TYPE 
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

class ReferenceCoordinate(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REFERENCECOORDINATE_TYPE 
    @get_factory_entity('SEPIO-CG:65119')
    def set_referenceSequence(self,x):
        self.data[DMWG_A933_REFERENCESEQUENCE_KEY] = x
    def get_referenceSequence(self):
        return self.data[DMWG_A933_REFERENCESEQUENCE_KEY]
    def set_start(self,x):
        self.data[DMWG_A931_START_KEY] = x
    def get_start(self):
        return self.data[DMWG_A931_START_KEY]
    def set_end(self,x):
        self.data[DMWG_A932_END_KEY] = x
    def get_end(self):
        return self.data[DMWG_A932_END_KEY]
    def set_refState(self,x):
        self.data[DMWG_A930_REFSTATE_KEY] = x
    def get_refState(self):
        return self.data[DMWG_A930_REFSTATE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class ContextualAlleleName(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONTEXTUALALLELENAME_TYPE 
    def set_name(self,x):
        self.data[DMWG_A920_NAME_KEY] = x
    def get_name(self):
        return self.data[DMWG_A920_NAME_KEY]
    def set_preferred(self,x):
        self.data[DMWG_A921_PREFERRED_KEY] = x
    def get_preferred(self):
        return self.data[DMWG_A921_PREFERRED_KEY]
    @get_factory_entity('SEPIO-CG:65903')
    def set_nameType(self,x):
        self.data[DMWG_A943_NAMETYPE_KEY] = x
    def get_nameType(self):
        return self.data[DMWG_A943_NAMETYPE_KEY]
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
    def set_prefix(self,x):
        self.data[DMWG_A152_PREFIX_KEY] = x
    def get_prefix(self):
        return self.data[DMWG_A152_PREFIX_KEY]
    def set_urlPattern(self,x):
        self.data[DMWG_A154_URLPATTERN_KEY] = x
    def get_urlPattern(self):
        return self.data[DMWG_A154_URLPATTERN_KEY]
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
    def add_hasPart(self,x):
        if not DMWG_A067_HASPART_KEY in self.data:
            self.data[DMWG_A067_HASPART_KEY] = []
        self.data[DMWG_A067_HASPART_KEY].append( x ) 
    def get_hasPart(self):
        return self.data[DMWG_A067_HASPART_KEY]
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

class GeneticCondition(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_GENETICCONDITION_TYPE 
    @get_factory_entity('SEPIO:0000372')
    def add_disease(self,x):
        if not DMWG_A158_DISEASE_KEY in self.data:
            self.data[DMWG_A158_DISEASE_KEY] = []
        self.data[DMWG_A158_DISEASE_KEY].append( x ) 
    def get_disease(self):
        return self.data[DMWG_A158_DISEASE_KEY]
    @get_factory_entity('SEPIO:0000375')
    def add_phenotype(self,x):
        if not DMWG_A141_PHENOTYPE_KEY in self.data:
            self.data[DMWG_A141_PHENOTYPE_KEY] = []
        self.data[DMWG_A141_PHENOTYPE_KEY].append( x ) 
    def get_phenotype(self):
        return self.data[DMWG_A141_PHENOTYPE_KEY]
    @get_factory_entity('SEPIO:0000416')
    def set_inheritancePattern(self,x):
        self.data[DMWG_A142_INHERITANCEPATTERN_KEY] = x
    def get_inheritancePattern(self):
        return self.data[DMWG_A142_INHERITANCEPATTERN_KEY]
    @get_factory_entity('SEPIO:0000396')
    def set_gene(self,x):
        self.data[DMWG_A143_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_A143_GENE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class VariantPathogenicityInterpretationCriterion(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_VARIANTPATHOGENICITYINTERPRETATIONCRITERION_TYPE 
    @get_factory_entity('SEPIO:0000353')
    def set_defaultStrength(self,x):
        self.data[DMWG_A153_DEFAULTSTRENGTH_KEY] = x
    def get_defaultStrength(self):
        return self.data[DMWG_A153_DEFAULTSTRENGTH_KEY]
    def set_usageNotes(self,x):
        self.data[DMWG_A150_USAGENOTES_KEY] = x
    def get_usageNotes(self):
        return self.data[DMWG_A150_USAGENOTES_KEY]
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
    def add_hasPart(self,x):
        if not DMWG_A068_HASPART_KEY in self.data:
            self.data[DMWG_A068_HASPART_KEY] = []
        self.data[DMWG_A068_HASPART_KEY].append( x ) 
    def get_hasPart(self):
        return self.data[DMWG_A068_HASPART_KEY]
    @get_factory_entity('SEPIO:0000338')
    def set_zygosity(self,x):
        self.data[DMWG_A069_ZYGOSITY_KEY] = x
    def get_zygosity(self):
        return self.data[DMWG_A069_ZYGOSITY_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class Position(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_POSITION_TYPE 
    def set_index(self,x):
        self.data[DMWG_A940_INDEX_KEY] = x
    def get_index(self):
        return self.data[DMWG_A940_INDEX_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

