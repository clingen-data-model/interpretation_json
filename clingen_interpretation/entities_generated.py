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
        self.data[DMWG_DOMAINENTITY_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_DOMAINENTITY_DESCRIPTION_KEY]
    def set_label(self,x):
        self.data[DMWG_DOMAINENTITY_LABEL_KEY] = x
    def get_label(self):
        return self.data[DMWG_DOMAINENTITY_LABEL_KEY]
    def add_synonym(self,x):
        if not DMWG_DOMAINENTITY_SYNONYM_KEY in self.data:
            self.data[DMWG_DOMAINENTITY_SYNONYM_KEY] = []
        self.data[DMWG_DOMAINENTITY_SYNONYM_KEY].append( x ) 
    def get_synonym(self):
        return self.data[DMWG_DOMAINENTITY_SYNONYM_KEY]

class ScoringAlgorithm(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_SCORINGALGORITHM_TYPE 
    def set_description(self,x):
        self.data[DMWG_SCORINGALGORITHM_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_SCORINGALGORITHM_DESCRIPTION_KEY]

class AssertionMethod(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ASSERTIONMETHOD_TYPE 
    def set_description(self,x):
        self.data[DMWG_ASSERTIONMETHOD_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_ASSERTIONMETHOD_DESCRIPTION_KEY]
    def set_url(self,x):
        self.data[DMWG_ASSERTIONMETHOD_URL_KEY] = x
    def get_url(self):
        return self.data[DMWG_ASSERTIONMETHOD_URL_KEY]
    def set_version(self,x):
        self.data[DMWG_ASSERTIONMETHOD_VERSION_KEY] = x
    def get_version(self):
        return self.data[DMWG_ASSERTIONMETHOD_VERSION_KEY]
    @get_factory_entity('ScoringAlgorithm')
    def set_scoringAlgorithm(self,x):
        self.data[DMWG_ASSERTIONMETHOD_SCORINGALGORITHM_KEY] = x
    def get_scoringAlgorithm(self):
        return self.data[DMWG_ASSERTIONMETHOD_SCORINGALGORITHM_KEY]

class Individual(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INDIVIDUAL_TYPE 
    def set_description(self,x):
        self.data[DMWG_INDIVIDUAL_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_INDIVIDUAL_DESCRIPTION_KEY]

class Disease(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_DISEASE_TYPE 

class LocusSpecificityType(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_LOCUSSPECIFICITYTYPE_TYPE 

class AscertainmentType(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ASCERTAINMENTTYPE_TYPE 

class RegionAnnotationType(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REGIONANNOTATIONTYPE_TYPE 

class Significance(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_SIGNIFICANCE_TYPE 

class MolecularConsequenceType(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_MOLECULARCONSEQUENCETYPE_TYPE 

class ReferenceSequence(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REFERENCESEQUENCE_TYPE 

class Family(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_FAMILY_TYPE 
    def set_label(self,x):
        self.data[DMWG_FAMILY_LABEL_KEY] = x
    def get_label(self):
        return self.data[DMWG_FAMILY_LABEL_KEY]
    def set_description(self,x):
        self.data[DMWG_FAMILY_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_FAMILY_DESCRIPTION_KEY]

class PenetranceType(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_PENETRANCETYPE_TYPE 

class EvidenceLineStrength(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_EVIDENCELINESTRENGTH_TYPE 

class AlleleInheritanceType(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELEINHERITANCETYPE_TYPE 

class ContributoryRole(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONTRIBUTORYROLE_TYPE 

class ConditionMechanismStrength(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONDITIONMECHANISMSTRENGTH_TYPE 

class Phenotype(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_PHENOTYPE_TYPE 

class ReferenceSequence(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REFERENCESEQUENCE_TYPE 
    def set_accession(self,x):
        self.data[DMWG_REFERENCESEQUENCE_ACCESSION_KEY] = x
    def get_accession(self):
        return self.data[DMWG_REFERENCESEQUENCE_ACCESSION_KEY]
    @get_factory_entity('ReferenceSequence')
    def add_produces(self,x):
        if not DMWG_REFERENCESEQUENCE_PRODUCES_KEY in self.data:
            self.data[DMWG_REFERENCESEQUENCE_PRODUCES_KEY] = []
        self.data[DMWG_REFERENCESEQUENCE_PRODUCES_KEY].append( x ) 
    def get_produces(self):
        return self.data[DMWG_REFERENCESEQUENCE_PRODUCES_KEY]
    @get_factory_entity('ReferenceSequence')
    def add_producedBy(self,x):
        if not DMWG_REFERENCESEQUENCE_PRODUCEDBY_KEY in self.data:
            self.data[DMWG_REFERENCESEQUENCE_PRODUCEDBY_KEY] = []
        self.data[DMWG_REFERENCESEQUENCE_PRODUCEDBY_KEY].append( x ) 
    def get_producedBy(self):
        return self.data[DMWG_REFERENCESEQUENCE_PRODUCEDBY_KEY]

class Gene(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_GENE_TYPE 
    def set_geneSymbol(self,x):
        self.data[DMWG_GENE_GENESYMBOL_KEY] = x
    def get_geneSymbol(self):
        return self.data[DMWG_GENE_GENESYMBOL_KEY]

class Criterion(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CRITERION_TYPE 
    @get_factory_entity('EvidenceLineStrength')
    def set_defaultStrength(self,x):
        self.data[DMWG_CRITERION_DEFAULTSTRENGTH_KEY] = x
    def get_defaultStrength(self):
        return self.data[DMWG_CRITERION_DEFAULTSTRENGTH_KEY]

class PopulationType(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_POPULATIONTYPE_TYPE 

class BenignMissenseVariationRate(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_BENIGNMISSENSEVARIATIONRATE_TYPE 

class NullAllele(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_NULLALLELE_TYPE 

class RegionAllelesOutcome(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REGIONALLELESOUTCOME_TYPE 

class ConditionStatus(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONDITIONSTATUS_TYPE 

class Conservation(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONSERVATION_TYPE 

class ParentalConfirmation(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_PARENTALCONFIRMATION_TYPE 

class Phase(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_PHASE_TYPE 

class AllelicState(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELICSTATE_TYPE 

class ModeOfInheritance(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_MODEOFINHERITANCE_TYPE 

class ReferenceSequenceRelatedType(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REFERENCESEQUENCERELATEDTYPE_TYPE 

class MechanismType(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_MECHANISMTYPE_TYPE 

class PredictionType(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_PREDICTIONTYPE_TYPE 

class CriterionEvaluation(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CRITERIONEVALUATION_TYPE 

class AlleleFunctionalImpactType(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELEFUNCTIONALIMPACTTYPE_TYPE 

class InconsistentSegregationObserved(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INCONSISTENTSEGREGATIONOBSERVED_TYPE 

