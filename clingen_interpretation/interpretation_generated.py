from interpretation_constants import *
from domain_entity_factory import get_factory_entity
from node import Node

from domain_entity_factory import get_factory_entity
class Contribution(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONTRIBUTION_TYPE 
    def set_agent(self,x):
        self.data[DMWG_CONTRIBUTION_AGENT_KEY] = x
    def get_agent(self):
        return self.data[DMWG_CONTRIBUTION_AGENT_KEY]
    def set_contributionDate(self,x):
        self.data[DMWG_CONTRIBUTION_CONTRIBUTIONDATE_KEY] = x
    def get_contributionDate(self):
        return self.data[DMWG_CONTRIBUTION_CONTRIBUTIONDATE_KEY]
    @get_factory_entity('ContributoryRole')
    def set_contributionRole(self,x):
        self.data[DMWG_CONTRIBUTION_CONTRIBUTIONROLE_KEY] = x
    def get_contributionRole(self):
        return self.data[DMWG_CONTRIBUTION_CONTRIBUTIONROLE_KEY]

class Example(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_EXAMPLE_TYPE 
    def set_informationId(self,x):
        self.data[DMWG_EXAMPLE_INFORMATIONID_KEY] = x
    def get_informationId(self):
        return self.data[DMWG_EXAMPLE_INFORMATIONID_KEY]
    def set_searchTags(self,x):
        self.data[DMWG_EXAMPLE_SEARCHTAGS_KEY] = x
    def get_searchTags(self):
        return self.data[DMWG_EXAMPLE_SEARCHTAGS_KEY]
    def set_index(self,x):
        self.data[DMWG_EXAMPLE_INDEX_KEY] = x
    def get_index(self):
        return self.data[DMWG_EXAMPLE_INDEX_KEY]
    def set_author(self,x):
        self.data[DMWG_EXAMPLE_AUTHOR_KEY] = x
    def get_author(self):
        return self.data[DMWG_EXAMPLE_AUTHOR_KEY]
    def set_description(self,x):
        self.data[DMWG_EXAMPLE_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_EXAMPLE_DESCRIPTION_KEY]
    def set_image(self,x):
        self.data[DMWG_EXAMPLE_IMAGE_KEY] = x
    def get_image(self):
        return self.data[DMWG_EXAMPLE_IMAGE_KEY]

class Agent(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_AGENT_TYPE 
    def set_label(self,x):
        self.data[DMWG_AGENT_LABEL_KEY] = x
    def get_label(self):
        return self.data[DMWG_AGENT_LABEL_KEY]
    def set_description(self,x):
        self.data[DMWG_AGENT_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_AGENT_DESCRIPTION_KEY]

class GeneticCondition(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_GENETICCONDITION_TYPE 
    def set_name(self,x):
        self.data[DMWG_GENETICCONDITION_NAME_KEY] = x
    def get_name(self):
        return self.data[DMWG_GENETICCONDITION_NAME_KEY]
    @get_factory_entity('Disease')
    def add_disease(self,x):
        if not DMWG_GENETICCONDITION_DISEASE_KEY in self.data:
            self.data[DMWG_GENETICCONDITION_DISEASE_KEY] = []
        self.data[DMWG_GENETICCONDITION_DISEASE_KEY].append( x ) 
    def get_disease(self):
        return self.data[DMWG_GENETICCONDITION_DISEASE_KEY]
    @get_factory_entity('Phenotype')
    def add_phenotype(self,x):
        if not DMWG_GENETICCONDITION_PHENOTYPE_KEY in self.data:
            self.data[DMWG_GENETICCONDITION_PHENOTYPE_KEY] = []
        self.data[DMWG_GENETICCONDITION_PHENOTYPE_KEY].append( x ) 
    def get_phenotype(self):
        return self.data[DMWG_GENETICCONDITION_PHENOTYPE_KEY]
    @get_factory_entity('ModeOfInheritance')
    def set_modeOfInheritance(self,x):
        self.data[DMWG_GENETICCONDITION_MODEOFINHERITANCE_KEY] = x
    def get_modeOfInheritance(self):
        return self.data[DMWG_GENETICCONDITION_MODEOFINHERITANCE_KEY]
    @get_factory_entity('Gene')
    def set_gene(self,x):
        self.data[DMWG_GENETICCONDITION_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_GENETICCONDITION_GENE_KEY]

class ValueSet(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_VALUESET_TYPE 
    def set_label(self,x):
        self.data[DMWG_VALUESET_LABEL_KEY] = x
    def get_label(self):
        return self.data[DMWG_VALUESET_LABEL_KEY]
    def set_description(self,x):
        self.data[DMWG_VALUESET_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_VALUESET_DESCRIPTION_KEY]
    def set_conceptListExtensibility(self,x):
        self.data[DMWG_VALUESET_CONCEPTLISTEXTENSIBILITY_KEY] = x
    def get_conceptListExtensibility(self):
        return self.data[DMWG_VALUESET_CONCEPTLISTEXTENSIBILITY_KEY]
    @get_factory_entity('IdentifierSystem')
    def add_sourceIdentifierSystems(self,x):
        if not DMWG_VALUESET_SOURCEIDENTIFIERSYSTEMS_KEY in self.data:
            self.data[DMWG_VALUESET_SOURCEIDENTIFIERSYSTEMS_KEY] = []
        self.data[DMWG_VALUESET_SOURCEIDENTIFIERSYSTEMS_KEY].append( x ) 
    def get_sourceIdentifierSystems(self):
        return self.data[DMWG_VALUESET_SOURCEIDENTIFIERSYSTEMS_KEY]
    @get_factory_entity('DomainEntity')
    def add_concept(self,x):
        if not DMWG_VALUESET_CONCEPT_KEY in self.data:
            self.data[DMWG_VALUESET_CONCEPT_KEY] = []
        self.data[DMWG_VALUESET_CONCEPT_KEY].append( x ) 
    def get_concept(self):
        return self.data[DMWG_VALUESET_CONCEPT_KEY]

class EvidenceLine(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_EVIDENCELINE_TYPE 
    def set_description(self,x):
        self.data[DMWG_EVIDENCELINE_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_EVIDENCELINE_DESCRIPTION_KEY]
    @get_factory_entity('EvidenceLineStrength')
    def set_evidenceStrength(self,x):
        self.data[DMWG_EVIDENCELINE_EVIDENCESTRENGTH_KEY] = x
    def get_evidenceStrength(self):
        return self.data[DMWG_EVIDENCELINE_EVIDENCESTRENGTH_KEY]
    def add_evidenceItem(self,x):
        if not DMWG_EVIDENCELINE_EVIDENCEITEM_KEY in self.data:
            self.data[DMWG_EVIDENCELINE_EVIDENCEITEM_KEY] = []
        self.data[DMWG_EVIDENCELINE_EVIDENCEITEM_KEY].append( x ) 
    def get_evidenceItem(self):
        return self.data[DMWG_EVIDENCELINE_EVIDENCEITEM_KEY]
    def add_contribution(self,x):
        if not DMWG_EVIDENCELINE_CONTRIBUTION_KEY in self.data:
            self.data[DMWG_EVIDENCELINE_CONTRIBUTION_KEY] = []
        self.data[DMWG_EVIDENCELINE_CONTRIBUTION_KEY].append( x ) 
    def get_contribution(self):
        return self.data[DMWG_EVIDENCELINE_CONTRIBUTION_KEY]

class ContextualAllele(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONTEXTUALALLELE_TYPE 
    def set_relatedCanonicalAllele(self,x):
        self.data[DMWG_CONTEXTUALALLELE_RELATEDCANONICALALLELE_KEY] = x
    def get_relatedCanonicalAllele(self):
        return self.data[DMWG_CONTEXTUALALLELE_RELATEDCANONICALALLELE_KEY]
    def set_alleleName(self,x):
        self.data[DMWG_CONTEXTUALALLELE_ALLELENAME_KEY] = x
    def get_alleleName(self):
        return self.data[DMWG_CONTEXTUALALLELE_ALLELENAME_KEY]
    def add_legacyNames(self,x):
        if not DMWG_CONTEXTUALALLELE_LEGACYNAMES_KEY in self.data:
            self.data[DMWG_CONTEXTUALALLELE_LEGACYNAMES_KEY] = []
        self.data[DMWG_CONTEXTUALALLELE_LEGACYNAMES_KEY].append( x ) 
    def get_legacyNames(self):
        return self.data[DMWG_CONTEXTUALALLELE_LEGACYNAMES_KEY]
    def add_produces(self,x):
        if not DMWG_CONTEXTUALALLELE_PRODUCES_KEY in self.data:
            self.data[DMWG_CONTEXTUALALLELE_PRODUCES_KEY] = []
        self.data[DMWG_CONTEXTUALALLELE_PRODUCES_KEY].append( x ) 
    def get_produces(self):
        return self.data[DMWG_CONTEXTUALALLELE_PRODUCES_KEY]
    def add_producedBy(self,x):
        if not DMWG_CONTEXTUALALLELE_PRODUCEDBY_KEY in self.data:
            self.data[DMWG_CONTEXTUALALLELE_PRODUCEDBY_KEY] = []
        self.data[DMWG_CONTEXTUALALLELE_PRODUCEDBY_KEY].append( x ) 
    def get_producedBy(self):
        return self.data[DMWG_CONTEXTUALALLELE_PRODUCEDBY_KEY]

class CanonicalAllele(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CANONICALALLELE_TYPE 
    def set_preferredCtxAllele(self,x):
        self.data[DMWG_CANONICALALLELE_PREFERREDCTXALLELE_KEY] = x
    def get_preferredCtxAllele(self):
        return self.data[DMWG_CANONICALALLELE_PREFERREDCTXALLELE_KEY]

class Statement(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_STATEMENT_TYPE 
    def set_qualifier(self,x):
        self.data[DMWG_A004_QUALIFIER_KEY] = x
    def get_qualifier(self):
        return self.data[DMWG_A004_QUALIFIER_KEY]
    def add_evidenceLine(self,x):
        if not DMWG_STATEMENT_EVIDENCELINE_KEY in self.data:
            self.data[DMWG_STATEMENT_EVIDENCELINE_KEY] = []
        self.data[DMWG_STATEMENT_EVIDENCELINE_KEY].append( x ) 
    def get_evidenceLine(self):
        return self.data[DMWG_STATEMENT_EVIDENCELINE_KEY]
    def set_description(self,x):
        self.data[DMWG_STATEMENT_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_STATEMENT_DESCRIPTION_KEY]
    def add_contribution(self,x):
        if not DMWG_STATEMENT_CONTRIBUTION_KEY in self.data:
            self.data[DMWG_STATEMENT_CONTRIBUTION_KEY] = []
        self.data[DMWG_STATEMENT_CONTRIBUTION_KEY].append( x ) 
    def get_contribution(self):
        return self.data[DMWG_STATEMENT_CONTRIBUTION_KEY]
    def add_source(self,x):
        if not DMWG_STATEMENT_SOURCE_KEY in self.data:
            self.data[DMWG_STATEMENT_SOURCE_KEY] = []
        self.data[DMWG_STATEMENT_SOURCE_KEY].append( x ) 
    def get_source(self):
        return self.data[DMWG_STATEMENT_SOURCE_KEY]

class IndividualAlleleInheritance(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INDIVIDUALALLELEINHERITANCE_TYPE 
    def set_canonicalAllele(self,x):
        self.data[DMWG_INDIVIDUALALLELEINHERITANCE_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_INDIVIDUALALLELEINHERITANCE_CANONICALALLELE_KEY]
    @get_factory_entity('Individual')
    def set_individual(self,x):
        self.data[DMWG_INDIVIDUALALLELEINHERITANCE_INDIVIDUAL_KEY] = x
    def get_individual(self):
        return self.data[DMWG_INDIVIDUALALLELEINHERITANCE_INDIVIDUAL_KEY]
    @get_factory_entity('AlleleInheritance')
    def add_alleleInheritance(self,x):
        if not DMWG_INDIVIDUALALLELEINHERITANCE_ALLELEINHERITANCE_KEY in self.data:
            self.data[DMWG_INDIVIDUALALLELEINHERITANCE_ALLELEINHERITANCE_KEY] = []
        self.data[DMWG_INDIVIDUALALLELEINHERITANCE_ALLELEINHERITANCE_KEY].append( x ) 
    def get_alleleInheritance(self):
        return self.data[DMWG_INDIVIDUALALLELEINHERITANCE_ALLELEINHERITANCE_KEY]
    @get_factory_entity('ParentalConfirmation')
    def set_parentalConfirmation(self,x):
        self.data[DMWG_INDIVIDUALALLELEINHERITANCE_PARENTALCONFIRMATION_KEY] = x
    def get_parentalConfirmation(self):
        return self.data[DMWG_INDIVIDUALALLELEINHERITANCE_PARENTALCONFIRMATION_KEY]

class FamilyCondition(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_FAMILYCONDITION_TYPE 
    @get_factory_entity('Individual')
    def set_proband(self,x):
        self.data[DMWG_FAMILYCONDITION_PROBAND_KEY] = x
    def get_proband(self):
        return self.data[DMWG_FAMILYCONDITION_PROBAND_KEY]
    def add_condition(self,x):
        if not DMWG_FAMILYCONDITION_CONDITION_KEY in self.data:
            self.data[DMWG_FAMILYCONDITION_CONDITION_KEY] = []
        self.data[DMWG_FAMILYCONDITION_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_FAMILYCONDITION_CONDITION_KEY]
    @get_factory_entity('ConditionStatus')
    def set_familyHasCondition(self,x):
        self.data[DMWG_FAMILYCONDITION_FAMILYHASCONDITION_KEY] = x
    def get_familyHasCondition(self):
        return self.data[DMWG_FAMILYCONDITION_FAMILYHASCONDITION_KEY]

class VariantInterpretation(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_VARIANTINTERPRETATION_TYPE 
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
    @get_factory_entity('Significance')
    def set_outcome(self,x):
        self.data[DMWG_VARIANTINTERPRETATION_OUTCOME_KEY] = x
    def get_outcome(self):
        return self.data[DMWG_VARIANTINTERPRETATION_OUTCOME_KEY]
    @get_factory_entity('AssertionMethod')
    def set_assertionMethod(self,x):
        self.data[DMWG_VARIANTINTERPRETATION_ASSERTIONMETHOD_KEY] = x
    def get_assertionMethod(self):
        return self.data[DMWG_VARIANTINTERPRETATION_ASSERTIONMETHOD_KEY]

class IndividualCondition(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INDIVIDUALCONDITION_TYPE 
    @get_factory_entity('Individual')
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
    @get_factory_entity('ConditionStatus')
    def set_individualHasCondition(self,x):
        self.data[DMWG_INDIVIDUALCONDITION_INDIVIDUALHASCONDITION_KEY] = x
    def get_individualHasCondition(self):
        return self.data[DMWG_INDIVIDUALCONDITION_INDIVIDUALHASCONDITION_KEY]

class LocusHeterogeneity(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_LOCUSHETEROGENEITY_TYPE 
    def set_condition(self,x):
        self.data[DMWG_LOCUSHETEROGENEITY_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[DMWG_LOCUSHETEROGENEITY_CONDITION_KEY]
    @get_factory_entity('Gene')
    def set_gene(self,x):
        self.data[DMWG_LOCUSHETEROGENEITY_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_LOCUSHETEROGENEITY_GENE_KEY]
    @get_factory_entity('LocusSpecificity')
    def set_specificity(self,x):
        self.data[DMWG_LOCUSHETEROGENEITY_SPECIFICITY_KEY] = x
    def get_specificity(self):
        return self.data[DMWG_LOCUSHETEROGENEITY_SPECIFICITY_KEY]

class AggregateSegregation(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_AGGREGATESEGREGATION_TYPE 
    def set_canonicalAllele(self,x):
        self.data[DMWG_AGGREGATESEGREGATION_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_AGGREGATESEGREGATION_CANONICALALLELE_KEY]
    def set_condition(self,x):
        self.data[DMWG_AGGREGATESEGREGATION_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[DMWG_AGGREGATESEGREGATION_CONDITION_KEY]
    def set_totalNumberOfSegregations(self,x):
        self.data[DMWG_AGGREGATESEGREGATION_TOTALNUMBEROFSEGREGATIONS_KEY] = x
    def get_totalNumberOfSegregations(self):
        return self.data[DMWG_AGGREGATESEGREGATION_TOTALNUMBEROFSEGREGATIONS_KEY]
    def add_familySegregation(self,x):
        if not DMWG_AGGREGATESEGREGATION_FAMILYSEGREGATION_KEY in self.data:
            self.data[DMWG_AGGREGATESEGREGATION_FAMILYSEGREGATION_KEY] = []
        self.data[DMWG_AGGREGATESEGREGATION_FAMILYSEGREGATION_KEY].append( x ) 
    def get_familySegregation(self):
        return self.data[DMWG_AGGREGATESEGREGATION_FAMILYSEGREGATION_KEY]
    @get_factory_entity('ModeOfInheritance')
    def set_modeOfInheritance(self,x):
        self.data[DMWG_AGGREGATESEGREGATION_MODEOFINHERITANCE_KEY] = x
    def get_modeOfInheritance(self):
        return self.data[DMWG_AGGREGATESEGREGATION_MODEOFINHERITANCE_KEY]
    def set_totalOfAllelePosConditionPosIndividuals(self,x):
        self.data[DMWG_AGGREGATESEGREGATION_TOTALOFALLELEPOSCONDITIONPOSINDIVIDUALS_KEY] = x
    def get_totalOfAllelePosConditionPosIndividuals(self):
        return self.data[DMWG_AGGREGATESEGREGATION_TOTALOFALLELEPOSCONDITIONPOSINDIVIDUALS_KEY]
    def set_totalOfAlleleNegConditionNegIndividuals(self,x):
        self.data[DMWG_AGGREGATESEGREGATION_TOTALOFALLELENEGCONDITIONNEGINDIVIDUALS_KEY] = x
    def get_totalOfAlleleNegConditionNegIndividuals(self):
        return self.data[DMWG_AGGREGATESEGREGATION_TOTALOFALLELENEGCONDITIONNEGINDIVIDUALS_KEY]
    def set_totalOfAllelePosConditionNegIndividuals(self,x):
        self.data[DMWG_AGGREGATESEGREGATION_TOTALOFALLELEPOSCONDITIONNEGINDIVIDUALS_KEY] = x
    def get_totalOfAllelePosConditionNegIndividuals(self):
        return self.data[DMWG_AGGREGATESEGREGATION_TOTALOFALLELEPOSCONDITIONNEGINDIVIDUALS_KEY]
    def set_totalOfAlleleNegConditionPosIndividuals(self,x):
        self.data[DMWG_AGGREGATESEGREGATION_TOTALOFALLELENEGCONDITIONPOSINDIVIDUALS_KEY] = x
    def get_totalOfAlleleNegConditionPosIndividuals(self):
        return self.data[DMWG_AGGREGATESEGREGATION_TOTALOFALLELENEGCONDITIONPOSINDIVIDUALS_KEY]
    def set_totalOfUntestedConditionPosIndividuals(self,x):
        self.data[DMWG_AGGREGATESEGREGATION_TOTALOFUNTESTEDCONDITIONPOSINDIVIDUALS_KEY] = x
    def get_totalOfUntestedConditionPosIndividuals(self):
        return self.data[DMWG_AGGREGATESEGREGATION_TOTALOFUNTESTEDCONDITIONPOSINDIVIDUALS_KEY]
    def set_totalOfUntestedConditionNegIndividuals(self,x):
        self.data[DMWG_AGGREGATESEGREGATION_TOTALOFUNTESTEDCONDITIONNEGINDIVIDUALS_KEY] = x
    def get_totalOfUntestedConditionNegIndividuals(self):
        return self.data[DMWG_AGGREGATESEGREGATION_TOTALOFUNTESTEDCONDITIONNEGINDIVIDUALS_KEY]
    def set_totalOfFamiliesWithInconsistentSegregations(self,x):
        self.data[DMWG_AGGREGATESEGREGATION_TOTALOFFAMILIESWITHINCONSISTENTSEGREGATIONS_KEY] = x
    def get_totalOfFamiliesWithInconsistentSegregations(self):
        return self.data[DMWG_AGGREGATESEGREGATION_TOTALOFFAMILIESWITHINCONSISTENTSEGREGATIONS_KEY]

class AlleleConservation(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELECONSERVATION_TYPE 
    def set_allele(self,x):
        self.data[DMWG_ALLELECONSERVATION_ALLELE_KEY] = x
    def get_allele(self):
        return self.data[DMWG_ALLELECONSERVATION_ALLELE_KEY]
    @get_factory_entity('Conservation')
    def set_conservationType(self,x):
        self.data[DMWG_ALLELECONSERVATION_CONSERVATIONTYPE_KEY] = x
    def get_conservationType(self):
        return self.data[DMWG_ALLELECONSERVATION_CONSERVATIONTYPE_KEY]
    def set_algorithm(self,x):
        self.data[DMWG_ALLELECONSERVATION_ALGORITHM_KEY] = x
    def get_algorithm(self):
        return self.data[DMWG_ALLELECONSERVATION_ALGORITHM_KEY]

class ConditionPenetrance(Statement):
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
    @get_factory_entity('Penetrance')
    def set_penetrance(self,x):
        self.data[DMWG_CONDITIONPENETRANCE_PENETRANCE_KEY] = x
    def get_penetrance(self):
        return self.data[DMWG_CONDITIONPENETRANCE_PENETRANCE_KEY]

class AlleleConservationScore(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELECONSERVATIONSCORE_TYPE 
    def set_allele(self,x):
        self.data[DMWG_ALLELECONSERVATIONSCORE_ALLELE_KEY] = x
    def get_allele(self):
        return self.data[DMWG_ALLELECONSERVATIONSCORE_ALLELE_KEY]
    @get_factory_entity('Conservation')
    def set_conservationType(self,x):
        self.data[DMWG_ALLELECONSERVATIONSCORE_CONSERVATIONTYPE_KEY] = x
    def get_conservationType(self):
        return self.data[DMWG_ALLELECONSERVATIONSCORE_CONSERVATIONTYPE_KEY]
    def set_algorithm(self,x):
        self.data[DMWG_ALLELECONSERVATIONSCORE_ALGORITHM_KEY] = x
    def get_algorithm(self):
        return self.data[DMWG_ALLELECONSERVATIONSCORE_ALGORITHM_KEY]
    def set_score(self,x):
        self.data[DMWG_ALLELECONSERVATIONSCORE_SCORE_KEY] = x
    def get_score(self):
        return self.data[DMWG_ALLELECONSERVATIONSCORE_SCORE_KEY]

class InSilicoPrediction(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INSILICOPREDICTION_TYPE 
    def set_canonicalAllele(self,x):
        self.data[DMWG_INSILICOPREDICTION_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_INSILICOPREDICTION_CANONICALALLELE_KEY]
    @get_factory_entity('ReferenceSequence')
    def set_transcript(self,x):
        self.data[DMWG_INSILICOPREDICTION_TRANSCRIPT_KEY] = x
    def get_transcript(self):
        return self.data[DMWG_INSILICOPREDICTION_TRANSCRIPT_KEY]
    @get_factory_entity('Prediction')
    def set_predictionType(self,x):
        self.data[DMWG_INSILICOPREDICTION_PREDICTIONTYPE_KEY] = x
    def get_predictionType(self):
        return self.data[DMWG_INSILICOPREDICTION_PREDICTIONTYPE_KEY]
    def set_prediction(self,x):
        self.data[DMWG_INSILICOPREDICTION_PREDICTION_KEY] = x
    def get_prediction(self):
        return self.data[DMWG_INSILICOPREDICTION_PREDICTION_KEY]
    def set_algorithm(self,x):
        self.data[DMWG_INSILICOPREDICTION_ALGORITHM_KEY] = x
    def get_algorithm(self):
        return self.data[DMWG_INSILICOPREDICTION_ALGORITHM_KEY]

class SequenceLocation(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_SEQUENCELOCATION_TYPE 
    @get_factory_entity('ReferenceSequence')
    def set_referenceSequence(self,x):
        self.data[DMWG_SEQUENCELOCATION_REFERENCESEQUENCE_KEY] = x
    def get_referenceSequence(self):
        return self.data[DMWG_SEQUENCELOCATION_REFERENCESEQUENCE_KEY]
    def set_start(self,x):
        self.data[DMWG_SEQUENCELOCATION_START_KEY] = x
    def get_start(self):
        return self.data[DMWG_SEQUENCELOCATION_START_KEY]
    def set_stop(self,x):
        self.data[DMWG_SEQUENCELOCATION_STOP_KEY] = x
    def get_stop(self):
        return self.data[DMWG_SEQUENCELOCATION_STOP_KEY]

class CriterionAssessment(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CRITERIONASSESSMENT_TYPE 
    @get_factory_entity('Criterion')
    def set_criterion(self,x):
        self.data[DMWG_CRITERIONASSESSMENT_CRITERION_KEY] = x
    def get_criterion(self):
        return self.data[DMWG_CRITERIONASSESSMENT_CRITERION_KEY]
    def set_variant(self,x):
        self.data[DMWG_CRITERIONASSESSMENT_VARIANT_KEY] = x
    def get_variant(self):
        return self.data[DMWG_CRITERIONASSESSMENT_VARIANT_KEY]
    def add_condition(self,x):
        if not DMWG_CRITERIONASSESSMENT_CONDITION_KEY in self.data:
            self.data[DMWG_CRITERIONASSESSMENT_CONDITION_KEY] = []
        self.data[DMWG_CRITERIONASSESSMENT_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_CRITERIONASSESSMENT_CONDITION_KEY]
    @get_factory_entity('CriterionEvaluation')
    def set_outcome(self,x):
        self.data[DMWG_CRITERIONASSESSMENT_OUTCOME_KEY] = x
    def get_outcome(self):
        return self.data[DMWG_CRITERIONASSESSMENT_OUTCOME_KEY]

class ConditionPrevelance(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONDITIONPREVELANCE_TYPE 
    def add_condition(self,x):
        if not DMWG_CONDITIONPREVELANCE_CONDITION_KEY in self.data:
            self.data[DMWG_CONDITIONPREVELANCE_CONDITION_KEY] = []
        self.data[DMWG_CONDITIONPREVELANCE_CONDITION_KEY].append( x ) 
    def get_condition(self):
        return self.data[DMWG_CONDITIONPREVELANCE_CONDITION_KEY]
    @get_factory_entity('Population')
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
    def set_prevelance(self,x):
        self.data[DMWG_CONDITIONPREVELANCE_PREVELANCE_KEY] = x
    def get_prevelance(self):
        return self.data[DMWG_CONDITIONPREVELANCE_PREVELANCE_KEY]

class InSilicoPredictionScore(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INSILICOPREDICTIONSCORE_TYPE 
    def set_canonicalAllele(self,x):
        self.data[DMWG_INSILICOPREDICTIONSCORE_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_INSILICOPREDICTIONSCORE_CANONICALALLELE_KEY]
    @get_factory_entity('ReferenceSequence')
    def set_transcript(self,x):
        self.data[DMWG_INSILICOPREDICTIONSCORE_TRANSCRIPT_KEY] = x
    def get_transcript(self):
        return self.data[DMWG_INSILICOPREDICTIONSCORE_TRANSCRIPT_KEY]
    @get_factory_entity('Prediction')
    def set_predictionType(self,x):
        self.data[DMWG_INSILICOPREDICTIONSCORE_PREDICTIONTYPE_KEY] = x
    def get_predictionType(self):
        return self.data[DMWG_INSILICOPREDICTIONSCORE_PREDICTIONTYPE_KEY]
    def set_prediction(self,x):
        self.data[DMWG_INSILICOPREDICTIONSCORE_PREDICTION_KEY] = x
    def get_prediction(self):
        return self.data[DMWG_INSILICOPREDICTIONSCORE_PREDICTION_KEY]
    def set_algorithm(self,x):
        self.data[DMWG_INSILICOPREDICTIONSCORE_ALGORITHM_KEY] = x
    def get_algorithm(self):
        return self.data[DMWG_INSILICOPREDICTIONSCORE_ALGORITHM_KEY]

class BenignMissenseVariationRate(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_BENIGNMISSENSEVARIATIONRATE_TYPE 
    def set_region(self,x):
        self.data[DMWG_BENIGNMISSENSEVARIATIONRATE_REGION_KEY] = x
    def get_region(self):
        return self.data[DMWG_BENIGNMISSENSEVARIATIONRATE_REGION_KEY]
    @get_factory_entity('Gene')
    def set_gene(self,x):
        self.data[DMWG_BENIGNMISSENSEVARIATIONRATE_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_BENIGNMISSENSEVARIATIONRATE_GENE_KEY]
    @get_factory_entity('BenignMissenseVariationRateOutcome')
    def set_value(self,x):
        self.data[DMWG_BENIGNMISSENSEVARIATIONRATE_VALUE_KEY] = x
    def get_value(self):
        return self.data[DMWG_BENIGNMISSENSEVARIATIONRATE_VALUE_KEY]

class FamilySegregation(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_FAMILYSEGREGATION_TYPE 
    def set_canonicalAllele(self,x):
        self.data[DMWG_FAMILYSEGREGATION_CANONICALALLELE_KEY] = x
    def get_canonicalAllele(self):
        return self.data[DMWG_FAMILYSEGREGATION_CANONICALALLELE_KEY]
    def set_condition(self,x):
        self.data[DMWG_FAMILYSEGREGATION_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[DMWG_FAMILYSEGREGATION_CONDITION_KEY]
    @get_factory_entity('Family')
    def set_family(self,x):
        self.data[DMWG_FAMILYSEGREGATION_FAMILY_KEY] = x
    def get_family(self):
        return self.data[DMWG_FAMILYSEGREGATION_FAMILY_KEY]
    def set_phenotypePositiveAllelePositive(self,x):
        self.data[DMWG_FAMILYSEGREGATION_PHENOTYPEPOSITIVEALLELEPOSITIVE_KEY] = x
    def get_phenotypePositiveAllelePositive(self):
        return self.data[DMWG_FAMILYSEGREGATION_PHENOTYPEPOSITIVEALLELEPOSITIVE_KEY]
    def set_phenotypePositiveAlleleNegative(self,x):
        self.data[DMWG_FAMILYSEGREGATION_PHENOTYPEPOSITIVEALLELENEGATIVE_KEY] = x
    def get_phenotypePositiveAlleleNegative(self):
        return self.data[DMWG_FAMILYSEGREGATION_PHENOTYPEPOSITIVEALLELENEGATIVE_KEY]
    def set_phenotypeNegativeAllelePositive(self,x):
        self.data[DMWG_FAMILYSEGREGATION_PHENOTYPENEGATIVEALLELEPOSITIVE_KEY] = x
    def get_phenotypeNegativeAllelePositive(self):
        return self.data[DMWG_FAMILYSEGREGATION_PHENOTYPENEGATIVEALLELEPOSITIVE_KEY]
    def set_phenotypeNegativeAlleleNegative(self,x):
        self.data[DMWG_FAMILYSEGREGATION_PHENOTYPENEGATIVEALLELENEGATIVE_KEY] = x
    def get_phenotypeNegativeAlleleNegative(self):
        return self.data[DMWG_FAMILYSEGREGATION_PHENOTYPENEGATIVEALLELENEGATIVE_KEY]
    def add_pedigree(self,x):
        if not DMWG_FAMILYSEGREGATION_PEDIGREE_KEY in self.data:
            self.data[DMWG_FAMILYSEGREGATION_PEDIGREE_KEY] = []
        self.data[DMWG_FAMILYSEGREGATION_PEDIGREE_KEY].append( x ) 
    def get_pedigree(self):
        return self.data[DMWG_FAMILYSEGREGATION_PEDIGREE_KEY]
    def add_columns(self,x):
        if not DMWG_FAMILYSEGREGATION_COLUMNS_KEY in self.data:
            self.data[DMWG_FAMILYSEGREGATION_COLUMNS_KEY] = []
        self.data[DMWG_FAMILYSEGREGATION_COLUMNS_KEY].append( x ) 
    def get_columns(self):
        return self.data[DMWG_FAMILYSEGREGATION_COLUMNS_KEY]
    def add_genotypeValues(self,x):
        if not DMWG_FAMILYSEGREGATION_GENOTYPEVALUES_KEY in self.data:
            self.data[DMWG_FAMILYSEGREGATION_GENOTYPEVALUES_KEY] = []
        self.data[DMWG_FAMILYSEGREGATION_GENOTYPEVALUES_KEY].append( x ) 
    def get_genotypeValues(self):
        return self.data[DMWG_FAMILYSEGREGATION_GENOTYPEVALUES_KEY]
    def add_affectedValues(self,x):
        if not DMWG_FAMILYSEGREGATION_AFFECTEDVALUES_KEY in self.data:
            self.data[DMWG_FAMILYSEGREGATION_AFFECTEDVALUES_KEY] = []
        self.data[DMWG_FAMILYSEGREGATION_AFFECTEDVALUES_KEY].append( x ) 
    def get_affectedValues(self):
        return self.data[DMWG_FAMILYSEGREGATION_AFFECTEDVALUES_KEY]
    @get_factory_entity('InconsistentSegregationObserved')
    def set_inconsistentSegregationsObserved(self,x):
        self.data[DMWG_FAMILYSEGREGATION_INCONSISTENTSEGREGATIONSOBSERVED_KEY] = x
    def get_inconsistentSegregationsObserved(self):
        return self.data[DMWG_FAMILYSEGREGATION_INCONSISTENTSEGREGATIONSOBSERVED_KEY]
    def set_inconsistentSegregationCount(self,x):
        self.data[DMWG_FAMILYSEGREGATION_INCONSISTENTSEGREGATIONCOUNT_KEY] = x
    def get_inconsistentSegregationCount(self):
        return self.data[DMWG_FAMILYSEGREGATION_INCONSISTENTSEGREGATIONCOUNT_KEY]

class RegionType(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REGIONTYPE_TYPE 
    def set_region(self,x):
        self.data[DMWG_REGIONTYPE_REGION_KEY] = x
    def get_region(self):
        return self.data[DMWG_REGIONTYPE_REGION_KEY]
    @get_factory_entity('RegionAnnotation')
    def add_annotation(self,x):
        if not DMWG_REGIONTYPE_ANNOTATION_KEY in self.data:
            self.data[DMWG_REGIONTYPE_ANNOTATION_KEY] = []
        self.data[DMWG_REGIONTYPE_ANNOTATION_KEY].append( x ) 
    def get_annotation(self):
        return self.data[DMWG_REGIONTYPE_ANNOTATION_KEY]

class RegionAlleles(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_REGIONALLELES_TYPE 
    def set_region(self,x):
        self.data[DMWG_REGIONALLELES_REGION_KEY] = x
    def get_region(self):
        return self.data[DMWG_REGIONALLELES_REGION_KEY]
    def add_allele(self,x):
        if not DMWG_REGIONALLELES_ALLELE_KEY in self.data:
            self.data[DMWG_REGIONALLELES_ALLELE_KEY] = []
        self.data[DMWG_REGIONALLELES_ALLELE_KEY].append( x ) 
    def get_allele(self):
        return self.data[DMWG_REGIONALLELES_ALLELE_KEY]
    @get_factory_entity('RegionAllelesOutcome')
    def set_outcome(self,x):
        self.data[DMWG_REGIONALLELES_OUTCOME_KEY] = x
    def get_outcome(self):
        return self.data[DMWG_REGIONALLELES_OUTCOME_KEY]

class AlleleFunctionalImpact(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELEFUNCTIONALIMPACT_TYPE 
    def set_contextualAllele(self,x):
        self.data[DMWG_ALLELEFUNCTIONALIMPACT_CONTEXTUALALLELE_KEY] = x
    def get_contextualAllele(self):
        return self.data[DMWG_ALLELEFUNCTIONALIMPACT_CONTEXTUALALLELE_KEY]
    @get_factory_entity('Gene')
    def set_gene(self,x):
        self.data[DMWG_ALLELEFUNCTIONALIMPACT_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_ALLELEFUNCTIONALIMPACT_GENE_KEY]
    def set_resultDescription(self,x):
        self.data[DMWG_ALLELEFUNCTIONALIMPACT_RESULTDESCRIPTION_KEY] = x
    def get_resultDescription(self):
        return self.data[DMWG_ALLELEFUNCTIONALIMPACT_RESULTDESCRIPTION_KEY]
    @get_factory_entity('AlleleFunctionalAssayMethod')
    def set_assayType(self,x):
        self.data[DMWG_ALLELEFUNCTIONALIMPACT_ASSAYTYPE_KEY] = x
    def get_assayType(self):
        return self.data[DMWG_ALLELEFUNCTIONALIMPACT_ASSAYTYPE_KEY]

class CaseControl(Statement):
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
    def set_caseGroupFrequency(self,x):
        self.data[DMWG_CASECONTROL_CASEGROUPFREQUENCY_KEY] = x
    def get_caseGroupFrequency(self):
        return self.data[DMWG_CASECONTROL_CASEGROUPFREQUENCY_KEY]
    def set_controlGroupFrequency(self,x):
        self.data[DMWG_CASECONTROL_CONTROLGROUPFREQUENCY_KEY] = x
    def get_controlGroupFrequency(self):
        return self.data[DMWG_CASECONTROL_CONTROLGROUPFREQUENCY_KEY]
    def set_oddsRatio(self,x):
        self.data[DMWG_CASECONTROL_ODDSRATIO_KEY] = x
    def get_oddsRatio(self):
        return self.data[DMWG_CASECONTROL_ODDSRATIO_KEY]
    def set_confidenceLevel(self,x):
        self.data[DMWG_CASECONTROL_CONFIDENCELEVEL_KEY] = x
    def get_confidenceLevel(self):
        return self.data[DMWG_CASECONTROL_CONFIDENCELEVEL_KEY]
    def set_confidenceIntervalLower(self,x):
        self.data[DMWG_CASECONTROL_CONFIDENCEINTERVALLOWER_KEY] = x
    def get_confidenceIntervalLower(self):
        return self.data[DMWG_CASECONTROL_CONFIDENCEINTERVALLOWER_KEY]
    def set_confidenceIntervalUpper(self,x):
        self.data[DMWG_CASECONTROL_CONFIDENCEINTERVALUPPER_KEY] = x
    def get_confidenceIntervalUpper(self):
        return self.data[DMWG_CASECONTROL_CONFIDENCEINTERVALUPPER_KEY]

class NullAllele(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_NULLALLELE_TYPE 
    def set_contextualAllele(self,x):
        self.data[DMWG_NULLALLELE_CONTEXTUALALLELE_KEY] = x
    def get_contextualAllele(self):
        return self.data[DMWG_NULLALLELE_CONTEXTUALALLELE_KEY]
    @get_factory_entity('NullAlleleOutcome')
    def set_annotation(self,x):
        self.data[DMWG_NULLALLELE_ANNOTATION_KEY] = x
    def get_annotation(self):
        return self.data[DMWG_NULLALLELE_ANNOTATION_KEY]

class AlleleFrequency(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELEFREQUENCY_TYPE 
    def set_allele(self,x):
        self.data[DMWG_ALLELEFREQUENCY_ALLELE_KEY] = x
    def get_allele(self):
        return self.data[DMWG_ALLELEFREQUENCY_ALLELE_KEY]
    @get_factory_entity('Population')
    def set_population(self,x):
        self.data[DMWG_ALLELEFREQUENCY_POPULATION_KEY] = x
    def get_population(self):
        return self.data[DMWG_ALLELEFREQUENCY_POPULATION_KEY]
    @get_factory_entity('Ascertainment')
    def set_ascertainment(self,x):
        self.data[DMWG_ALLELEFREQUENCY_ASCERTAINMENT_KEY] = x
    def get_ascertainment(self):
        return self.data[DMWG_ALLELEFREQUENCY_ASCERTAINMENT_KEY]
    def set_alleleFrequency(self,x):
        self.data[DMWG_ALLELEFREQUENCY_ALLELEFREQUENCY_KEY] = x
    def get_alleleFrequency(self):
        return self.data[DMWG_ALLELEFREQUENCY_ALLELEFREQUENCY_KEY]
    def set_alleleCount(self,x):
        self.data[DMWG_ALLELEFREQUENCY_ALLELECOUNT_KEY] = x
    def get_alleleCount(self):
        return self.data[DMWG_ALLELEFREQUENCY_ALLELECOUNT_KEY]
    def set_alleleNumber(self,x):
        self.data[DMWG_ALLELEFREQUENCY_ALLELENUMBER_KEY] = x
    def get_alleleNumber(self):
        return self.data[DMWG_ALLELEFREQUENCY_ALLELENUMBER_KEY]
    def set_individualCount(self,x):
        self.data[DMWG_ALLELEFREQUENCY_INDIVIDUALCOUNT_KEY] = x
    def get_individualCount(self):
        return self.data[DMWG_ALLELEFREQUENCY_INDIVIDUALCOUNT_KEY]
    def set_homozygousAlleleIndividualCount(self,x):
        self.data[DMWG_ALLELEFREQUENCY_HOMOZYGOUSALLELEINDIVIDUALCOUNT_KEY] = x
    def get_homozygousAlleleIndividualCount(self):
        return self.data[DMWG_ALLELEFREQUENCY_HOMOZYGOUSALLELEINDIVIDUALCOUNT_KEY]
    def set_heterozygousAlleleIndividualCount(self,x):
        self.data[DMWG_ALLELEFREQUENCY_HETEROZYGOUSALLELEINDIVIDUALCOUNT_KEY] = x
    def get_heterozygousAlleleIndividualCount(self):
        return self.data[DMWG_ALLELEFREQUENCY_HETEROZYGOUSALLELEINDIVIDUALCOUNT_KEY]
    def set_hemizygousAlleleIndividualCount(self,x):
        self.data[DMWG_ALLELEFREQUENCY_HEMIZYGOUSALLELEINDIVIDUALCOUNT_KEY] = x
    def get_hemizygousAlleleIndividualCount(self):
        return self.data[DMWG_ALLELEFREQUENCY_HEMIZYGOUSALLELEINDIVIDUALCOUNT_KEY]
    def set_medianCoverage(self,x):
        self.data[DMWG_ALLELEFREQUENCY_MEDIANCOVERAGE_KEY] = x
    def get_medianCoverage(self):
        return self.data[DMWG_ALLELEFREQUENCY_MEDIANCOVERAGE_KEY]

class AlleleMolecularConsequence(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_ALLELEMOLECULARCONSEQUENCE_TYPE 
    def set_contextualAllele(self,x):
        self.data[DMWG_ALLELEMOLECULARCONSEQUENCE_CONTEXTUALALLELE_KEY] = x
    def get_contextualAllele(self):
        return self.data[DMWG_ALLELEMOLECULARCONSEQUENCE_CONTEXTUALALLELE_KEY]
    @get_factory_entity('MolecularConsequence')
    def set_consequence(self,x):
        self.data[DMWG_ALLELEMOLECULARCONSEQUENCE_CONSEQUENCE_KEY] = x
    def get_consequence(self):
        return self.data[DMWG_ALLELEMOLECULARCONSEQUENCE_CONSEQUENCE_KEY]

class ConditionMechanism(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CONDITIONMECHANISM_TYPE 
    def set_condition(self,x):
        self.data[DMWG_CONDITIONMECHANISM_CONDITION_KEY] = x
    def get_condition(self):
        return self.data[DMWG_CONDITIONMECHANISM_CONDITION_KEY]
    @get_factory_entity('Gene')
    def set_gene(self,x):
        self.data[DMWG_CONDITIONMECHANISM_GENE_KEY] = x
    def get_gene(self):
        return self.data[DMWG_CONDITIONMECHANISM_GENE_KEY]
    @get_factory_entity('Mechanism')
    def set_mechanism(self,x):
        self.data[DMWG_CONDITIONMECHANISM_MECHANISM_KEY] = x
    def get_mechanism(self):
        return self.data[DMWG_CONDITIONMECHANISM_MECHANISM_KEY]
    @get_factory_entity('ConditionMechanismStrength')
    def set_mechanismConfidence(self,x):
        self.data[DMWG_CONDITIONMECHANISM_MECHANISMCONFIDENCE_KEY] = x
    def get_mechanismConfidence(self):
        return self.data[DMWG_CONDITIONMECHANISM_MECHANISMCONFIDENCE_KEY]

class IndividualGenotype(Statement):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_INDIVIDUALGENOTYPE_TYPE 
    @get_factory_entity('Individual')
    def set_individual(self,x):
        self.data[DMWG_INDIVIDUALGENOTYPE_INDIVIDUAL_KEY] = x
    def get_individual(self):
        return self.data[DMWG_INDIVIDUALGENOTYPE_INDIVIDUAL_KEY]
    @get_factory_entity('Genotype')
    def add_genotype(self,x):
        if not DMWG_INDIVIDUALGENOTYPE_GENOTYPE_KEY in self.data:
            self.data[DMWG_INDIVIDUALGENOTYPE_GENOTYPE_KEY] = []
        self.data[DMWG_INDIVIDUALGENOTYPE_GENOTYPE_KEY].append( x ) 
    def get_genotype(self):
        return self.data[DMWG_INDIVIDUALGENOTYPE_GENOTYPE_KEY]

class UserLabel(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_USERLABEL_TYPE 
    def set_label(self,x):
        self.data[DMWG_USERLABEL_LABEL_KEY] = x
    def get_label(self):
        return self.data[DMWG_USERLABEL_LABEL_KEY]
    def set_description(self,x):
        self.data[DMWG_USERLABEL_DESCRIPTION_KEY] = x
    def get_description(self):
        return self.data[DMWG_USERLABEL_DESCRIPTION_KEY]
    def add_contribution(self,x):
        if not DMWG_USERLABEL_CONTRIBUTION_KEY in self.data:
            self.data[DMWG_USERLABEL_CONTRIBUTION_KEY] = []
        self.data[DMWG_USERLABEL_CONTRIBUTION_KEY].append( x ) 
    def get_contribution(self):
        return self.data[DMWG_USERLABEL_CONTRIBUTION_KEY]
    def set_comments(self,x):
        self.data[DMWG_USERLABEL_COMMENTS_KEY] = x
    def get_comments(self):
        return self.data[DMWG_USERLABEL_COMMENTS_KEY]

