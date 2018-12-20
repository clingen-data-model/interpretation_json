from clingen_interpretation.interpretation_constants import *
from clingen_interpretation.domain_entity_factory import get_factory_entity
from clingen_interpretation.node import Node

class Entity(Node):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_ENTITY 
    def set_label(self,x):
        self.data[PROP_A200_LABEL_KEY] = x
    def get_label(self):
        return self.data[PROP_A200_LABEL_KEY]
    def set_description(self,x):
        self.data[PROP_A201_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[PROP_A201_DESCRIPTION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class Statement(Entity):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_STATEMENT 
    def add_userLabelDictionary(self,x):
        if not PROP_A073_USERLABELDICTIONARY_KEY in self.data:
            self.data[PROP_A073_USERLABELDICTIONARY_KEY] = []
        self.data[PROP_A073_USERLABELDICTIONARY_KEY].append( x ) 
    def get_userLabelDictionary(self):
        return self.data[PROP_A073_USERLABELDICTIONARY_KEY]
    def set_outcomeQualifier(self,x):
        self.data[PROP_A004_OUTCOMEQUALIFIER_KEY] = x
    def get_outcomeQualifier(self):
        return self.data[PROP_A004_OUTCOMEQUALIFIER_KEY]
    def add_evidenceLine(self,x):
        if not PROP_A055_EVIDENCELINE_KEY in self.data:
            self.data[PROP_A055_EVIDENCELINE_KEY] = []
        self.data[PROP_A055_EVIDENCELINE_KEY].append( x ) 
    def get_evidenceLine(self):
        return self.data[PROP_A055_EVIDENCELINE_KEY]
    def add_contribution(self,x):
        if not PROP_A119_CONTRIBUTION_KEY in self.data:
            self.data[PROP_A119_CONTRIBUTION_KEY] = []
        self.data[PROP_A119_CONTRIBUTION_KEY].append( x ) 
    def get_contribution(self):
        return self.data[PROP_A119_CONTRIBUTION_KEY]
    def add_source(self,x):
        if not PROP_A127_SOURCE_KEY in self.data:
            self.data[PROP_A127_SOURCE_KEY] = []
        self.data[PROP_A127_SOURCE_KEY].append( x ) 
    def get_source(self):
        return self.data[PROP_A127_SOURCE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class VariantPathogenicityInterpretation(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_VARIANTPATHOGENICITYINTERPRETATION 
    def set_variant(self,x):
        self.data[PROP_A122_VARIANT_KEY] = x
    def get_variant(self):
        return self.data[PROP_A122_VARIANT_KEY]
    @get_factory_entity('SEPIO:0000371')
    def set_statementOutcome(self,x):
        self.data[PROP_A124_STATEMENTOUTCOME_KEY] = x
    def get_statementOutcome(self):
        return self.data[PROP_A124_STATEMENTOUTCOME_KEY]
    def add_condition(self,x):
        if not PROP_A123_CONDITION_KEY in self.data:
            self.data[PROP_A123_CONDITION_KEY] = []
        self.data[PROP_A123_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[PROP_A123_CONDITION_KEY]
    @get_factory_entity('SEPIO-CG:65132')
    def set_assertionMethod(self,x):
        self.data[PROP_A125_ASSERTIONMETHOD_KEY] = x
    def get_assertionMethod(self):
        return self.data[PROP_A125_ASSERTIONMETHOD_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class CriterionAssessment(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_CRITERIONASSESSMENT 
    @get_factory_entity('SEPIO:0000395')
    def set_criterion(self,x):
        self.data[PROP_A115_CRITERION_KEY] = x
    def get_criterion(self):
        return self.data[PROP_A115_CRITERION_KEY]
    def set_variant(self,x):
        self.data[PROP_A117_VARIANT_KEY] = x
    def get_variant(self):
        return self.data[PROP_A117_VARIANT_KEY]
    @get_factory_entity('SEPIO:0000347')
    def set_statementOutcome(self,x):
        self.data[PROP_A116_STATEMENTOUTCOME_KEY] = x
    def get_statementOutcome(self):
        return self.data[PROP_A116_STATEMENTOUTCOME_KEY]
    def add_condition(self,x):
        if not PROP_A118_CONDITION_KEY in self.data:
            self.data[PROP_A118_CONDITION_KEY] = []
        self.data[PROP_A118_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[PROP_A118_CONDITION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class AggregateCosegregationStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_AGGREGATECOSEGREGATIONSTATEMENT 
    def set_canonicalAllele(self,x):
        self.data[PROP_A086_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[PROP_A086_CANONICALALLELE_KEY]
    def set_condition(self,x):
        self.data[PROP_A087_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[PROP_A087_CONDITION_KEY]
    @get_factory_entity('SEPIO:0000416')
    def set_inheritancePatternParameter(self,x):
        self.data[PROP_A160_INHERITANCEPATTERNPARAMETER_KEY] = x
    def get_inheritancePatternParameter(self):
        return self.data[PROP_A160_INHERITANCEPATTERNPARAMETER_KEY]
    def add_familySegregation(self,x):
        if not PROP_A089_FAMILYSEGREGATION_KEY in self.data:
            self.data[PROP_A089_FAMILYSEGREGATION_KEY] = []
        self.data[PROP_A089_FAMILYSEGREGATION_KEY].append( x ) 
    def get_familySegregation(self):
        return self.data[PROP_A089_FAMILYSEGREGATION_KEY]
    def set_totalNumberOfSegregations(self,x):
        self.data[PROP_A088_TOTALNUMBEROFSEGREGATIONS_KEY] = x
    def get_totalNumberOfSegregations(self):
        return self.data[PROP_A088_TOTALNUMBEROFSEGREGATIONS_KEY]
    def set_totalOfAllelePosConditionPosIndividuals(self,x):
        self.data[PROP_A161_TOTALOFALLELEPOSCONDITIONPOSINDIVIDUALS_KEY] = x
    def get_totalOfAllelePosConditionPosIndividuals(self):
        return self.data[PROP_A161_TOTALOFALLELEPOSCONDITIONPOSINDIVIDUALS_KEY]
    def set_totalOfAlleleNegConditionNegIndividuals(self,x):
        self.data[PROP_A162_TOTALOFALLELENEGCONDITIONNEGINDIVIDUALS_KEY] = x
    def get_totalOfAlleleNegConditionNegIndividuals(self):
        return self.data[PROP_A162_TOTALOFALLELENEGCONDITIONNEGINDIVIDUALS_KEY]
    def set_totalOfAllelePosConditionNegIndividuals(self,x):
        self.data[PROP_A163_TOTALOFALLELEPOSCONDITIONNEGINDIVIDUALS_KEY] = x
    def get_totalOfAllelePosConditionNegIndividuals(self):
        return self.data[PROP_A163_TOTALOFALLELEPOSCONDITIONNEGINDIVIDUALS_KEY]
    def set_totalOfAlleleNegConditionPosIndividuals(self,x):
        self.data[PROP_A164_TOTALOFALLELENEGCONDITIONPOSINDIVIDUALS_KEY] = x
    def get_totalOfAlleleNegConditionPosIndividuals(self):
        return self.data[PROP_A164_TOTALOFALLELENEGCONDITIONPOSINDIVIDUALS_KEY]
    def set_totalOfUntestedConditionPosIndividuals(self,x):
        self.data[PROP_A165_TOTALOFUNTESTEDCONDITIONPOSINDIVIDUALS_KEY] = x
    def get_totalOfUntestedConditionPosIndividuals(self):
        return self.data[PROP_A165_TOTALOFUNTESTEDCONDITIONPOSINDIVIDUALS_KEY]
    def set_totalOfUntestedConditionNegIndividuals(self,x):
        self.data[PROP_A166_TOTALOFUNTESTEDCONDITIONNEGINDIVIDUALS_KEY] = x
    def get_totalOfUntestedConditionNegIndividuals(self):
        return self.data[PROP_A166_TOTALOFUNTESTEDCONDITIONNEGINDIVIDUALS_KEY]
    def set_totalOfFamiliesWithInconsistentSegregations(self,x):
        self.data[PROP_A167_TOTALOFFAMILIESWITHINCONSISTENTSEGREGATIONS_KEY] = x
    def get_totalOfFamiliesWithInconsistentSegregations(self):
        return self.data[PROP_A167_TOTALOFFAMILIESWITHINCONSISTENTSEGREGATIONS_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class AlleleConservationScoreStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_ALLELECONSERVATIONSCORESTATEMENT 
    def set_allele(self,x):
        self.data[PROP_A185_ALLELE_KEY] = x
    def get_allele(self):
        return self.data[PROP_A185_ALLELE_KEY]
    def set_score(self,x):
        self.data[PROP_A114_SCORE_KEY] = x
    def get_score(self):
        return self.data[PROP_A114_SCORE_KEY]
    def set_algorithm(self,x):
        self.data[PROP_A187_ALGORITHM_KEY] = x
    def get_algorithm(self):
        return self.data[PROP_A187_ALGORITHM_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class AlleleConservationStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_ALLELECONSERVATIONSTATEMENT 
    def set_allele(self,x):
        self.data[PROP_A111_ALLELE_KEY] = x
    def get_allele(self):
        return self.data[PROP_A111_ALLELE_KEY]
    @get_factory_entity('SEPIO-CG:65124')
    def set_statementOutcome(self,x):
        self.data[PROP_A112_STATEMENTOUTCOME_KEY] = x
    def get_statementOutcome(self):
        return self.data[PROP_A112_STATEMENTOUTCOME_KEY]
    def set_algorithm(self,x):
        self.data[PROP_A113_ALGORITHM_KEY] = x
    def get_algorithm(self):
        return self.data[PROP_A113_ALGORITHM_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class AlleleFunctionalImpactStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_ALLELEFUNCTIONALIMPACTSTATEMENT 
    def set_contextualAllele(self,x):
        self.data[PROP_A028_CONTEXTUALALLELE_KEY] = x
    def get_contextualAllele(self):
        return self.data[PROP_A028_CONTEXTUALALLELE_KEY]
    @get_factory_entity('SEPIO:0000396')
    def set_gene(self,x):
        self.data[PROP_A029_GENE_KEY] = x
    def get_gene(self):
        return self.data[PROP_A029_GENE_KEY]
    def set_resultDescription(self,x):
        self.data[PROP_A026_RESULTDESCRIPTION_KEY] = x
    def get_resultDescription(self):
        return self.data[PROP_A026_RESULTDESCRIPTION_KEY]
    @get_factory_entity('SEPIO:0000382')
    def set_assayType(self,x):
        self.data[PROP_A027_ASSAYTYPE_KEY] = x
    def get_assayType(self):
        return self.data[PROP_A027_ASSAYTYPE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class AlleleMolecularConsequenceStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_ALLELEMOLECULARCONSEQUENCESTATEMENT 
    def set_contextualAllele(self,x):
        self.data[PROP_A009_CONTEXTUALALLELE_KEY] = x
    def get_contextualAllele(self):
        return self.data[PROP_A009_CONTEXTUALALLELE_KEY]
    @get_factory_entity('SEPIO:0000380')
    def set_statementOutcome(self,x):
        self.data[PROP_A001_STATEMENTOUTCOME_KEY] = x
    def get_statementOutcome(self):
        return self.data[PROP_A001_STATEMENTOUTCOME_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class CaseControlAlleleFrequencyStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_CASECONTROLALLELEFREQUENCYSTATEMENT 
    def set_canonicalAllele(self,x):
        self.data[PROP_A038_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[PROP_A038_CANONICALALLELE_KEY]
    def set_condition(self,x):
        self.data[PROP_A039_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[PROP_A039_CONDITION_KEY]
    def set_caseGroupFrequency(self,x):
        self.data[PROP_A042_CASEGROUPFREQUENCY_KEY] = x
    def get_caseGroupFrequency(self):
        return self.data[PROP_A042_CASEGROUPFREQUENCY_KEY]
    def set_controlGroupFrequency(self,x):
        self.data[PROP_A043_CONTROLGROUPFREQUENCY_KEY] = x
    def get_controlGroupFrequency(self):
        return self.data[PROP_A043_CONTROLGROUPFREQUENCY_KEY]
    def set_oddsRatio(self,x):
        self.data[PROP_A040_ODDSRATIO_KEY] = x
    def get_oddsRatio(self):
        return self.data[PROP_A040_ODDSRATIO_KEY]
    def set_confidenceLevel(self,x):
        self.data[PROP_A041_CONFIDENCELEVEL_KEY] = x
    def get_confidenceLevel(self):
        return self.data[PROP_A041_CONFIDENCELEVEL_KEY]
    def set_confidenceIntervalLower(self,x):
        self.data[PROP_A048_CONFIDENCEINTERVALLOWER_KEY] = x
    def get_confidenceIntervalLower(self):
        return self.data[PROP_A048_CONFIDENCEINTERVALLOWER_KEY]
    def set_confidenceIntervalUpper(self,x):
        self.data[PROP_A049_CONFIDENCEINTERVALUPPER_KEY] = x
    def get_confidenceIntervalUpper(self):
        return self.data[PROP_A049_CONFIDENCEINTERVALUPPER_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class FamilyCosegregationStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_FAMILYCOSEGREGATIONSTATEMENT 
    def set_canonicalAllele(self,x):
        self.data[PROP_A082_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[PROP_A082_CANONICALALLELE_KEY]
    def set_condition(self,x):
        self.data[PROP_A081_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[PROP_A081_CONDITION_KEY]
    def set_family(self,x):
        self.data[PROP_A083_FAMILY_KEY] = x
    def get_family(self):
        return self.data[PROP_A083_FAMILY_KEY]
    def set_phenotypePositiveAllelePositive(self,x):
        self.data[PROP_A084_PHENOTYPEPOSITIVEALLELEPOSITIVE_KEY] = x
    def get_phenotypePositiveAllelePositive(self):
        return self.data[PROP_A084_PHENOTYPEPOSITIVEALLELEPOSITIVE_KEY]
    def set_phenotypePositiveAlleleNegative(self,x):
        self.data[PROP_A050_PHENOTYPEPOSITIVEALLELENEGATIVE_KEY] = x
    def get_phenotypePositiveAlleleNegative(self):
        return self.data[PROP_A050_PHENOTYPEPOSITIVEALLELENEGATIVE_KEY]
    def set_phenotypeNegativeAllelePositive(self,x):
        self.data[PROP_A085_PHENOTYPENEGATIVEALLELEPOSITIVE_KEY] = x
    def get_phenotypeNegativeAllelePositive(self):
        return self.data[PROP_A085_PHENOTYPENEGATIVEALLELEPOSITIVE_KEY]
    def set_phenotypeNegativeAlleleNegative(self,x):
        self.data[PROP_A126_PHENOTYPENEGATIVEALLELENEGATIVE_KEY] = x
    def get_phenotypeNegativeAlleleNegative(self):
        return self.data[PROP_A126_PHENOTYPENEGATIVEALLELENEGATIVE_KEY]
    @get_factory_entity('SEPIO-CG:65127')
    def set_inconsistentSegregationsObserved(self,x):
        self.data[PROP_A110_INCONSISTENTSEGREGATIONSOBSERVED_KEY] = x
    def get_inconsistentSegregationsObserved(self):
        return self.data[PROP_A110_INCONSISTENTSEGREGATIONSOBSERVED_KEY]
    def set_inconsistentSegregationCount(self,x):
        self.data[PROP_A079_INCONSISTENTSEGREGATIONCOUNT_KEY] = x
    def get_inconsistentSegregationCount(self):
        return self.data[PROP_A079_INCONSISTENTSEGREGATIONCOUNT_KEY]
    def add_columns(self,x):
        if not PROP_A090_COLUMNS_KEY in self.data:
            self.data[PROP_A090_COLUMNS_KEY] = []
        self.data[PROP_A090_COLUMNS_KEY].append( x ) 
    def get_columns(self):
        return self.data[PROP_A090_COLUMNS_KEY]
    def add_pedigree(self,x):
        if not PROP_A093_PEDIGREE_KEY in self.data:
            self.data[PROP_A093_PEDIGREE_KEY] = []
        self.data[PROP_A093_PEDIGREE_KEY].append( x ) 
    def get_pedigree(self):
        return self.data[PROP_A093_PEDIGREE_KEY]
    def add_genotypeValues(self,x):
        if not PROP_A092_GENOTYPEVALUES_KEY in self.data:
            self.data[PROP_A092_GENOTYPEVALUES_KEY] = []
        self.data[PROP_A092_GENOTYPEVALUES_KEY].append( x ) 
    def get_genotypeValues(self):
        return self.data[PROP_A092_GENOTYPEVALUES_KEY]
    def add_affectedValues(self,x):
        if not PROP_A091_AFFECTEDVALUES_KEY in self.data:
            self.data[PROP_A091_AFFECTEDVALUES_KEY] = []
        self.data[PROP_A091_AFFECTEDVALUES_KEY].append( x ) 
    def get_affectedValues(self):
        return self.data[PROP_A091_AFFECTEDVALUES_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class InSilicoPredictionScoreStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_INSILICOPREDICTIONSCORESTATEMENT 
    def set_canonicalAllele(self,x):
        self.data[PROP_A181_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[PROP_A181_CANONICALALLELE_KEY]
    @get_factory_entity('SEPIO-CG:65119')
    def set_transcript(self,x):
        self.data[PROP_A182_TRANSCRIPT_KEY] = x
    def get_transcript(self):
        return self.data[PROP_A182_TRANSCRIPT_KEY]
    def set_prediction(self,x):
        self.data[PROP_A095_PREDICTION_KEY] = x
    def get_prediction(self):
        return self.data[PROP_A095_PREDICTION_KEY]
    @get_factory_entity('SEPIO:0000345')
    def set_predictionType(self,x):
        self.data[PROP_A183_PREDICTIONTYPE_KEY] = x
    def get_predictionType(self):
        return self.data[PROP_A183_PREDICTIONTYPE_KEY]
    def set_algorithm(self,x):
        self.data[PROP_A184_ALGORITHM_KEY] = x
    def get_algorithm(self):
        return self.data[PROP_A184_ALGORITHM_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class InSilicoPredictionStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_INSILICOPREDICTIONSTATEMENT 
    def set_canonicalAllele(self,x):
        self.data[PROP_A096_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[PROP_A096_CANONICALALLELE_KEY]
    @get_factory_entity('SEPIO-CG:65119')
    def set_transcript(self,x):
        self.data[PROP_A034_TRANSCRIPT_KEY] = x
    def get_transcript(self):
        return self.data[PROP_A034_TRANSCRIPT_KEY]
    def set_statementOutcome(self,x):
        self.data[PROP_A099_STATEMENTOUTCOME_KEY] = x
    def get_statementOutcome(self):
        return self.data[PROP_A099_STATEMENTOUTCOME_KEY]
    @get_factory_entity('SEPIO:0000345')
    def set_predictionType(self,x):
        self.data[PROP_A097_PREDICTIONTYPE_KEY] = x
    def get_predictionType(self):
        return self.data[PROP_A097_PREDICTIONTYPE_KEY]
    def set_algorithm(self,x):
        self.data[PROP_A098_ALGORITHM_KEY] = x
    def get_algorithm(self):
        return self.data[PROP_A098_ALGORITHM_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class NullAlleleStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_NULLALLELESTATEMENT 
    def set_contextualAllele(self,x):
        self.data[PROP_A077_CONTEXTUALALLELE_KEY] = x
    def get_contextualAllele(self):
        return self.data[PROP_A077_CONTEXTUALALLELE_KEY]
    @get_factory_entity('SEPIO-CG:65128')
    def set_statementOutcome(self,x):
        self.data[PROP_A078_STATEMENTOUTCOME_KEY] = x
    def get_statementOutcome(self):
        return self.data[PROP_A078_STATEMENTOUTCOME_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class PopulationAlleleFrequencyStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_POPULATIONALLELEFREQUENCYSTATEMENT 
    def set_allele(self,x):
        self.data[PROP_A031_ALLELE_KEY] = x
    def get_allele(self):
        return self.data[PROP_A031_ALLELE_KEY]
    def set_alleleFrequency(self,x):
        self.data[PROP_A060_ALLELEFREQUENCY_KEY] = x
    def get_alleleFrequency(self):
        return self.data[PROP_A060_ALLELEFREQUENCY_KEY]
    @get_factory_entity('SEPIO-CG:65112')
    def set_population(self,x):
        self.data[PROP_A047_POPULATION_KEY] = x
    def get_population(self):
        return self.data[PROP_A047_POPULATION_KEY]
    def set_alleleCount(self,x):
        self.data[PROP_A032_ALLELECOUNT_KEY] = x
    def get_alleleCount(self):
        return self.data[PROP_A032_ALLELECOUNT_KEY]
    def set_alleleNumber(self,x):
        self.data[PROP_A033_ALLELENUMBER_KEY] = x
    def get_alleleNumber(self):
        return self.data[PROP_A033_ALLELENUMBER_KEY]
    def set_individualCount(self,x):
        self.data[PROP_A044_INDIVIDUALCOUNT_KEY] = x
    def get_individualCount(self):
        return self.data[PROP_A044_INDIVIDUALCOUNT_KEY]
    def set_homozygousAlleleIndividualCount(self,x):
        self.data[PROP_A045_HOMOZYGOUSALLELEINDIVIDUALCOUNT_KEY] = x
    def get_homozygousAlleleIndividualCount(self):
        return self.data[PROP_A045_HOMOZYGOUSALLELEINDIVIDUALCOUNT_KEY]
    def set_heterozygousAlleleIndividualCount(self,x):
        self.data[PROP_A046_HETEROZYGOUSALLELEINDIVIDUALCOUNT_KEY] = x
    def get_heterozygousAlleleIndividualCount(self):
        return self.data[PROP_A046_HETEROZYGOUSALLELEINDIVIDUALCOUNT_KEY]
    def set_hemizygousAlleleIndividualCount(self,x):
        self.data[PROP_A051_HEMIZYGOUSALLELEINDIVIDUALCOUNT_KEY] = x
    def get_hemizygousAlleleIndividualCount(self):
        return self.data[PROP_A051_HEMIZYGOUSALLELEINDIVIDUALCOUNT_KEY]
    def set_medianCoverage(self,x):
        self.data[PROP_A062_MEDIANCOVERAGE_KEY] = x
    def get_medianCoverage(self):
        return self.data[PROP_A062_MEDIANCOVERAGE_KEY]
    @get_factory_entity('SEPIO:0000409')
    def set_ascertainment(self,x):
        self.data[PROP_A030_ASCERTAINMENT_KEY] = x
    def get_ascertainment(self):
        return self.data[PROP_A030_ASCERTAINMENT_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class RegionAllelesStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_REGIONALLELESSTATEMENT 
    def add_allele(self,x):
        if not PROP_A058_ALLELE_KEY in self.data:
            self.data[PROP_A058_ALLELE_KEY] = []
        self.data[PROP_A058_ALLELE_KEY].append( x ) 
    def get_allele(self):
        return self.data[PROP_A058_ALLELE_KEY]
    @get_factory_entity('SEPIO-CG:65129')
    def set_statementOutcome(self,x):
        self.data[PROP_A059_STATEMENTOUTCOME_KEY] = x
    def get_statementOutcome(self):
        return self.data[PROP_A059_STATEMENTOUTCOME_KEY]
    def set_region(self,x):
        self.data[PROP_A071_REGION_KEY] = x
    def get_region(self):
        return self.data[PROP_A071_REGION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class ConditionMechanismStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_CONDITIONMECHANISMSTATEMENT 
    def set_condition(self,x):
        self.data[PROP_A012_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[PROP_A012_CONDITION_KEY]
    @get_factory_entity('SEPIO:0000396')
    def set_gene(self,x):
        self.data[PROP_A011_GENE_KEY] = x
    def get_gene(self):
        return self.data[PROP_A011_GENE_KEY]
    @get_factory_entity('SEPIO-CG:65108')
    def set_statementOutcome(self,x):
        self.data[PROP_A002_STATEMENTOUTCOME_KEY] = x
    def get_statementOutcome(self):
        return self.data[PROP_A002_STATEMENTOUTCOME_KEY]
    @get_factory_entity('SEPIO:0000354')
    def set_mechanismConfidence(self,x):
        self.data[PROP_A003_MECHANISMCONFIDENCE_KEY] = x
    def get_mechanismConfidence(self):
        return self.data[PROP_A003_MECHANISMCONFIDENCE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class ConditionPenetranceStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_CONDITIONPENETRANCESTATEMENT 
    def add_condition(self,x):
        if not PROP_A107_CONDITION_KEY in self.data:
            self.data[PROP_A107_CONDITION_KEY] = []
        self.data[PROP_A107_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[PROP_A107_CONDITION_KEY]
    @get_factory_entity('SEPIO-CG:65114')
    def set_statementOutcome(self,x):
        self.data[PROP_A108_STATEMENTOUTCOME_KEY] = x
    def get_statementOutcome(self):
        return self.data[PROP_A108_STATEMENTOUTCOME_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class ConditionPrevelanceStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_CONDITIONPREVELANCESTATEMENT 
    def add_condition(self,x):
        if not PROP_A103_CONDITION_KEY in self.data:
            self.data[PROP_A103_CONDITION_KEY] = []
        self.data[PROP_A103_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[PROP_A103_CONDITION_KEY]
    @get_factory_entity('SEPIO-CG:65112')
    def set_population(self,x):
        self.data[PROP_A106_POPULATION_KEY] = x
    def get_population(self):
        return self.data[PROP_A106_POPULATION_KEY]
    def set_minimum(self,x):
        self.data[PROP_A104_MINIMUM_KEY] = x
    def get_minimum(self):
        return self.data[PROP_A104_MINIMUM_KEY]
    def set_maximum(self,x):
        self.data[PROP_A105_MAXIMUM_KEY] = x
    def get_maximum(self):
        return self.data[PROP_A105_MAXIMUM_KEY]
    def set_prevelance(self,x):
        self.data[PROP_A109_PREVELANCE_KEY] = x
    def get_prevelance(self):
        return self.data[PROP_A109_PREVELANCE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class LocusHeterogeneityStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_LOCUSHETEROGENEITYSTATEMENT 
    def set_condition(self,x):
        self.data[PROP_A100_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[PROP_A100_CONDITION_KEY]
    @get_factory_entity('SEPIO:0000396')
    def set_gene(self,x):
        self.data[PROP_A101_GENE_KEY] = x
    def get_gene(self):
        return self.data[PROP_A101_GENE_KEY]
    @get_factory_entity('SEPIO:0000348')
    def set_statementOutcome(self,x):
        self.data[PROP_A102_STATEMENTOUTCOME_KEY] = x
    def get_statementOutcome(self):
        return self.data[PROP_A102_STATEMENTOUTCOME_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class BenignMissenseVariationRateStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_BENIGNMISSENSEVARIATIONRATESTATEMENT 
    def set_region(self,x):
        self.data[PROP_A076_REGION_KEY] = x
    def get_region(self):
        return self.data[PROP_A076_REGION_KEY]
    @get_factory_entity('SEPIO:0000396')
    def set_gene(self,x):
        self.data[PROP_A094_GENE_KEY] = x
    def get_gene(self):
        return self.data[PROP_A094_GENE_KEY]
    @get_factory_entity('SEPIO:0000349')
    def set_statementOutcome(self,x):
        self.data[PROP_A080_STATEMENTOUTCOME_KEY] = x
    def get_statementOutcome(self):
        return self.data[PROP_A080_STATEMENTOUTCOME_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class RegionTypeStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_REGIONTYPESTATEMENT 
    def set_region(self,x):
        self.data[PROP_A063_REGION_KEY] = x
    def get_region(self):
        return self.data[PROP_A063_REGION_KEY]
    @get_factory_entity('SEPIO:0000343')
    def add_statementOutcome(self,x):
        if not PROP_A057_STATEMENTOUTCOME_KEY in self.data:
            self.data[PROP_A057_STATEMENTOUTCOME_KEY] = []
        self.data[PROP_A057_STATEMENTOUTCOME_KEY].append( x ) 
    def get_statementOutcome(self):
        return self.data[PROP_A057_STATEMENTOUTCOME_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class FamilyConditionStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_FAMILYCONDITIONSTATEMENT 
    def set_proband(self,x):
        self.data[PROP_A019_PROBAND_KEY] = x
    def get_proband(self):
        return self.data[PROP_A019_PROBAND_KEY]
    @get_factory_entity('SEPIO-CG:65126')
    def set_statementOutcome(self,x):
        self.data[PROP_A021_STATEMENTOUTCOME_KEY] = x
    def get_statementOutcome(self):
        return self.data[PROP_A021_STATEMENTOUTCOME_KEY]
    def add_condition(self,x):
        if not PROP_A020_CONDITION_KEY in self.data:
            self.data[PROP_A020_CONDITION_KEY] = []
        self.data[PROP_A020_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[PROP_A020_CONDITION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class IndividualAlleleInheritanceStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_INDIVIDUALALLELEINHERITANCESTATEMENT 
    def set_individual(self,x):
        self.data[PROP_A023_INDIVIDUAL_KEY] = x
    def get_individual(self):
        return self.data[PROP_A023_INDIVIDUAL_KEY]
    @get_factory_entity('SEPIO-CG:65125')
    def set_parentalConfirmation(self,x):
        self.data[PROP_A025_PARENTALCONFIRMATION_KEY] = x
    def get_parentalConfirmation(self):
        return self.data[PROP_A025_PARENTALCONFIRMATION_KEY]
    @get_factory_entity('SEPIO:0000392')
    def add_statementOutcome(self,x):
        if not PROP_A074_STATEMENTOUTCOME_KEY in self.data:
            self.data[PROP_A074_STATEMENTOUTCOME_KEY] = []
        self.data[PROP_A074_STATEMENTOUTCOME_KEY].append( x ) 
    def get_statementOutcome(self):
        return self.data[PROP_A074_STATEMENTOUTCOME_KEY]
    def set_canonicalAllele(self,x):
        self.data[PROP_A022_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[PROP_A022_CANONICALALLELE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class IndividualConditionStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_INDIVIDUALCONDITIONSTATEMENT 
    def set_individual(self,x):
        self.data[PROP_A016_INDIVIDUAL_KEY] = x
    def get_individual(self):
        return self.data[PROP_A016_INDIVIDUAL_KEY]
    @get_factory_entity('SEPIO-CG:65126')
    def set_statementOutcome(self,x):
        self.data[PROP_A018_STATEMENTOUTCOME_KEY] = x
    def get_statementOutcome(self):
        return self.data[PROP_A018_STATEMENTOUTCOME_KEY]
    def add_condition(self,x):
        if not PROP_A017_CONDITION_KEY in self.data:
            self.data[PROP_A017_CONDITION_KEY] = []
        self.data[PROP_A017_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[PROP_A017_CONDITION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class IndividualGenotypeStatement(Statement):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_INDIVIDUALGENOTYPESTATEMENT 
    def set_individual(self,x):
        self.data[PROP_A065_INDIVIDUAL_KEY] = x
    def get_individual(self):
        return self.data[PROP_A065_INDIVIDUAL_KEY]
    def set_statementOutcome(self,x):
        self.data[PROP_A188_STATEMENTOUTCOME_KEY] = x
    def get_statementOutcome(self):
        return self.data[PROP_A188_STATEMENTOUTCOME_KEY]
    def add_genotype(self,x):
        if not PROP_A066_GENOTYPE_KEY in self.data:
            self.data[PROP_A066_GENOTYPE_KEY] = []
        self.data[PROP_A066_GENOTYPE_KEY].append( x ) 
    def get_genotype(self):
        return self.data[PROP_A066_GENOTYPE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class EvidenceLine(Entity):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_EVIDENCELINE 
    @get_factory_entity('SEPIO:0000353')
    def set_evidenceStrength(self,x):
        self.data[PROP_A179_EVIDENCESTRENGTH_KEY] = x
    def get_evidenceStrength(self):
        return self.data[PROP_A179_EVIDENCESTRENGTH_KEY]
    def add_evidenceItem(self,x):
        if not PROP_A178_EVIDENCEITEM_KEY in self.data:
            self.data[PROP_A178_EVIDENCEITEM_KEY] = []
        self.data[PROP_A178_EVIDENCEITEM_KEY].append( x ) 
    def get_evidenceItem(self):
        return self.data[PROP_A178_EVIDENCEITEM_KEY]
    def add_contribution(self,x):
        if not PROP_A180_CONTRIBUTION_KEY in self.data:
            self.data[PROP_A180_CONTRIBUTION_KEY] = []
        self.data[PROP_A180_CONTRIBUTION_KEY].append( x ) 
    def get_contribution(self):
        return self.data[PROP_A180_CONTRIBUTION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class Agent(Entity):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_AGENT 
    def set_agentFor(self,x):
        self.data[PROP_A190_AGENTFOR_KEY] = x
    def get_agentFor(self):
        return self.data[PROP_A190_AGENTFOR_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class Contribution(Entity):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_CONTRIBUTION 
    def set_agent(self,x):
        self.data[PROP_A006_AGENT_KEY] = x
    def get_agent(self):
        return self.data[PROP_A006_AGENT_KEY]
    @get_factory_entity('SEPIO-CG:65120')
    def set_contributionRole(self,x):
        self.data[PROP_A008_CONTRIBUTIONROLE_KEY] = x
    def get_contributionRole(self):
        return self.data[PROP_A008_CONTRIBUTIONROLE_KEY]
    def set_contributionDate(self,x):
        self.data[PROP_A007_CONTRIBUTIONDATE_KEY] = x
    def get_contributionDate(self):
        return self.data[PROP_A007_CONTRIBUTIONDATE_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class UserLabel(Entity):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_USERLABEL 
    def set_labelFor(self,x):
        self.data[PROP_A130_LABELFOR_KEY] = x
    def get_labelFor(self):
        return self.data[PROP_A130_LABELFOR_KEY]
    def add_contribution(self,x):
        if not PROP_A131_CONTRIBUTION_KEY in self.data:
            self.data[PROP_A131_CONTRIBUTION_KEY] = []
        self.data[PROP_A131_CONTRIBUTION_KEY].append( x ) 
    def get_contribution(self):
        return self.data[PROP_A131_CONTRIBUTION_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

class ValueSet(Entity):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[ID_KEY] = iri
        self.data[TYPE_KEY] = TYPE_VALUESET 
    @get_factory_entity('SEPIO:0000363')
    def set_valueSetExtensibility(self,x):
        self.data[PROP_A136_VALUESETEXTENSIBILITY_KEY] = x
    def get_valueSetExtensibility(self):
        return self.data[PROP_A136_VALUESETEXTENSIBILITY_KEY]
    def add_valueSetIdentifierSystems(self,x):
        if not PROP_A145_VALUESETIDENTIFIERSYSTEMS_KEY in self.data:
            self.data[PROP_A145_VALUESETIDENTIFIERSYSTEMS_KEY] = []
        self.data[PROP_A145_VALUESETIDENTIFIERSYSTEMS_KEY].append( x ) 
    def get_valueSetIdentifierSystems(self):
        return self.data[PROP_A145_VALUESETIDENTIFIERSYSTEMS_KEY]
    def add_concept(self,x):
        if not PROP_A121_CONCEPT_KEY in self.data:
            self.data[PROP_A121_CONCEPT_KEY] = []
        self.data[PROP_A121_CONCEPT_KEY].append( x ) 
    def get_concept(self):
        return self.data[PROP_A121_CONCEPT_KEY]
    def set_label(self,x):
        self.data[LabelIdentifier] = x
    def get_label(self):
        return self.data[LabelIdentifier]

