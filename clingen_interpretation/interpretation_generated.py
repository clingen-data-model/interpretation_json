from interpretation_constants import *
from domain_entity_factory import get_factory_entity
from node import Node

class Contribution(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONTRIBUTION_TYPE 
    def set_agent(self,x):
        self.data[DMWG_A006_AGENT_KEY] = x
    def get_agent(self):
        return self.data[DMWG_A006_AGENT_KEY]
    def set_contributionDate(self,x):
        self.data[DMWG_A007_CONTRIBUTIONDATE_KEY] = x
    def get_contributionDate(self):
        return self.data[DMWG_A007_CONTRIBUTIONDATE_KEY]
    @get_factory_entity('SEPIO-CG:65120')
    def set_contributionRole(self,x):
        self.data[DMWG_A008_CONTRIBUTIONROLE_KEY] = x
    def get_contributionRole(self):
        return self.data[DMWG_A008_CONTRIBUTIONROLE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class Example(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_EXAMPLE_TYPE 
    def set_informationId(self,x):
        self.data[DMWG_A013_INFORMATIONID_KEY] = x
    def get_informationId(self):
        return self.data[DMWG_A013_INFORMATIONID_KEY]
    def set_searchTags(self,x):
        self.data[DMWG_A014_SEARCHTAGS_KEY] = x
    def get_searchTags(self):
        return self.data[DMWG_A014_SEARCHTAGS_KEY]
    def set_index(self,x):
        self.data[DMWG_A015_INDEX_KEY] = x
    def get_index(self):
        return self.data[DMWG_A015_INDEX_KEY]
    def set_author(self,x):
        self.data[DMWG_A035_AUTHOR_KEY] = x
    def get_author(self):
        return self.data[DMWG_A035_AUTHOR_KEY]
    def set_description(self,x):
        self.data[DMWG_A036_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_A036_DESCRIPTION_KEY]
    def set_image(self,x):
        self.data[DMWG_A037_IMAGE_KEY] = x
    def get_image(self):
        return self.data[DMWG_A037_IMAGE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class Agent(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_AGENT_TYPE 
    def set_description(self,x):
        self.data[DMWG_A148_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_A148_DESCRIPTION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class ValueSet(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_VALUESET_TYPE 
    def set_description(self,x):
        self.data[DMWG_A133_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_A133_DESCRIPTION_KEY]
    @get_factory_entity('SEPIO-CG:65101')
    def set_conceptListExtensibility(self,x):
        self.data[DMWG_A136_CONCEPTLISTEXTENSIBILITY_KEY] = x
    def get_conceptListExtensibility(self):
        return self.data[DMWG_A136_CONCEPTLISTEXTENSIBILITY_KEY]
    def add_sourceIdentifierSystems(self,x):
        if not DMWG_A145_SOURCEIDENTIFIERSYSTEMS_KEY in self.data:
            self.data[DMWG_A145_SOURCEIDENTIFIERSYSTEMS_KEY] = []
        self.data[DMWG_A145_SOURCEIDENTIFIERSYSTEMS_KEY].append( x ) 
    def get_sourceIdentifierSystems(self):
        return self.data[DMWG_A145_SOURCEIDENTIFIERSYSTEMS_KEY]
    def add_concept(self,x):
        if not DMWG_A121_CONCEPT_KEY in self.data:
            self.data[DMWG_A121_CONCEPT_KEY] = []
        self.data[DMWG_A121_CONCEPT_KEY].append( x ) 
    def get_concept(self):
        return self.data[DMWG_A121_CONCEPT_KEY]
    def set_conceptType(self,x):
        self.data[DMWG_A155_CONCEPTTYPE_KEY] = x
    def get_conceptType(self):
        return self.data[DMWG_A155_CONCEPTTYPE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class EvidenceLine(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_EVIDENCELINE_TYPE 
    def set_description(self,x):
        self.data[DMWG_A177_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_A177_DESCRIPTION_KEY]
    @get_factory_entity('SEPIO-CG:65116')
    def set_evidenceStrength(self,x):
        self.data[DMWG_A179_EVIDENCESTRENGTH_KEY] = x
    def get_evidenceStrength(self):
        return self.data[DMWG_A179_EVIDENCESTRENGTH_KEY]
    def add_evidenceItem(self,x):
        if not DMWG_A178_EVIDENCEITEM_KEY in self.data:
            self.data[DMWG_A178_EVIDENCEITEM_KEY] = []
        self.data[DMWG_A178_EVIDENCEITEM_KEY].append( x ) 
    def get_evidenceItem(self):
        return self.data[DMWG_A178_EVIDENCEITEM_KEY]
    def add_contribution(self,x):
        if not DMWG_A180_CONTRIBUTION_KEY in self.data:
            self.data[DMWG_A180_CONTRIBUTION_KEY] = []
        self.data[DMWG_A180_CONTRIBUTION_KEY].append( x ) 
    def get_contribution(self):
        return self.data[DMWG_A180_CONTRIBUTION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class Statement(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_STATEMENT_TYPE 
    def add_userLabel(self,x):
        if not DMWG_A073_USERLABEL_KEY in self.data:
            self.data[DMWG_A073_USERLABEL_KEY] = []
        self.data[DMWG_A073_USERLABEL_KEY].append( x ) 
    def get_userLabel(self):
        return self.data[DMWG_A073_USERLABEL_KEY]
    def set_qualifier(self,x):
        self.data[DMWG_A004_QUALIFIER_KEY] = x
    def get_qualifier(self):
        return self.data[DMWG_A004_QUALIFIER_KEY]
    def add_evidenceLine(self,x):
        if not DMWG_A055_EVIDENCELINE_KEY in self.data:
            self.data[DMWG_A055_EVIDENCELINE_KEY] = []
        self.data[DMWG_A055_EVIDENCELINE_KEY].append( x ) 
    def get_evidenceLine(self):
        return self.data[DMWG_A055_EVIDENCELINE_KEY]
    def set_description(self,x):
        self.data[DMWG_A120_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_A120_DESCRIPTION_KEY]
    def add_contribution(self,x):
        if not DMWG_A119_CONTRIBUTION_KEY in self.data:
            self.data[DMWG_A119_CONTRIBUTION_KEY] = []
        self.data[DMWG_A119_CONTRIBUTION_KEY].append( x ) 
    def get_contribution(self):
        return self.data[DMWG_A119_CONTRIBUTION_KEY]
    def add_source(self,x):
        if not DMWG_A127_SOURCE_KEY in self.data:
            self.data[DMWG_A127_SOURCE_KEY] = []
        self.data[DMWG_A127_SOURCE_KEY].append( x ) 
    def get_source(self):
        return self.data[DMWG_A127_SOURCE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class IndividualAlleleInheritance(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INDIVIDUALALLELEINHERITANCE_TYPE 
    def set_canonicalAllele(self,x):
        self.data[DMWG_A022_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_A022_CANONICALALLELE_KEY]
    def set_individual(self,x):
        self.data[DMWG_A023_INDIVIDUAL_KEY] = x
    def get_individual(self):
        return self.data[DMWG_A023_INDIVIDUAL_KEY]
    @get_factory_entity('SEPIO-CG:65121')
    def add_alleleInheritance(self,x):
        if not DMWG_A074_ALLELEINHERITANCE_KEY in self.data:
            self.data[DMWG_A074_ALLELEINHERITANCE_KEY] = []
        self.data[DMWG_A074_ALLELEINHERITANCE_KEY].append( x ) 
    def get_alleleInheritance(self):
        return self.data[DMWG_A074_ALLELEINHERITANCE_KEY]
    @get_factory_entity('SEPIO-CG:65125')
    def set_parentalConfirmation(self,x):
        self.data[DMWG_A025_PARENTALCONFIRMATION_KEY] = x
    def get_parentalConfirmation(self):
        return self.data[DMWG_A025_PARENTALCONFIRMATION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class FamilyCondition(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_FAMILYCONDITION_TYPE 
    def set_proband(self,x):
        self.data[DMWG_A019_PROBAND_KEY] = x
    def get_proband(self):
        return self.data[DMWG_A019_PROBAND_KEY]
    def add_condition(self,x):
        if not DMWG_A020_CONDITION_KEY in self.data:
            self.data[DMWG_A020_CONDITION_KEY] = []
        self.data[DMWG_A020_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_A020_CONDITION_KEY]
    @get_factory_entity('SEPIO-CG:65126')
    def set_familyHasCondition(self,x):
        self.data[DMWG_A021_FAMILYHASCONDITION_KEY] = x
    def get_familyHasCondition(self):
        return self.data[DMWG_A021_FAMILYHASCONDITION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class VariantInterpretation(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_VARIANTINTERPRETATION_TYPE 
    def set_variant(self,x):
        self.data[DMWG_A122_VARIANT_KEY] = x
    def get_variant(self):
        return self.data[DMWG_A122_VARIANT_KEY]
    def add_condition(self,x):
        if not DMWG_A123_CONDITION_KEY in self.data:
            self.data[DMWG_A123_CONDITION_KEY] = []
        self.data[DMWG_A123_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_A123_CONDITION_KEY]
    @get_factory_entity('SEPIO-CG:65103')
    def set_outcome(self,x):
        self.data[DMWG_A124_OUTCOME_KEY] = x
    def get_outcome(self):
        return self.data[DMWG_A124_OUTCOME_KEY]
    @get_factory_entity('SEPIO-CG:65132')
    def set_assertionMethod(self,x):
        self.data[DMWG_A125_ASSERTIONMETHOD_KEY] = x
    def get_assertionMethod(self):
        return self.data[DMWG_A125_ASSERTIONMETHOD_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class IndividualCondition(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INDIVIDUALCONDITION_TYPE 
    def set_individual(self,x):
        self.data[DMWG_A016_INDIVIDUAL_KEY] = x
    def get_individual(self):
        return self.data[DMWG_A016_INDIVIDUAL_KEY]
    def add_condition(self,x):
        if not DMWG_A017_CONDITION_KEY in self.data:
            self.data[DMWG_A017_CONDITION_KEY] = []
        self.data[DMWG_A017_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_A017_CONDITION_KEY]
    @get_factory_entity('SEPIO-CG:65126')
    def set_individualHasCondition(self,x):
        self.data[DMWG_A018_INDIVIDUALHASCONDITION_KEY] = x
    def get_individualHasCondition(self):
        return self.data[DMWG_A018_INDIVIDUALHASCONDITION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class LocusHeterogeneity(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_LOCUSHETEROGENEITY_TYPE 
    def set_condition(self,x):
        self.data[DMWG_A100_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[DMWG_A100_CONDITION_KEY]
    def set_gene(self,x):
        self.data[DMWG_A101_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_A101_GENE_KEY]
    @get_factory_entity('SEPIO-CG:65123')
    def set_specificity(self,x):
        self.data[DMWG_A102_SPECIFICITY_KEY] = x
    def get_specificity(self):
        return self.data[DMWG_A102_SPECIFICITY_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class AggregateSegregation(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_AGGREGATESEGREGATION_TYPE 
    def set_canonicalAllele(self,x):
        self.data[DMWG_A086_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_A086_CANONICALALLELE_KEY]
    def set_condition(self,x):
        self.data[DMWG_A087_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[DMWG_A087_CONDITION_KEY]
    def set_totalNumberOfSegregations(self,x):
        self.data[DMWG_A088_TOTALNUMBEROFSEGREGATIONS_KEY] = x
    def get_totalNumberOfSegregations(self):
        return self.data[DMWG_A088_TOTALNUMBEROFSEGREGATIONS_KEY]
    def add_familySegregation(self,x):
        if not DMWG_A089_FAMILYSEGREGATION_KEY in self.data:
            self.data[DMWG_A089_FAMILYSEGREGATION_KEY] = []
        self.data[DMWG_A089_FAMILYSEGREGATION_KEY].append( x ) 
    def get_familySegregation(self):
        return self.data[DMWG_A089_FAMILYSEGREGATION_KEY]
    @get_factory_entity('SEPIO-CG:65107')
    def set_modeOfInheritance(self,x):
        self.data[DMWG_A160_MODEOFINHERITANCE_KEY] = x
    def get_modeOfInheritance(self):
        return self.data[DMWG_A160_MODEOFINHERITANCE_KEY]
    def set_totalOfAllelePosConditionPosIndividuals(self,x):
        self.data[DMWG_A161_TOTALOFALLELEPOSCONDITIONPOSINDIVIDUALS_KEY] = x
    def get_totalOfAllelePosConditionPosIndividuals(self):
        return self.data[DMWG_A161_TOTALOFALLELEPOSCONDITIONPOSINDIVIDUALS_KEY]
    def set_totalOfAlleleNegConditionNegIndividuals(self,x):
        self.data[DMWG_A162_TOTALOFALLELENEGCONDITIONNEGINDIVIDUALS_KEY] = x
    def get_totalOfAlleleNegConditionNegIndividuals(self):
        return self.data[DMWG_A162_TOTALOFALLELENEGCONDITIONNEGINDIVIDUALS_KEY]
    def set_totalOfAllelePosConditionNegIndividuals(self,x):
        self.data[DMWG_A163_TOTALOFALLELEPOSCONDITIONNEGINDIVIDUALS_KEY] = x
    def get_totalOfAllelePosConditionNegIndividuals(self):
        return self.data[DMWG_A163_TOTALOFALLELEPOSCONDITIONNEGINDIVIDUALS_KEY]
    def set_totalOfAlleleNegConditionPosIndividuals(self,x):
        self.data[DMWG_A164_TOTALOFALLELENEGCONDITIONPOSINDIVIDUALS_KEY] = x
    def get_totalOfAlleleNegConditionPosIndividuals(self):
        return self.data[DMWG_A164_TOTALOFALLELENEGCONDITIONPOSINDIVIDUALS_KEY]
    def set_totalOfUntestedConditionPosIndividuals(self,x):
        self.data[DMWG_A165_TOTALOFUNTESTEDCONDITIONPOSINDIVIDUALS_KEY] = x
    def get_totalOfUntestedConditionPosIndividuals(self):
        return self.data[DMWG_A165_TOTALOFUNTESTEDCONDITIONPOSINDIVIDUALS_KEY]
    def set_totalOfUntestedConditionNegIndividuals(self,x):
        self.data[DMWG_A166_TOTALOFUNTESTEDCONDITIONNEGINDIVIDUALS_KEY] = x
    def get_totalOfUntestedConditionNegIndividuals(self):
        return self.data[DMWG_A166_TOTALOFUNTESTEDCONDITIONNEGINDIVIDUALS_KEY]
    def set_totalOfFamiliesWithInconsistentSegregations(self,x):
        self.data[DMWG_A167_TOTALOFFAMILIESWITHINCONSISTENTSEGREGATIONS_KEY] = x
    def get_totalOfFamiliesWithInconsistentSegregations(self):
        return self.data[DMWG_A167_TOTALOFFAMILIESWITHINCONSISTENTSEGREGATIONS_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class AlleleConservation(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELECONSERVATION_TYPE 
    def set_allele(self,x):
        self.data[DMWG_A111_ALLELE_KEY] = x
    def get_allele(self):
        return self.data[DMWG_A111_ALLELE_KEY]
    def set_conservationType(self,x):
        self.data[DMWG_A112_CONSERVATIONTYPE_KEY] = x
    def get_conservationType(self):
        return self.data[DMWG_A112_CONSERVATIONTYPE_KEY]
    def set_algorithm(self,x):
        self.data[DMWG_A113_ALGORITHM_KEY] = x
    def get_algorithm(self):
        return self.data[DMWG_A113_ALGORITHM_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class ConditionPenetrance(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONDITIONPENETRANCE_TYPE 
    def add_condition(self,x):
        if not DMWG_A107_CONDITION_KEY in self.data:
            self.data[DMWG_A107_CONDITION_KEY] = []
        self.data[DMWG_A107_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_A107_CONDITION_KEY]
    @get_factory_entity('SEPIO-CG:65114')
    def set_penetrance(self,x):
        self.data[DMWG_A108_PENETRANCE_KEY] = x
    def get_penetrance(self):
        return self.data[DMWG_A108_PENETRANCE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class AlleleConservationScore(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELECONSERVATIONSCORE_TYPE 
    def set_allele(self,x):
        self.data[DMWG_A185_ALLELE_KEY] = x
    def get_allele(self):
        return self.data[DMWG_A185_ALLELE_KEY]
    def set_conservationType(self,x):
        self.data[DMWG_A186_CONSERVATIONTYPE_KEY] = x
    def get_conservationType(self):
        return self.data[DMWG_A186_CONSERVATIONTYPE_KEY]
    def set_algorithm(self,x):
        self.data[DMWG_A187_ALGORITHM_KEY] = x
    def get_algorithm(self):
        return self.data[DMWG_A187_ALGORITHM_KEY]
    def set_score(self,x):
        self.data[DMWG_A114_SCORE_KEY] = x
    def get_score(self):
        return self.data[DMWG_A114_SCORE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class InSilicoPrediction(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INSILICOPREDICTION_TYPE 
    def set_canonicalAllele(self,x):
        self.data[DMWG_A096_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_A096_CANONICALALLELE_KEY]
    def set_transcript(self,x):
        self.data[DMWG_A034_TRANSCRIPT_KEY] = x
    def get_transcript(self):
        return self.data[DMWG_A034_TRANSCRIPT_KEY]
    @get_factory_entity('SEPIO-CG:65109')
    def set_predictionType(self,x):
        self.data[DMWG_A097_PREDICTIONTYPE_KEY] = x
    def get_predictionType(self):
        return self.data[DMWG_A097_PREDICTIONTYPE_KEY]
    def set_prediction(self,x):
        self.data[DMWG_A099_PREDICTION_KEY] = x
    def get_prediction(self):
        return self.data[DMWG_A099_PREDICTION_KEY]
    def set_algorithm(self,x):
        self.data[DMWG_A098_ALGORITHM_KEY] = x
    def get_algorithm(self):
        return self.data[DMWG_A098_ALGORITHM_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class CriterionAssessment(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CRITERIONASSESSMENT_TYPE 
    @get_factory_entity('SEPIO-CG:65131')
    def set_criterion(self,x):
        self.data[DMWG_A115_CRITERION_KEY] = x
    def get_criterion(self):
        return self.data[DMWG_A115_CRITERION_KEY]
    def set_variant(self,x):
        self.data[DMWG_A117_VARIANT_KEY] = x
    def get_variant(self):
        return self.data[DMWG_A117_VARIANT_KEY]
    def add_condition(self,x):
        if not DMWG_A118_CONDITION_KEY in self.data:
            self.data[DMWG_A118_CONDITION_KEY] = []
        self.data[DMWG_A118_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_A118_CONDITION_KEY]
    @get_factory_entity('SEPIO-CG:65110')
    def set_outcome(self,x):
        self.data[DMWG_A116_OUTCOME_KEY] = x
    def get_outcome(self):
        return self.data[DMWG_A116_OUTCOME_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class ConditionPrevelance(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONDITIONPREVELANCE_TYPE 
    def add_condition(self,x):
        if not DMWG_A103_CONDITION_KEY in self.data:
            self.data[DMWG_A103_CONDITION_KEY] = []
        self.data[DMWG_A103_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_A103_CONDITION_KEY]
    @get_factory_entity('SEPIO-CG:65112')
    def set_population(self,x):
        self.data[DMWG_A106_POPULATION_KEY] = x
    def get_population(self):
        return self.data[DMWG_A106_POPULATION_KEY]
    def set_minimum(self,x):
        self.data[DMWG_A104_MINIMUM_KEY] = x
    def get_minimum(self):
        return self.data[DMWG_A104_MINIMUM_KEY]
    def set_maximum(self,x):
        self.data[DMWG_A105_MAXIMUM_KEY] = x
    def get_maximum(self):
        return self.data[DMWG_A105_MAXIMUM_KEY]
    def set_prevelance(self,x):
        self.data[DMWG_A109_PREVELANCE_KEY] = x
    def get_prevelance(self):
        return self.data[DMWG_A109_PREVELANCE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class InSilicoPredictionScore(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INSILICOPREDICTIONSCORE_TYPE 
    def set_canonicalAllele(self,x):
        self.data[DMWG_A181_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_A181_CANONICALALLELE_KEY]
    def set_transcript(self,x):
        self.data[DMWG_A182_TRANSCRIPT_KEY] = x
    def get_transcript(self):
        return self.data[DMWG_A182_TRANSCRIPT_KEY]
    @get_factory_entity('SEPIO-CG:65109')
    def set_predictionType(self,x):
        self.data[DMWG_A183_PREDICTIONTYPE_KEY] = x
    def get_predictionType(self):
        return self.data[DMWG_A183_PREDICTIONTYPE_KEY]
    def set_prediction(self,x):
        self.data[DMWG_A095_PREDICTION_KEY] = x
    def get_prediction(self):
        return self.data[DMWG_A095_PREDICTION_KEY]
    def set_algorithm(self,x):
        self.data[DMWG_A184_ALGORITHM_KEY] = x
    def get_algorithm(self):
        return self.data[DMWG_A184_ALGORITHM_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class BenignMissenseVariationRate(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_BENIGNMISSENSEVARIATIONRATE_TYPE 
    def set_region(self,x):
        self.data[DMWG_A076_REGION_KEY] = x
    def get_region(self):
        return self.data[DMWG_A076_REGION_KEY]
    def set_gene(self,x):
        self.data[DMWG_A094_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_A094_GENE_KEY]
    @get_factory_entity('SEPIO-CG:65113')
    def set_value(self,x):
        self.data[DMWG_A080_VALUE_KEY] = x
    def get_value(self):
        return self.data[DMWG_A080_VALUE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class FamilySegregation(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_FAMILYSEGREGATION_TYPE 
    def set_canonicalAllele(self,x):
        self.data[DMWG_A082_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_A082_CANONICALALLELE_KEY]
    def set_condition(self,x):
        self.data[DMWG_A081_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[DMWG_A081_CONDITION_KEY]
    def set_family(self,x):
        self.data[DMWG_A083_FAMILY_KEY] = x
    def get_family(self):
        return self.data[DMWG_A083_FAMILY_KEY]
    def set_phenotypePositiveAllelePositive(self,x):
        self.data[DMWG_A084_PHENOTYPEPOSITIVEALLELEPOSITIVE_KEY] = x
    def get_phenotypePositiveAllelePositive(self):
        return self.data[DMWG_A084_PHENOTYPEPOSITIVEALLELEPOSITIVE_KEY]
    def set_phenotypePositiveAlleleNegative(self,x):
        self.data[DMWG_A050_PHENOTYPEPOSITIVEALLELENEGATIVE_KEY] = x
    def get_phenotypePositiveAlleleNegative(self):
        return self.data[DMWG_A050_PHENOTYPEPOSITIVEALLELENEGATIVE_KEY]
    def set_phenotypeNegativeAllelePositive(self,x):
        self.data[DMWG_A085_PHENOTYPENEGATIVEALLELEPOSITIVE_KEY] = x
    def get_phenotypeNegativeAllelePositive(self):
        return self.data[DMWG_A085_PHENOTYPENEGATIVEALLELEPOSITIVE_KEY]
    def set_phenotypeNegativeAlleleNegative(self,x):
        self.data[DMWG_A126_PHENOTYPENEGATIVEALLELENEGATIVE_KEY] = x
    def get_phenotypeNegativeAlleleNegative(self):
        return self.data[DMWG_A126_PHENOTYPENEGATIVEALLELENEGATIVE_KEY]
    def add_pedigree(self,x):
        if not DMWG_A093_PEDIGREE_KEY in self.data:
            self.data[DMWG_A093_PEDIGREE_KEY] = []
        self.data[DMWG_A093_PEDIGREE_KEY].append( x ) 
    def get_pedigree(self):
        return self.data[DMWG_A093_PEDIGREE_KEY]
    def add_columns(self,x):
        if not DMWG_A090_COLUMNS_KEY in self.data:
            self.data[DMWG_A090_COLUMNS_KEY] = []
        self.data[DMWG_A090_COLUMNS_KEY].append( x ) 
    def get_columns(self):
        return self.data[DMWG_A090_COLUMNS_KEY]
    def add_genotypeValues(self,x):
        if not DMWG_A092_GENOTYPEVALUES_KEY in self.data:
            self.data[DMWG_A092_GENOTYPEVALUES_KEY] = []
        self.data[DMWG_A092_GENOTYPEVALUES_KEY].append( x ) 
    def get_genotypeValues(self):
        return self.data[DMWG_A092_GENOTYPEVALUES_KEY]
    def add_affectedValues(self,x):
        if not DMWG_A091_AFFECTEDVALUES_KEY in self.data:
            self.data[DMWG_A091_AFFECTEDVALUES_KEY] = []
        self.data[DMWG_A091_AFFECTEDVALUES_KEY].append( x ) 
    def get_affectedValues(self):
        return self.data[DMWG_A091_AFFECTEDVALUES_KEY]
    @get_factory_entity('SEPIO-CG:65127')
    def set_inconsistentSegregationsObserved(self,x):
        self.data[DMWG_A110_INCONSISTENTSEGREGATIONSOBSERVED_KEY] = x
    def get_inconsistentSegregationsObserved(self):
        return self.data[DMWG_A110_INCONSISTENTSEGREGATIONSOBSERVED_KEY]
    def set_inconsistentSegregationCount(self,x):
        self.data[DMWG_A079_INCONSISTENTSEGREGATIONCOUNT_KEY] = x
    def get_inconsistentSegregationCount(self):
        return self.data[DMWG_A079_INCONSISTENTSEGREGATIONCOUNT_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class RegionType(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REGIONTYPE_TYPE 
    def set_region(self,x):
        self.data[DMWG_A063_REGION_KEY] = x
    def get_region(self):
        return self.data[DMWG_A063_REGION_KEY]
    @get_factory_entity('SEPIO-CG:65104')
    def add_annotation(self,x):
        if not DMWG_A057_ANNOTATION_KEY in self.data:
            self.data[DMWG_A057_ANNOTATION_KEY] = []
        self.data[DMWG_A057_ANNOTATION_KEY].append( x ) 
    def get_annotation(self):
        return self.data[DMWG_A057_ANNOTATION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class RegionAlleles(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REGIONALLELES_TYPE 
    def set_region(self,x):
        self.data[DMWG_A071_REGION_KEY] = x
    def get_region(self):
        return self.data[DMWG_A071_REGION_KEY]
    def add_allele(self,x):
        if not DMWG_A058_ALLELE_KEY in self.data:
            self.data[DMWG_A058_ALLELE_KEY] = []
        self.data[DMWG_A058_ALLELE_KEY].append( x ) 
    def get_allele(self):
        return self.data[DMWG_A058_ALLELE_KEY]
    @get_factory_entity('SEPIO-CG:65129')
    def set_outcome(self,x):
        self.data[DMWG_A059_OUTCOME_KEY] = x
    def get_outcome(self):
        return self.data[DMWG_A059_OUTCOME_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class AlleleFunctionalImpact(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELEFUNCTIONALIMPACT_TYPE 
    def set_contextualAllele(self,x):
        self.data[DMWG_A028_CONTEXTUALALLELE_KEY] = x
    def get_contextualAllele(self):
        return self.data[DMWG_A028_CONTEXTUALALLELE_KEY]
    def set_gene(self,x):
        self.data[DMWG_A029_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_A029_GENE_KEY]
    def set_resultDescription(self,x):
        self.data[DMWG_A026_RESULTDESCRIPTION_KEY] = x
    def get_resultDescription(self):
        return self.data[DMWG_A026_RESULTDESCRIPTION_KEY]
    @get_factory_entity('SEPIO-CG:65111')
    def set_assayType(self,x):
        self.data[DMWG_A027_ASSAYTYPE_KEY] = x
    def get_assayType(self):
        return self.data[DMWG_A027_ASSAYTYPE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class CaseControl(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CASECONTROL_TYPE 
    def set_canonicalAllele(self,x):
        self.data[DMWG_A038_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_A038_CANONICALALLELE_KEY]
    def set_condition(self,x):
        self.data[DMWG_A039_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[DMWG_A039_CONDITION_KEY]
    def set_caseGroupFrequency(self,x):
        self.data[DMWG_A042_CASEGROUPFREQUENCY_KEY] = x
    def get_caseGroupFrequency(self):
        return self.data[DMWG_A042_CASEGROUPFREQUENCY_KEY]
    def set_controlGroupFrequency(self,x):
        self.data[DMWG_A043_CONTROLGROUPFREQUENCY_KEY] = x
    def get_controlGroupFrequency(self):
        return self.data[DMWG_A043_CONTROLGROUPFREQUENCY_KEY]
    def set_oddsRatio(self,x):
        self.data[DMWG_A040_ODDSRATIO_KEY] = x
    def get_oddsRatio(self):
        return self.data[DMWG_A040_ODDSRATIO_KEY]
    def set_confidenceLevel(self,x):
        self.data[DMWG_A041_CONFIDENCELEVEL_KEY] = x
    def get_confidenceLevel(self):
        return self.data[DMWG_A041_CONFIDENCELEVEL_KEY]
    def set_confidenceIntervalLower(self,x):
        self.data[DMWG_A048_CONFIDENCEINTERVALLOWER_KEY] = x
    def get_confidenceIntervalLower(self):
        return self.data[DMWG_A048_CONFIDENCEINTERVALLOWER_KEY]
    def set_confidenceIntervalUpper(self,x):
        self.data[DMWG_A049_CONFIDENCEINTERVALUPPER_KEY] = x
    def get_confidenceIntervalUpper(self):
        return self.data[DMWG_A049_CONFIDENCEINTERVALUPPER_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class NullAllele(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_NULLALLELE_TYPE 
    def set_contextualAllele(self,x):
        self.data[DMWG_A077_CONTEXTUALALLELE_KEY] = x
    def get_contextualAllele(self):
        return self.data[DMWG_A077_CONTEXTUALALLELE_KEY]
    @get_factory_entity('SEPIO-CG:65128')
    def set_annotation(self,x):
        self.data[DMWG_A078_ANNOTATION_KEY] = x
    def get_annotation(self):
        return self.data[DMWG_A078_ANNOTATION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class AlleleFrequency(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELEFREQUENCY_TYPE 
    def set_allele(self,x):
        self.data[DMWG_A031_ALLELE_KEY] = x
    def get_allele(self):
        return self.data[DMWG_A031_ALLELE_KEY]
    @get_factory_entity('SEPIO-CG:65112')
    def set_population(self,x):
        self.data[DMWG_A047_POPULATION_KEY] = x
    def get_population(self):
        return self.data[DMWG_A047_POPULATION_KEY]
    @get_factory_entity('SEPIO-CG:65122')
    def set_ascertainment(self,x):
        self.data[DMWG_A030_ASCERTAINMENT_KEY] = x
    def get_ascertainment(self):
        return self.data[DMWG_A030_ASCERTAINMENT_KEY]
    def set_alleleFrequency(self,x):
        self.data[DMWG_A060_ALLELEFREQUENCY_KEY] = x
    def get_alleleFrequency(self):
        return self.data[DMWG_A060_ALLELEFREQUENCY_KEY]
    def set_alleleCount(self,x):
        self.data[DMWG_A032_ALLELECOUNT_KEY] = x
    def get_alleleCount(self):
        return self.data[DMWG_A032_ALLELECOUNT_KEY]
    def set_alleleNumber(self,x):
        self.data[DMWG_A033_ALLELENUMBER_KEY] = x
    def get_alleleNumber(self):
        return self.data[DMWG_A033_ALLELENUMBER_KEY]
    def set_individualCount(self,x):
        self.data[DMWG_A044_INDIVIDUALCOUNT_KEY] = x
    def get_individualCount(self):
        return self.data[DMWG_A044_INDIVIDUALCOUNT_KEY]
    def set_homozygousAlleleIndividualCount(self,x):
        self.data[DMWG_A045_HOMOZYGOUSALLELEINDIVIDUALCOUNT_KEY] = x
    def get_homozygousAlleleIndividualCount(self):
        return self.data[DMWG_A045_HOMOZYGOUSALLELEINDIVIDUALCOUNT_KEY]
    def set_heterozygousAlleleIndividualCount(self,x):
        self.data[DMWG_A046_HETEROZYGOUSALLELEINDIVIDUALCOUNT_KEY] = x
    def get_heterozygousAlleleIndividualCount(self):
        return self.data[DMWG_A046_HETEROZYGOUSALLELEINDIVIDUALCOUNT_KEY]
    def set_hemizygousAlleleIndividualCount(self,x):
        self.data[DMWG_A051_HEMIZYGOUSALLELEINDIVIDUALCOUNT_KEY] = x
    def get_hemizygousAlleleIndividualCount(self):
        return self.data[DMWG_A051_HEMIZYGOUSALLELEINDIVIDUALCOUNT_KEY]
    def set_medianCoverage(self,x):
        self.data[DMWG_A062_MEDIANCOVERAGE_KEY] = x
    def get_medianCoverage(self):
        return self.data[DMWG_A062_MEDIANCOVERAGE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class IndividualGenotype(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INDIVIDUALGENOTYPE_TYPE 
    def set_individual(self,x):
        self.data[DMWG_A065_INDIVIDUAL_KEY] = x
    def get_individual(self):
        return self.data[DMWG_A065_INDIVIDUAL_KEY]
    def add_genotype(self,x):
        if not DMWG_A066_GENOTYPE_KEY in self.data:
            self.data[DMWG_A066_GENOTYPE_KEY] = []
        self.data[DMWG_A066_GENOTYPE_KEY].append( x ) 
    def get_genotype(self):
        return self.data[DMWG_A066_GENOTYPE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class AlleleMolecularConsequence(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELEMOLECULARCONSEQUENCE_TYPE 
    def set_contextualAllele(self,x):
        self.data[DMWG_A009_CONTEXTUALALLELE_KEY] = x
    def get_contextualAllele(self):
        return self.data[DMWG_A009_CONTEXTUALALLELE_KEY]
    @get_factory_entity('SEPIO-CG:65102')
    def set_consequence(self,x):
        self.data[DMWG_A001_CONSEQUENCE_KEY] = x
    def get_consequence(self):
        return self.data[DMWG_A001_CONSEQUENCE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class ConditionMechanism(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONDITIONMECHANISM_TYPE 
    def set_condition(self,x):
        self.data[DMWG_A012_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[DMWG_A012_CONDITION_KEY]
    def set_gene(self,x):
        self.data[DMWG_A011_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_A011_GENE_KEY]
    @get_factory_entity('SEPIO-CG:65108')
    def set_mechanism(self,x):
        self.data[DMWG_A002_MECHANISM_KEY] = x
    def get_mechanism(self):
        return self.data[DMWG_A002_MECHANISM_KEY]
    @get_factory_entity('SEPIO-CG:65115')
    def set_mechanismConfidence(self,x):
        self.data[DMWG_A003_MECHANISMCONFIDENCE_KEY] = x
    def get_mechanismConfidence(self):
        return self.data[DMWG_A003_MECHANISMCONFIDENCE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class UserLabel(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_USERLABEL_TYPE 
    def set_labelFor(self,x):
        self.data[DMWG_A130_LABELFOR_KEY] = x
    def get_labelFor(self):
        return self.data[DMWG_A130_LABELFOR_KEY]
    def set_description(self,x):
        self.data[DMWG_A134_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_A134_DESCRIPTION_KEY]
    def add_contribution(self,x):
        if not DMWG_A131_CONTRIBUTION_KEY in self.data:
            self.data[DMWG_A131_CONTRIBUTION_KEY] = []
        self.data[DMWG_A131_CONTRIBUTION_KEY].append( x ) 
    def get_contribution(self):
        return self.data[DMWG_A131_CONTRIBUTION_KEY]
    def set_comments(self,x):
        self.data[DMWG_A150_COMMENTS_KEY] = x
    def get_comments(self):
        return self.data[DMWG_A150_COMMENTS_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

