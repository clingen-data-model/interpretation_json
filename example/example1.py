from clingen_interpretation.interpretation_generated import *
from clingen_interpretation.interpretation_extras import *
from clingen_interpretation.interpretation_constants import *
from clingen_interpretation.Allele import CanonicalAllele
import requests

def create_allele():
    # For this example we will use a ClinVar id as source with the associated hgvs_names, dbsnp_ids and preferred_name
    identifier = "ClinVar:11852"
    hgvs_names = {  "GRCh37": "NC_000011.9:g.76869378G>A", \
                    "GRCh38": "NC_000011.10:g.77158332G>A", \
                    "others": [ \
                        "NG_009086.1:g.35069G>A", \
                        "NM_000260.3:c.905G>A", \
                        "NP_000251.3:p.Arg302His", \
                        "Q13402:p.Arg302His"]}
    dbsnp_ids = [ "41298135" ]
    preferred_name =  "NM_000260.3(MYO7A):c.905G>A (p.Arg302His)"

    return CanonicalAllele( identifier=identifier, \
                            hgvs_names=hgvs_names, \
                            dbsnp_ids=dbsnp_ids, \
                            preferred_name=preferred_name )

def create_condition():
    ontology = 'http://purl.obolibrary.org/obo/'
    code = 'MONDO_0019501'
    name = 'Usher syndrome'
    disease = create_disease(ontology, code, name)

    condition = GeneticCondition()
    condition.add_disease(disease)
    condition.set_inheritancePattern( "Autosomal recessive inheritance" )

    return condition

def create_agent():
    agent_id = 'http://examples.com/agent1'
    agent = Agent(agent_id)
    agent.set_label('Gregor Mendel')
    return agent

def create_computational_agent():
    agent_id = 'http://examples.com/agent2'
    agent = Agent(agent_id)
    agent.set_label('ExAC Data Loader v1')
    return agent

def create_assessment(allele,agent):
    assessment_id = 'http://examples.com/assessment1'
    assessment = CriterionAssessment( assessment_id )
    criteria = read_criteria()
    criterion = criteria['PM2']
    assessment.set_criterion(criterion)
    #The library will check the input against allowed codings
    assessment.set_statementOutcome('met')
    assessment.set_variant(allele)
    when = '2017-01-24T16:07:57.082704+00:00'
    contribution = create_contribution(agent, when, PROP_ASSESSOR_ROLE)

    assessment.add_contribution(contribution)
    return assessment

#The numbers here are not correct; they are only for examples.
def create_frequency_data(allele,agent):
    frequency = PopulationAlleleFrequencyStatement()
    #the library will look up the code
    frequency.set_ascertainment('ExAC ascertainment method')
    #the library will look up the code
    frequency.set_population('GNOMAD:nfe')
    frequency.set_allele(allele)
    frequency.set_alleleCount(0)
    frequency.set_alleleNumber(1000)
    #The library will not calculate the frequency for you
    frequency.set_alleleFrequency(0)
    when = '2016-01-24T16:07:57.082704+00:00'
    contribution = create_contribution(agent, when, PROP_CURATOR_ROLE)
    frequency.add_contribution(contribution)
    return frequency

def create_example():
    #Create the root interpretation
    interpretation_id = 'http://example.com/interpretation_1'
    #Create and add the allele(variant)
    interpretation = VariantPathogenicityInterpretation(interpretation_id)
    allele = create_allele()
    interpretation.set_variant(allele)
    #Create and add the condition (disease)
    condition = create_condition()
    interpretation.add_condition(condition)
    #Call the variant pathogenic for this disease
    interpretation.set_statementOutcome( 'Pathogenic' )
    #Create Agent/contribution
    agent = create_agent()
    when = '2017-01-24T16:16:59.073653+00:00'
    contribution = create_contribution(agent, when, PROP_APPROVER_ROLE)
    interpretation.add_contribution(contribution)
    #Create assessment, (with same agent doing assessing & interpreting)
    assessment = create_assessment(allele,agent)
    strength = assessment.get_criterion().get_defaultStrength()
    add_criterion_assessment(interpretation,assessment,strength)
    #Create evidence
    frequency = create_frequency_data(allele,create_computational_agent())
    add_evidenceItems( assessment, [frequency] )

    #Write interpretation JSON to file
    outf = open('example1.json','w')
    json.dump(interpretation, outf, sort_keys = True, indent=4, \
            separators=(',',': '), cls = InterpretationEncoder,\
            out_style = 'first')
    outf.close()

if __name__ == '__main__':
    create_example()
