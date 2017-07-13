from interpretation_constants import *
from coding_factory import get_factory_coding, get_factory_concept
from node import Node

class ScoringAlgorithm(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_SCORINGALGORITHM_TYPE 
    def set_description(self,x):
        self.data[DMWG_SCORINGALGORITHM_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_SCORINGALGORITHM_DESCRIPTION_KEY]

class AssertionMethod(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ASSERTIONMETHOD_TYPE 
    def set_scoringAlgorithm(self,x):
        self.data[DMWG_ASSERTIONMETHOD_SCORINGALGORITHM_KEY] = x
    def get_scoringAlgorithm(self):
        return self.data[DMWG_ASSERTIONMETHOD_SCORINGALGORITHM_KEY]
    def set_version(self,x):
        self.data[DMWG_ASSERTIONMETHOD_VERSION_KEY] = x
    def get_version(self):
        return self.data[DMWG_ASSERTIONMETHOD_VERSION_KEY]
    def set_description(self,x):
        self.data[DMWG_ASSERTIONMETHOD_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_ASSERTIONMETHOD_DESCRIPTION_KEY]
    def set_url(self,x):
        self.data[DMWG_ASSERTIONMETHOD_URL_KEY] = x
    def get_url(self):
        return self.data[DMWG_ASSERTIONMETHOD_URL_KEY]

class Contribution(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONTRIBUTION_TYPE 
    @get_factory_concept('VS021')
    def set_role(self,x):
        self.data[DMWG_CONTRIBUTION_ROLE_KEY] = x
    def get_role(self):
        return self.data[DMWG_CONTRIBUTION_ROLE_KEY]
    def set_onDate(self,x):
        self.data[DMWG_CONTRIBUTION_ONDATE_KEY] = x
    def get_onDate(self):
        return self.data[DMWG_CONTRIBUTION_ONDATE_KEY]
    def set_agent(self,x):
        self.data[DMWG_CONTRIBUTION_AGENT_KEY] = x
    def get_agent(self):
        return self.data[DMWG_CONTRIBUTION_AGENT_KEY]

class Example(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_EXAMPLE_TYPE 
    def set_description(self,x):
        self.data[DMWG_EXAMPLE_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_EXAMPLE_DESCRIPTION_KEY]
    def set_image(self,x):
        self.data[DMWG_EXAMPLE_IMAGE_KEY] = x
    def get_image(self):
        return self.data[DMWG_EXAMPLE_IMAGE_KEY]
    def set_author(self,x):
        self.data[DMWG_EXAMPLE_AUTHOR_KEY] = x
    def get_author(self):
        return self.data[DMWG_EXAMPLE_AUTHOR_KEY]
    def set_searchTags(self,x):
        self.data[DMWG_EXAMPLE_SEARCHTAGS_KEY] = x
    def get_searchTags(self):
        return self.data[DMWG_EXAMPLE_SEARCHTAGS_KEY]
    def set_index(self,x):
        self.data[DMWG_EXAMPLE_INDEX_KEY] = x
    def get_index(self):
        return self.data[DMWG_EXAMPLE_INDEX_KEY]
    def set_informationId(self,x):
        self.data[DMWG_EXAMPLE_INFORMATIONID_KEY] = x
    def get_informationId(self):
        return self.data[DMWG_EXAMPLE_INFORMATIONID_KEY]

class Agent(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_AGENT_TYPE 
    def set_description(self,x):
        self.data[DMWG_AGENT_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_AGENT_DESCRIPTION_KEY]
    def set_name(self,x):
        self.data[DMWG_AGENT_NAME_KEY] = x
    def get_name(self):
        return self.data[DMWG_AGENT_NAME_KEY]

class Individual(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INDIVIDUAL_TYPE 
    def set_description(self,x):
        self.data[DMWG_INDIVIDUAL_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_INDIVIDUAL_DESCRIPTION_KEY]

class ValueSet(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_VALUESET_TYPE 
    def set_description(self,x):
        self.data[DMWG_VALUESET_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_VALUESET_DESCRIPTION_KEY]
    def set_name(self,x):
        self.data[DMWG_VALUESET_NAME_KEY] = x
    def get_name(self):
        return self.data[DMWG_VALUESET_NAME_KEY]
    def add_includesCoding(self,x):
        if not DMWG_VALUESET_INCLUDESCODING_KEY in self.data:
            self.data[DMWG_VALUESET_INCLUDESCODING_KEY] = []
        self.data[DMWG_VALUESET_INCLUDESCODING_KEY].append( x ) 
    def get_includesCoding(self):
        return self.data[DMWG_VALUESET_INCLUDESCODING_KEY]

class ValueSetCoding(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_VALUESETCODING_TYPE 

class EvidenceLine(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_EVIDENCELINE_TYPE 
    def add_contribution(self,x):
        if not DMWG_EVIDENCELINE_CONTRIBUTION_KEY in self.data:
            self.data[DMWG_EVIDENCELINE_CONTRIBUTION_KEY] = []
        self.data[DMWG_EVIDENCELINE_CONTRIBUTION_KEY].append( x ) 
    def get_contribution(self):
        return self.data[DMWG_EVIDENCELINE_CONTRIBUTION_KEY]
    def set_explanation(self,x):
        self.data[DMWG_EVIDENCELINE_EXPLANATION_KEY] = x
    def get_explanation(self):
        return self.data[DMWG_EVIDENCELINE_EXPLANATION_KEY]
    @get_factory_concept('VS017')
    def set_evidenceStrength(self,x):
        self.data[DMWG_EVIDENCELINE_EVIDENCESTRENGTH_KEY] = x
    def get_evidenceStrength(self):
        return self.data[DMWG_EVIDENCELINE_EVIDENCESTRENGTH_KEY]
    def add_information(self,x):
        if not DMWG_EVIDENCELINE_INFORMATION_KEY in self.data:
            self.data[DMWG_EVIDENCELINE_INFORMATION_KEY] = []
        self.data[DMWG_EVIDENCELINE_INFORMATION_KEY].append( x ) 
    def get_information(self):
        return self.data[DMWG_EVIDENCELINE_INFORMATION_KEY]

class ReferenceSequence(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REFERENCESEQUENCE_TYPE 
    @get_factory_concept('VS020')
    def set_accession(self,x):
        self.data[DMWG_REFERENCESEQUENCE_ACCESSION_KEY] = x
    def get_accession(self):
        return self.data[DMWG_REFERENCESEQUENCE_ACCESSION_KEY]

class CodeSystem(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CODESYSTEM_TYPE 

class ContextualAllele(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONTEXTUALALLELE_TYPE 
    def add_legacyNames(self,x):
        if not DMWG_CONTEXTUALALLELE_LEGACYNAMES_KEY in self.data:
            self.data[DMWG_CONTEXTUALALLELE_LEGACYNAMES_KEY] = []
        self.data[DMWG_CONTEXTUALALLELE_LEGACYNAMES_KEY].append( x ) 
    def get_legacyNames(self):
        return self.data[DMWG_CONTEXTUALALLELE_LEGACYNAMES_KEY]
    def set_alleleName(self,x):
        self.data[DMWG_CONTEXTUALALLELE_ALLELENAME_KEY] = x
    def get_alleleName(self):
        return self.data[DMWG_CONTEXTUALALLELE_ALLELENAME_KEY]
    def set_relatedCanonicalAllele(self,x):
        self.data[DMWG_CONTEXTUALALLELE_RELATEDCANONICALALLELE_KEY] = x
    def get_relatedCanonicalAllele(self):
        return self.data[DMWG_CONTEXTUALALLELE_RELATEDCANONICALALLELE_KEY]

class Gene(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_GENE_TYPE 
    def set_symbol(self,x):
        self.data[DMWG_GENE_SYMBOL_KEY] = x
    def get_symbol(self):
        return self.data[DMWG_GENE_SYMBOL_KEY]

class Criterion(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CRITERION_TYPE 
    @get_factory_concept('VS017')
    def set_defaultStrength(self,x):
        self.data[DMWG_CRITERION_DEFAULTSTRENGTH_KEY] = x
    def get_defaultStrength(self):
        return self.data[DMWG_CRITERION_DEFAULTSTRENGTH_KEY]
    def set_shortDescription(self,x):
        self.data[DMWG_CRITERION_SHORTDESCRIPTION_KEY] = x
    def get_shortDescription(self):
        return self.data[DMWG_CRITERION_SHORTDESCRIPTION_KEY]
    def set_description(self,x):
        self.data[DMWG_CRITERION_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_CRITERION_DESCRIPTION_KEY]

class CanonicalAllele(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CANONICALALLELE_TYPE 
    def set_identifier(self,x):
        self.data[DMWG_CANONICALALLELE_IDENTIFIER_KEY] = x
    def get_identifier(self):
        return self.data[DMWG_CANONICALALLELE_IDENTIFIER_KEY]
    def set_preferredCtxAllele(self,x):
        self.data[DMWG_CANONICALALLELE_PREFERREDCTXALLELE_KEY] = x
    def get_preferredCtxAllele(self):
        return self.data[DMWG_CANONICALALLELE_PREFERREDCTXALLELE_KEY]

class Information(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INFORMATION_TYPE 
    def add_contribution(self,x):
        if not DMWG_INFORMATION_CONTRIBUTION_KEY in self.data:
            self.data[DMWG_INFORMATION_CONTRIBUTION_KEY] = []
        self.data[DMWG_INFORMATION_CONTRIBUTION_KEY].append( x ) 
    def get_contribution(self):
        return self.data[DMWG_INFORMATION_CONTRIBUTION_KEY]
    def add_source(self,x):
        if not DMWG_INFORMATION_SOURCE_KEY in self.data:
            self.data[DMWG_INFORMATION_SOURCE_KEY] = []
        self.data[DMWG_INFORMATION_SOURCE_KEY].append( x ) 
    def get_source(self):
        return self.data[DMWG_INFORMATION_SOURCE_KEY]
    def set_explanation(self,x):
        self.data[DMWG_INFORMATION_EXPLANATION_KEY] = x
    def get_explanation(self):
        return self.data[DMWG_INFORMATION_EXPLANATION_KEY]

class DeNovoAllele(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_DENOVOALLELE_TYPE 
    def set_paternityConfirmed(self,x):
        self.data[DMWG_DENOVOALLELE_PATERNITYCONFIRMED_KEY] = x
    def get_paternityConfirmed(self):
        return self.data[DMWG_DENOVOALLELE_PATERNITYCONFIRMED_KEY]
    def set_maternityConfirmed(self,x):
        self.data[DMWG_DENOVOALLELE_MATERNITYCONFIRMED_KEY] = x
    def get_maternityConfirmed(self):
        return self.data[DMWG_DENOVOALLELE_MATERNITYCONFIRMED_KEY]
    def set_individual(self,x):
        self.data[DMWG_DENOVOALLELE_INDIVIDUAL_KEY] = x
    def get_individual(self):
        return self.data[DMWG_DENOVOALLELE_INDIVIDUAL_KEY]
    def set_canonicalAllele(self,x):
        self.data[DMWG_DENOVOALLELE_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_DENOVOALLELE_CANONICALALLELE_KEY]
    @get_factory_coding('VS022')
    def add_alleleInheritance(self,x):
        if not DMWG_DENOVOALLELE_ALLELEINHERITANCE_KEY in self.data:
            self.data[DMWG_DENOVOALLELE_ALLELEINHERITANCE_KEY] = []
        self.data[DMWG_DENOVOALLELE_ALLELEINHERITANCE_KEY].append( x ) 
    def get_alleleInheritance(self):
        return self.data[DMWG_DENOVOALLELE_ALLELEINHERITANCE_KEY]

class FamilyHistory(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_FAMILYHISTORY_TYPE 
    def set_familyHasCondition(self,x):
        self.data[DMWG_FAMILYHISTORY_FAMILYHASCONDITION_KEY] = x
    def get_familyHasCondition(self):
        return self.data[DMWG_FAMILYHISTORY_FAMILYHASCONDITION_KEY]
    def add_condition(self,x):
        if not DMWG_FAMILYHISTORY_CONDITION_KEY in self.data:
            self.data[DMWG_FAMILYHISTORY_CONDITION_KEY] = []
        self.data[DMWG_FAMILYHISTORY_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_FAMILYHISTORY_CONDITION_KEY]
    def set_proband(self,x):
        self.data[DMWG_FAMILYHISTORY_PROBAND_KEY] = x
    def get_proband(self):
        return self.data[DMWG_FAMILYHISTORY_PROBAND_KEY]

class VariantInterpretation(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_VARIANTINTERPRETATION_TYPE 
    def add_evidence(self,x):
        if not DMWG_VARIANTINTERPRETATION_EVIDENCE_KEY in self.data:
            self.data[DMWG_VARIANTINTERPRETATION_EVIDENCE_KEY] = []
        self.data[DMWG_VARIANTINTERPRETATION_EVIDENCE_KEY].append( x ) 
    def get_evidence(self):
        return self.data[DMWG_VARIANTINTERPRETATION_EVIDENCE_KEY]
    def set_variant(self,x):
        self.data[DMWG_VARIANTINTERPRETATION_VARIANT_KEY] = x
    def get_variant(self):
        return self.data[DMWG_VARIANTINTERPRETATION_VARIANT_KEY]
    def add_condition(self,x):
        if not DMWG_VARIANTINTERPRETATION_CONDITION_KEY in self.data:
            self.data[DMWG_VARIANTINTERPRETATION_CONDITION_KEY] = []
        self.data[DMWG_VARIANTINTERPRETATION_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_VARIANTINTERPRETATION_CONDITION_KEY]
    @get_factory_coding('VS003')
    def set_clinicalSignificance(self,x):
        self.data[DMWG_VARIANTINTERPRETATION_CLINICALSIGNIFICANCE_KEY] = x
    def get_clinicalSignificance(self):
        return self.data[DMWG_VARIANTINTERPRETATION_CLINICALSIGNIFICANCE_KEY]
    def set_assertionMethod(self,x):
        self.data[DMWG_VARIANTINTERPRETATION_ASSERTIONMETHOD_KEY] = x
    def get_assertionMethod(self):
        return self.data[DMWG_VARIANTINTERPRETATION_ASSERTIONMETHOD_KEY]

class BenignMissenseVariationRate(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_BENIGNMISSENSEVARIATIONRATE_TYPE 
    def set_region(self,x):
        self.data[DMWG_BENIGNMISSENSEVARIATIONRATE_REGION_KEY] = x
    def get_region(self):
        return self.data[DMWG_BENIGNMISSENSEVARIATIONRATE_REGION_KEY]
    def set_gene(self,x):
        self.data[DMWG_BENIGNMISSENSEVARIATIONRATE_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_BENIGNMISSENSEVARIATIONRATE_GENE_KEY]
    @get_factory_coding('VS014')
    def set_value(self,x):
        self.data[DMWG_BENIGNMISSENSEVARIATIONRATE_VALUE_KEY] = x
    def get_value(self):
        return self.data[DMWG_BENIGNMISSENSEVARIATIONRATE_VALUE_KEY]

class MendelianCondition(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_MENDELIANCONDITION_TYPE 
    @get_factory_concept('VS018')
    def add_disease(self,x):
        if not DMWG_MENDELIANCONDITION_DISEASE_KEY in self.data:
            self.data[DMWG_MENDELIANCONDITION_DISEASE_KEY] = []
        self.data[DMWG_MENDELIANCONDITION_DISEASE_KEY].append( x ) 
    def get_disease(self):
        return self.data[DMWG_MENDELIANCONDITION_DISEASE_KEY]
    @get_factory_coding('VS007')
    def set_modeOfInheritance(self,x):
        self.data[DMWG_MENDELIANCONDITION_MODEOFINHERITANCE_KEY] = x
    def get_modeOfInheritance(self):
        return self.data[DMWG_MENDELIANCONDITION_MODEOFINHERITANCE_KEY]
    def set_gene(self,x):
        self.data[DMWG_MENDELIANCONDITION_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_MENDELIANCONDITION_GENE_KEY]
    @get_factory_concept('VS019')
    def add_phenotype(self,x):
        if not DMWG_MENDELIANCONDITION_PHENOTYPE_KEY in self.data:
            self.data[DMWG_MENDELIANCONDITION_PHENOTYPE_KEY] = []
        self.data[DMWG_MENDELIANCONDITION_PHENOTYPE_KEY].append( x ) 
    def get_phenotype(self):
        return self.data[DMWG_MENDELIANCONDITION_PHENOTYPE_KEY]
    def set_name(self,x):
        self.data[DMWG_MENDELIANCONDITION_NAME_KEY] = x
    def get_name(self):
        return self.data[DMWG_MENDELIANCONDITION_NAME_KEY]

class IndividualCondition(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INDIVIDUALCONDITION_TYPE 
    def set_hasCondition(self,x):
        self.data[DMWG_INDIVIDUALCONDITION_HASCONDITION_KEY] = x
    def get_hasCondition(self):
        return self.data[DMWG_INDIVIDUALCONDITION_HASCONDITION_KEY]
    def set_individual(self,x):
        self.data[DMWG_INDIVIDUALCONDITION_INDIVIDUAL_KEY] = x
    def get_individual(self):
        return self.data[DMWG_INDIVIDUALCONDITION_INDIVIDUAL_KEY]
    def add_condition(self,x):
        if not DMWG_INDIVIDUALCONDITION_CONDITION_KEY in self.data:
            self.data[DMWG_INDIVIDUALCONDITION_CONDITION_KEY] = []
        self.data[DMWG_INDIVIDUALCONDITION_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_INDIVIDUALCONDITION_CONDITION_KEY]

class AggregateSegregationData(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_AGGREGATESEGREGATIONDATA_TYPE 
    def set_totalOfAlleleNegConditionPosIndividuals(self,x):
        self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALOFALLELENEGCONDITIONPOSINDIVIDUALS_KEY] = x
    def get_totalOfAlleleNegConditionPosIndividuals(self):
        return self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALOFALLELENEGCONDITIONPOSINDIVIDUALS_KEY]
    def set_totalOfUntestedConditionPosIndividuals(self,x):
        self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALOFUNTESTEDCONDITIONPOSINDIVIDUALS_KEY] = x
    def get_totalOfUntestedConditionPosIndividuals(self):
        return self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALOFUNTESTEDCONDITIONPOSINDIVIDUALS_KEY]
    def set_totalOfUntestedConditionNegIndividuals(self,x):
        self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALOFUNTESTEDCONDITIONNEGINDIVIDUALS_KEY] = x
    def get_totalOfUntestedConditionNegIndividuals(self):
        return self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALOFUNTESTEDCONDITIONNEGINDIVIDUALS_KEY]
    def set_totalOfFamiliesWithInconsistentSegregations(self,x):
        self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALOFFAMILIESWITHINCONSISTENTSEGREGATIONS_KEY] = x
    def get_totalOfFamiliesWithInconsistentSegregations(self):
        return self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALOFFAMILIESWITHINCONSISTENTSEGREGATIONS_KEY]
    @get_factory_concept('VS007')
    def set_modeOfInheritance(self,x):
        self.data[DMWG_AGGREGATESEGREGATIONDATA_MODEOFINHERITANCE_KEY] = x
    def get_modeOfInheritance(self):
        return self.data[DMWG_AGGREGATESEGREGATIONDATA_MODEOFINHERITANCE_KEY]
    def set_totalOfAllelePosConditionPosIndividuals(self,x):
        self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALOFALLELEPOSCONDITIONPOSINDIVIDUALS_KEY] = x
    def get_totalOfAllelePosConditionPosIndividuals(self):
        return self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALOFALLELEPOSCONDITIONPOSINDIVIDUALS_KEY]
    def set_totalOfAlleleNegConditionNegIndividuals(self,x):
        self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALOFALLELENEGCONDITIONNEGINDIVIDUALS_KEY] = x
    def get_totalOfAlleleNegConditionNegIndividuals(self):
        return self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALOFALLELENEGCONDITIONNEGINDIVIDUALS_KEY]
    def set_totalOfAllelePosConditionNegIndividuals(self,x):
        self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALOFALLELEPOSCONDITIONNEGINDIVIDUALS_KEY] = x
    def get_totalOfAllelePosConditionNegIndividuals(self):
        return self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALOFALLELEPOSCONDITIONNEGINDIVIDUALS_KEY]
    def set_condition(self,x):
        self.data[DMWG_AGGREGATESEGREGATIONDATA_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[DMWG_AGGREGATESEGREGATIONDATA_CONDITION_KEY]
    def set_canonicalAllele(self,x):
        self.data[DMWG_AGGREGATESEGREGATIONDATA_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_AGGREGATESEGREGATIONDATA_CANONICALALLELE_KEY]
    def add_familySegregationData(self,x):
        if not DMWG_AGGREGATESEGREGATIONDATA_FAMILYSEGREGATIONDATA_KEY in self.data:
            self.data[DMWG_AGGREGATESEGREGATIONDATA_FAMILYSEGREGATIONDATA_KEY] = []
        self.data[DMWG_AGGREGATESEGREGATIONDATA_FAMILYSEGREGATIONDATA_KEY].append( x ) 
    def get_familySegregationData(self):
        return self.data[DMWG_AGGREGATESEGREGATIONDATA_FAMILYSEGREGATIONDATA_KEY]
    def set_totalNumberOfSegregations(self,x):
        self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALNUMBEROFSEGREGATIONS_KEY] = x
    def get_totalNumberOfSegregations(self):
        return self.data[DMWG_AGGREGATESEGREGATIONDATA_TOTALNUMBEROFSEGREGATIONS_KEY]

class Conservation(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONSERVATION_TYPE 
    def set_allele(self,x):
        self.data[DMWG_CONSERVATION_ALLELE_KEY] = x
    def get_allele(self):
        return self.data[DMWG_CONSERVATION_ALLELE_KEY]
    def set_algorithm(self,x):
        self.data[DMWG_CONSERVATION_ALGORITHM_KEY] = x
    def get_algorithm(self):
        return self.data[DMWG_CONSERVATION_ALGORITHM_KEY]
    def set_conserved(self,x):
        self.data[DMWG_CONSERVATION_CONSERVED_KEY] = x
    def get_conserved(self):
        return self.data[DMWG_CONSERVATION_CONSERVED_KEY]
    def set_score(self,x):
        self.data[DMWG_CONSERVATION_SCORE_KEY] = x
    def get_score(self):
        return self.data[DMWG_CONSERVATION_SCORE_KEY]

class ConditionPenetrance(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONDITIONPENETRANCE_TYPE 
    def add_condition(self,x):
        if not DMWG_CONDITIONPENETRANCE_CONDITION_KEY in self.data:
            self.data[DMWG_CONDITIONPENETRANCE_CONDITION_KEY] = []
        self.data[DMWG_CONDITIONPENETRANCE_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_CONDITIONPENETRANCE_CONDITION_KEY]
    @get_factory_concept('VS015')
    def set_penetrance(self,x):
        self.data[DMWG_CONDITIONPENETRANCE_PENETRANCE_KEY] = x
    def get_penetrance(self):
        return self.data[DMWG_CONDITIONPENETRANCE_PENETRANCE_KEY]

class InSilicoPrediction(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INSILICOPREDICTION_TYPE 
    def set_transcript(self,x):
        self.data[DMWG_INSILICOPREDICTION_TRANSCRIPT_KEY] = x
    def get_transcript(self):
        return self.data[DMWG_INSILICOPREDICTION_TRANSCRIPT_KEY]
    def set_quantitativePrediction(self,x):
        self.data[DMWG_INSILICOPREDICTION_QUANTITATIVEPREDICTION_KEY] = x
    def get_quantitativePrediction(self):
        return self.data[DMWG_INSILICOPREDICTION_QUANTITATIVEPREDICTION_KEY]
    def set_canonicalAllele(self,x):
        self.data[DMWG_INSILICOPREDICTION_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_INSILICOPREDICTION_CANONICALALLELE_KEY]
    @get_factory_concept('VS010')
    def set_predictionType(self,x):
        self.data[DMWG_INSILICOPREDICTION_PREDICTIONTYPE_KEY] = x
    def get_predictionType(self):
        return self.data[DMWG_INSILICOPREDICTION_PREDICTIONTYPE_KEY]
    def set_algorithm(self,x):
        self.data[DMWG_INSILICOPREDICTION_ALGORITHM_KEY] = x
    def get_algorithm(self):
        return self.data[DMWG_INSILICOPREDICTION_ALGORITHM_KEY]
    def set_categoricalPrediction(self,x):
        self.data[DMWG_INSILICOPREDICTION_CATEGORICALPREDICTION_KEY] = x
    def get_categoricalPrediction(self):
        return self.data[DMWG_INSILICOPREDICTION_CATEGORICALPREDICTION_KEY]

class Family(Information):
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

class CriterionAssessment(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CRITERIONASSESSMENT_TYPE 
    def set_criterion(self,x):
        self.data[DMWG_CRITERIONASSESSMENT_CRITERION_KEY] = x
    def get_criterion(self):
        return self.data[DMWG_CRITERIONASSESSMENT_CRITERION_KEY]
    def set_variant(self,x):
        self.data[DMWG_CRITERIONASSESSMENT_VARIANT_KEY] = x
    def get_variant(self):
        return self.data[DMWG_CRITERIONASSESSMENT_VARIANT_KEY]
    @get_factory_coding('VS011')
    def set_outcome(self,x):
        self.data[DMWG_CRITERIONASSESSMENT_OUTCOME_KEY] = x
    def get_outcome(self):
        return self.data[DMWG_CRITERIONASSESSMENT_OUTCOME_KEY]
    def add_condition(self,x):
        if not DMWG_CRITERIONASSESSMENT_CONDITION_KEY in self.data:
            self.data[DMWG_CRITERIONASSESSMENT_CONDITION_KEY] = []
        self.data[DMWG_CRITERIONASSESSMENT_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_CRITERIONASSESSMENT_CONDITION_KEY]
    def add_evidence(self,x):
        if not DMWG_CRITERIONASSESSMENT_EVIDENCE_KEY in self.data:
            self.data[DMWG_CRITERIONASSESSMENT_EVIDENCE_KEY] = []
        self.data[DMWG_CRITERIONASSESSMENT_EVIDENCE_KEY].append( x ) 
    def get_evidence(self):
        return self.data[DMWG_CRITERIONASSESSMENT_EVIDENCE_KEY]

class ConditionPrevelance(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONDITIONPREVELANCE_TYPE 
    @get_factory_concept('VS013')
    def set_population(self,x):
        self.data[DMWG_CONDITIONPREVELANCE_POPULATION_KEY] = x
    def get_population(self):
        return self.data[DMWG_CONDITIONPREVELANCE_POPULATION_KEY]
    def set_minimum(self,x):
        self.data[DMWG_CONDITIONPREVELANCE_MINIMUM_KEY] = x
    def get_minimum(self):
        return self.data[DMWG_CONDITIONPREVELANCE_MINIMUM_KEY]
    def set_maximum(self,x):
        self.data[DMWG_CONDITIONPREVELANCE_MAXIMUM_KEY] = x
    def get_maximum(self):
        return self.data[DMWG_CONDITIONPREVELANCE_MAXIMUM_KEY]
    def add_condition(self,x):
        if not DMWG_CONDITIONPREVELANCE_CONDITION_KEY in self.data:
            self.data[DMWG_CONDITIONPREVELANCE_CONDITION_KEY] = []
        self.data[DMWG_CONDITIONPREVELANCE_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_CONDITIONPREVELANCE_CONDITION_KEY]
    def set_prevelance(self,x):
        self.data[DMWG_CONDITIONPREVELANCE_PREVELANCE_KEY] = x
    def get_prevelance(self):
        return self.data[DMWG_CONDITIONPREVELANCE_PREVELANCE_KEY]

class ConditionEtiology(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONDITIONETIOLOGY_TYPE 
    def set_specificity(self,x):
        self.data[DMWG_CONDITIONETIOLOGY_SPECIFICITY_KEY] = x
    def get_specificity(self):
        return self.data[DMWG_CONDITIONETIOLOGY_SPECIFICITY_KEY]
    def set_condition(self,x):
        self.data[DMWG_CONDITIONETIOLOGY_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[DMWG_CONDITIONETIOLOGY_CONDITION_KEY]
    def set_gene(self,x):
        self.data[DMWG_CONDITIONETIOLOGY_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_CONDITIONETIOLOGY_GENE_KEY]

class FamilySegregationData(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_FAMILYSEGREGATIONDATA_TYPE 
    def set_anyInconsistentSegregations(self,x):
        self.data[DMWG_FAMILYSEGREGATIONDATA_ANYINCONSISTENTSEGREGATIONS_KEY] = x
    def get_anyInconsistentSegregations(self):
        return self.data[DMWG_FAMILYSEGREGATIONDATA_ANYINCONSISTENTSEGREGATIONS_KEY]
    def set_phenotypeNegativeAlleleNegative(self,x):
        self.data[DMWG_FAMILYSEGREGATIONDATA_PHENOTYPENEGATIVEALLELENEGATIVE_KEY] = x
    def get_phenotypeNegativeAlleleNegative(self):
        return self.data[DMWG_FAMILYSEGREGATIONDATA_PHENOTYPENEGATIVEALLELENEGATIVE_KEY]
    def set_phenotypePositiveAlleleNegative(self,x):
        self.data[DMWG_FAMILYSEGREGATIONDATA_PHENOTYPEPOSITIVEALLELENEGATIVE_KEY] = x
    def get_phenotypePositiveAlleleNegative(self):
        return self.data[DMWG_FAMILYSEGREGATIONDATA_PHENOTYPEPOSITIVEALLELENEGATIVE_KEY]
    def add_columns(self,x):
        if not DMWG_FAMILYSEGREGATIONDATA_COLUMNS_KEY in self.data:
            self.data[DMWG_FAMILYSEGREGATIONDATA_COLUMNS_KEY] = []
        self.data[DMWG_FAMILYSEGREGATIONDATA_COLUMNS_KEY].append( x ) 
    def get_columns(self):
        return self.data[DMWG_FAMILYSEGREGATIONDATA_COLUMNS_KEY]
    def add_affectedValues(self,x):
        if not DMWG_FAMILYSEGREGATIONDATA_AFFECTEDVALUES_KEY in self.data:
            self.data[DMWG_FAMILYSEGREGATIONDATA_AFFECTEDVALUES_KEY] = []
        self.data[DMWG_FAMILYSEGREGATIONDATA_AFFECTEDVALUES_KEY].append( x ) 
    def get_affectedValues(self):
        return self.data[DMWG_FAMILYSEGREGATIONDATA_AFFECTEDVALUES_KEY]
    def add_genotypeValues(self,x):
        if not DMWG_FAMILYSEGREGATIONDATA_GENOTYPEVALUES_KEY in self.data:
            self.data[DMWG_FAMILYSEGREGATIONDATA_GENOTYPEVALUES_KEY] = []
        self.data[DMWG_FAMILYSEGREGATIONDATA_GENOTYPEVALUES_KEY].append( x ) 
    def get_genotypeValues(self):
        return self.data[DMWG_FAMILYSEGREGATIONDATA_GENOTYPEVALUES_KEY]
    def add_pedigree(self,x):
        if not DMWG_FAMILYSEGREGATIONDATA_PEDIGREE_KEY in self.data:
            self.data[DMWG_FAMILYSEGREGATIONDATA_PEDIGREE_KEY] = []
        self.data[DMWG_FAMILYSEGREGATIONDATA_PEDIGREE_KEY].append( x ) 
    def get_pedigree(self):
        return self.data[DMWG_FAMILYSEGREGATIONDATA_PEDIGREE_KEY]
    def set_phenotypeNegativeAllelePositive(self,x):
        self.data[DMWG_FAMILYSEGREGATIONDATA_PHENOTYPENEGATIVEALLELEPOSITIVE_KEY] = x
    def get_phenotypeNegativeAllelePositive(self):
        return self.data[DMWG_FAMILYSEGREGATIONDATA_PHENOTYPENEGATIVEALLELEPOSITIVE_KEY]
    def set_phenotypePositiveAllelePositive(self,x):
        self.data[DMWG_FAMILYSEGREGATIONDATA_PHENOTYPEPOSITIVEALLELEPOSITIVE_KEY] = x
    def get_phenotypePositiveAllelePositive(self):
        return self.data[DMWG_FAMILYSEGREGATIONDATA_PHENOTYPEPOSITIVEALLELEPOSITIVE_KEY]
    def set_family(self,x):
        self.data[DMWG_FAMILYSEGREGATIONDATA_FAMILY_KEY] = x
    def get_family(self):
        return self.data[DMWG_FAMILYSEGREGATIONDATA_FAMILY_KEY]
    def set_canonicalAllele(self,x):
        self.data[DMWG_FAMILYSEGREGATIONDATA_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_FAMILYSEGREGATIONDATA_CANONICALALLELE_KEY]
    def set_condition(self,x):
        self.data[DMWG_FAMILYSEGREGATIONDATA_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[DMWG_FAMILYSEGREGATIONDATA_CONDITION_KEY]

class RegionAnnotation(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REGIONANNOTATION_TYPE 
    @get_factory_coding('VS004')
    def add_excludedTypes(self,x):
        if not DMWG_REGIONANNOTATION_EXCLUDEDTYPES_KEY in self.data:
            self.data[DMWG_REGIONANNOTATION_EXCLUDEDTYPES_KEY] = []
        self.data[DMWG_REGIONANNOTATION_EXCLUDEDTYPES_KEY].append( x ) 
    def get_excludedTypes(self):
        return self.data[DMWG_REGIONANNOTATION_EXCLUDEDTYPES_KEY]
    @get_factory_coding('VS004')
    def add_includedTypes(self,x):
        if not DMWG_REGIONANNOTATION_INCLUDEDTYPES_KEY in self.data:
            self.data[DMWG_REGIONANNOTATION_INCLUDEDTYPES_KEY] = []
        self.data[DMWG_REGIONANNOTATION_INCLUDEDTYPES_KEY].append( x ) 
    def get_includedTypes(self):
        return self.data[DMWG_REGIONANNOTATION_INCLUDEDTYPES_KEY]
    def set_region(self,x):
        self.data[DMWG_REGIONANNOTATION_REGION_KEY] = x
    def get_region(self):
        return self.data[DMWG_REGIONANNOTATION_REGION_KEY]

class RegionAlleles(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REGIONALLELES_TYPE 
    def add_includedAlleles(self,x):
        if not DMWG_REGIONALLELES_INCLUDEDALLELES_KEY in self.data:
            self.data[DMWG_REGIONALLELES_INCLUDEDALLELES_KEY] = []
        self.data[DMWG_REGIONALLELES_INCLUDEDALLELES_KEY].append( x ) 
    def get_includedAlleles(self):
        return self.data[DMWG_REGIONALLELES_INCLUDEDALLELES_KEY]
    def add_excludedAlleles(self,x):
        if not DMWG_REGIONALLELES_EXCLUDEDALLELES_KEY in self.data:
            self.data[DMWG_REGIONALLELES_EXCLUDEDALLELES_KEY] = []
        self.data[DMWG_REGIONALLELES_EXCLUDEDALLELES_KEY].append( x ) 
    def get_excludedAlleles(self):
        return self.data[DMWG_REGIONALLELES_EXCLUDEDALLELES_KEY]
    def set_region(self,x):
        self.data[DMWG_REGIONALLELES_REGION_KEY] = x
    def get_region(self):
        return self.data[DMWG_REGIONALLELES_REGION_KEY]

class FunctionalData(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_FUNCTIONALDATA_TYPE 
    @get_factory_concept('VS012')
    def set_dataType(self,x):
        self.data[DMWG_FUNCTIONALDATA_DATATYPE_KEY] = x
    def get_dataType(self):
        return self.data[DMWG_FUNCTIONALDATA_DATATYPE_KEY]
    def set_result(self,x):
        self.data[DMWG_FUNCTIONALDATA_RESULT_KEY] = x
    def get_result(self):
        return self.data[DMWG_FUNCTIONALDATA_RESULT_KEY]
    def set_gene(self,x):
        self.data[DMWG_FUNCTIONALDATA_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_FUNCTIONALDATA_GENE_KEY]
    def set_contextualAllele(self,x):
        self.data[DMWG_FUNCTIONALDATA_CONTEXTUALALLELE_KEY] = x
    def get_contextualAllele(self):
        return self.data[DMWG_FUNCTIONALDATA_CONTEXTUALALLELE_KEY]

class CaseControl(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CASECONTROL_TYPE 
    def set_canonicalAllele(self,x):
        self.data[DMWG_CASECONTROL_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_CASECONTROL_CANONICALALLELE_KEY]
    def set_condition(self,x):
        self.data[DMWG_CASECONTROL_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[DMWG_CASECONTROL_CONDITION_KEY]
    def set_controlGroupFrequency(self,x):
        self.data[DMWG_CASECONTROL_CONTROLGROUPFREQUENCY_KEY] = x
    def get_controlGroupFrequency(self):
        return self.data[DMWG_CASECONTROL_CONTROLGROUPFREQUENCY_KEY]
    def set_caseGroupFrequency(self,x):
        self.data[DMWG_CASECONTROL_CASEGROUPFREQUENCY_KEY] = x
    def get_caseGroupFrequency(self):
        return self.data[DMWG_CASECONTROL_CASEGROUPFREQUENCY_KEY]
    def set_confidenceLevel(self,x):
        self.data[DMWG_CASECONTROL_CONFIDENCELEVEL_KEY] = x
    def get_confidenceLevel(self):
        return self.data[DMWG_CASECONTROL_CONFIDENCELEVEL_KEY]
    def set_oddsRatio(self,x):
        self.data[DMWG_CASECONTROL_ODDSRATIO_KEY] = x
    def get_oddsRatio(self):
        return self.data[DMWG_CASECONTROL_ODDSRATIO_KEY]
    def set_confidenceIntervalUpper(self,x):
        self.data[DMWG_CASECONTROL_CONFIDENCEINTERVALUPPER_KEY] = x
    def get_confidenceIntervalUpper(self):
        return self.data[DMWG_CASECONTROL_CONFIDENCEINTERVALUPPER_KEY]
    def set_confidenceIntervalLower(self,x):
        self.data[DMWG_CASECONTROL_CONFIDENCEINTERVALLOWER_KEY] = x
    def get_confidenceIntervalLower(self):
        return self.data[DMWG_CASECONTROL_CONFIDENCEINTERVALLOWER_KEY]

class Locus(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_LOCUS_TYPE 
    def set_referenceSequence(self,x):
        self.data[DMWG_LOCUS_REFERENCESEQUENCE_KEY] = x
    def get_referenceSequence(self):
        return self.data[DMWG_LOCUS_REFERENCESEQUENCE_KEY]
    def set_start(self,x):
        self.data[DMWG_LOCUS_START_KEY] = x
    def get_start(self):
        return self.data[DMWG_LOCUS_START_KEY]
    def set_stop(self,x):
        self.data[DMWG_LOCUS_STOP_KEY] = x
    def get_stop(self):
        return self.data[DMWG_LOCUS_STOP_KEY]

class AlleleFrequency(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELEFREQUENCY_TYPE 
    def set_alleleCount(self,x):
        self.data[DMWG_ALLELEFREQUENCY_ALLELECOUNT_KEY] = x
    def get_alleleCount(self):
        return self.data[DMWG_ALLELEFREQUENCY_ALLELECOUNT_KEY]
    def set_alleleNumber(self,x):
        self.data[DMWG_ALLELEFREQUENCY_ALLELENUMBER_KEY] = x
    def get_alleleNumber(self):
        return self.data[DMWG_ALLELEFREQUENCY_ALLELENUMBER_KEY]
    @get_factory_concept('VS023')
    def set_ascertainment(self,x):
        self.data[DMWG_ALLELEFREQUENCY_ASCERTAINMENT_KEY] = x
    def get_ascertainment(self):
        return self.data[DMWG_ALLELEFREQUENCY_ASCERTAINMENT_KEY]
    def set_allele(self,x):
        self.data[DMWG_ALLELEFREQUENCY_ALLELE_KEY] = x
    def get_allele(self):
        return self.data[DMWG_ALLELEFREQUENCY_ALLELE_KEY]
    def set_hemizygousAlleleIndividualCount(self,x):
        self.data[DMWG_ALLELEFREQUENCY_HEMIZYGOUSALLELEINDIVIDUALCOUNT_KEY] = x
    def get_hemizygousAlleleIndividualCount(self):
        return self.data[DMWG_ALLELEFREQUENCY_HEMIZYGOUSALLELEINDIVIDUALCOUNT_KEY]
    @get_factory_concept('VS013')
    def set_population(self,x):
        self.data[DMWG_ALLELEFREQUENCY_POPULATION_KEY] = x
    def get_population(self):
        return self.data[DMWG_ALLELEFREQUENCY_POPULATION_KEY]
    def set_heterozygousAlleleIndividualCount(self,x):
        self.data[DMWG_ALLELEFREQUENCY_HETEROZYGOUSALLELEINDIVIDUALCOUNT_KEY] = x
    def get_heterozygousAlleleIndividualCount(self):
        return self.data[DMWG_ALLELEFREQUENCY_HETEROZYGOUSALLELEINDIVIDUALCOUNT_KEY]
    def set_homozygousAlleleIndividualCount(self,x):
        self.data[DMWG_ALLELEFREQUENCY_HOMOZYGOUSALLELEINDIVIDUALCOUNT_KEY] = x
    def get_homozygousAlleleIndividualCount(self):
        return self.data[DMWG_ALLELEFREQUENCY_HOMOZYGOUSALLELEINDIVIDUALCOUNT_KEY]
    def set_individualCount(self,x):
        self.data[DMWG_ALLELEFREQUENCY_INDIVIDUALCOUNT_KEY] = x
    def get_individualCount(self):
        return self.data[DMWG_ALLELEFREQUENCY_INDIVIDUALCOUNT_KEY]
    def set_alleleFrequency(self,x):
        self.data[DMWG_ALLELEFREQUENCY_ALLELEFREQUENCY_KEY] = x
    def get_alleleFrequency(self):
        return self.data[DMWG_ALLELEFREQUENCY_ALLELEFREQUENCY_KEY]
    def set_medianCoverage(self,x):
        self.data[DMWG_ALLELEFREQUENCY_MEDIANCOVERAGE_KEY] = x
    def get_medianCoverage(self):
        return self.data[DMWG_ALLELEFREQUENCY_MEDIANCOVERAGE_KEY]

class MolecularConsequence(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_MOLECULARCONSEQUENCE_TYPE 
    def set_lof(self,x):
        self.data[DMWG_MOLECULARCONSEQUENCE_LOF_KEY] = x
    def get_lof(self):
        return self.data[DMWG_MOLECULARCONSEQUENCE_LOF_KEY]
    def set_contextualAllele(self,x):
        self.data[DMWG_MOLECULARCONSEQUENCE_CONTEXTUALALLELE_KEY] = x
    def get_contextualAllele(self):
        return self.data[DMWG_MOLECULARCONSEQUENCE_CONTEXTUALALLELE_KEY]
    @get_factory_concept('VS002')
    def set_consequence(self,x):
        self.data[DMWG_MOLECULARCONSEQUENCE_CONSEQUENCE_KEY] = x
    def get_consequence(self):
        return self.data[DMWG_MOLECULARCONSEQUENCE_CONSEQUENCE_KEY]

class ConditionMechanism(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONDITIONMECHANISM_TYPE 
    def set_gene(self,x):
        self.data[DMWG_CONDITIONMECHANISM_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_CONDITIONMECHANISM_GENE_KEY]
    def set_condition(self,x):
        self.data[DMWG_CONDITIONMECHANISM_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[DMWG_CONDITIONMECHANISM_CONDITION_KEY]
    @get_factory_coding('VS016')
    def set_mechanismConfidence(self,x):
        self.data[DMWG_CONDITIONMECHANISM_MECHANISMCONFIDENCE_KEY] = x
    def get_mechanismConfidence(self):
        return self.data[DMWG_CONDITIONMECHANISM_MECHANISMCONFIDENCE_KEY]
    @get_factory_coding('VS009')
    def set_mechanism(self,x):
        self.data[DMWG_CONDITIONMECHANISM_MECHANISM_KEY] = x
    def get_mechanism(self):
        return self.data[DMWG_CONDITIONMECHANISM_MECHANISM_KEY]

class IndividualAllele(Information):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INDIVIDUALALLELE_TYPE 
    @get_factory_coding('VS005')
    def set_phase(self,x):
        self.data[DMWG_INDIVIDUALALLELE_PHASE_KEY] = x
    def get_phase(self):
        return self.data[DMWG_INDIVIDUALALLELE_PHASE_KEY]
    @get_factory_coding('VS006')
    def set_secondaryZygosity(self,x):
        self.data[DMWG_INDIVIDUALALLELE_SECONDARYZYGOSITY_KEY] = x
    def get_secondaryZygosity(self):
        return self.data[DMWG_INDIVIDUALALLELE_SECONDARYZYGOSITY_KEY]
    @get_factory_coding('VS006')
    def set_primaryZygosity(self,x):
        self.data[DMWG_INDIVIDUALALLELE_PRIMARYZYGOSITY_KEY] = x
    def get_primaryZygosity(self):
        return self.data[DMWG_INDIVIDUALALLELE_PRIMARYZYGOSITY_KEY]
    def set_individual(self,x):
        self.data[DMWG_INDIVIDUALALLELE_INDIVIDUAL_KEY] = x
    def get_individual(self):
        return self.data[DMWG_INDIVIDUALALLELE_INDIVIDUAL_KEY]
    def set_secondaryAllele(self,x):
        self.data[DMWG_INDIVIDUALALLELE_SECONDARYALLELE_KEY] = x
    def get_secondaryAllele(self):
        return self.data[DMWG_INDIVIDUALALLELE_SECONDARYALLELE_KEY]
    def set_primaryAllele(self,x):
        self.data[DMWG_INDIVIDUALALLELE_PRIMARYALLELE_KEY] = x
    def get_primaryAllele(self):
        return self.data[DMWG_INDIVIDUALALLELE_PRIMARYALLELE_KEY]

