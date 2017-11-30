from interpretation_constants import *
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
    def set_userLabel(self,x):
        self.data[DMWG_DOMAINENTITY_USERLABEL_KEY] = x
    def get_userLabel(self):
        return self.data[DMWG_DOMAINENTITY_USERLABEL_KEY]

class ScoringAlgorithm(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_SCORINGALGORITHM_TYPE 

class AssertionMethod(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ASSERTIONMETHOD_TYPE 
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

class Genotype(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_GENOTYPE_TYPE 
    @get_factory_entity('Haplotype')
    def add_haplotype(self,x):
        if not DMWG_GENOTYPE_HAPLOTYPE_KEY in self.data:
            self.data[DMWG_GENOTYPE_HAPLOTYPE_KEY] = []
        self.data[DMWG_GENOTYPE_HAPLOTYPE_KEY].append( x ) 
    def get_haplotype(self):
        return self.data[DMWG_GENOTYPE_HAPLOTYPE_KEY]
    @get_factory_entity('AllelicState')
    def set_zygosity(self,x):
        self.data[DMWG_GENOTYPE_ZYGOSITY_KEY] = x
    def get_zygosity(self):
        return self.data[DMWG_GENOTYPE_ZYGOSITY_KEY]

class Individual(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INDIVIDUAL_TYPE 

class Disease(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_DISEASE_TYPE 

class LocusSpecificity(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_LOCUSSPECIFICITY_TYPE 

class Ascertainment(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ASCERTAINMENT_TYPE 

class RegionAnnotation(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REGIONANNOTATION_TYPE 

class Significance(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_SIGNIFICANCE_TYPE 

class Haplotype(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_HAPLOTYPE_TYPE 
    def add_allele(self,x):
        if not DMWG_HAPLOTYPE_ALLELE_KEY in self.data:
            self.data[DMWG_HAPLOTYPE_ALLELE_KEY] = []
        self.data[DMWG_HAPLOTYPE_ALLELE_KEY].append( x ) 
    def get_allele(self):
        return self.data[DMWG_HAPLOTYPE_ALLELE_KEY]

class MolecularConsequence(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_MOLECULARCONSEQUENCE_TYPE 

class Family(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_FAMILY_TYPE 

class Penetrance(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_PENETRANCE_TYPE 

class EvidenceLineStrength(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_EVIDENCELINESTRENGTH_TYPE 

class AlleleInheritance(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELEINHERITANCE_TYPE 

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

class IdentifierSystem(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_IDENTIFIERSYSTEM_TYPE 
    def set_label(self,x):
        self.data[DMWG_IDENTIFIERSYSTEM_LABEL_KEY] = x
    def get_label(self):
        return self.data[DMWG_IDENTIFIERSYSTEM_LABEL_KEY]
    def set_description(self,x):
        self.data[DMWG_IDENTIFIERSYSTEM_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_IDENTIFIERSYSTEM_DESCRIPTION_KEY]
    def set_oid(self,x):
        self.data[DMWG_IDENTIFIERSYSTEM_OID_KEY] = x
    def get_oid(self):
        return self.data[DMWG_IDENTIFIERSYSTEM_OID_KEY]
    def set_uri(self,x):
        self.data[DMWG_IDENTIFIERSYSTEM_URI_KEY] = x
    def get_uri(self):
        return self.data[DMWG_IDENTIFIERSYSTEM_URI_KEY]
    def set_prefix(self,x):
        self.data[DMWG_IDENTIFIERSYSTEM_PREFIX_KEY] = x
    def get_prefix(self):
        return self.data[DMWG_IDENTIFIERSYSTEM_PREFIX_KEY]

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

class Population(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_POPULATION_TYPE 

class BenignMissenseVariationRateOutcome(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_BENIGNMISSENSEVARIATIONRATEOUTCOME_TYPE 

class NullAlleleOutcome(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_NULLALLELEOUTCOME_TYPE 

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

class ReferenceSequenceRelated(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REFERENCESEQUENCERELATED_TYPE 

class Mechanism(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_MECHANISM_TYPE 

class Prediction(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_PREDICTION_TYPE 

class CriterionEvaluation(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CRITERIONEVALUATION_TYPE 

class AlleleFunctionalAssayMethod(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELEFUNCTIONALASSAYMETHOD_TYPE 

class ValueSetConceptListExtensibility(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_VALUESETCONCEPTLISTEXTENSIBILITY_TYPE 

class Phenotype(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_PHENOTYPE_TYPE 

class InconsistentSegregationObserved(DomainEntity):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INCONSISTENTSEGREGATIONOBSERVED_TYPE 

