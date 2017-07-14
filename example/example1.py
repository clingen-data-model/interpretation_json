from clingen_interpretation.interpretation_generated import *
from clingen_interpretation.interpretation_extras import *
from clingen_interpretation.interpretation_constants import *
from clingen_interpretation.Allele import Variant
import requests

def create_allele():
    #For this example, we will use this HGVS
    hgvs = 'NC_000014.8:g.23898488G>A'
    # send a GET request with parameter
    url = 'http://reg.genome.network/allele?hgvs='
    # convert symbol > to special code %3E
    url += requests.utils.quote(hgvs)
    #retreive the ClinGen 
    res = requests.get(url)
    txt = res.text
    cardata = json.loads(txt)
    allele = Variant(cardata)
    return allele

def create_condition():
    ontology = 'http://www.disease-ontology.org/term/'  
    code = 'DOID_11984'
    name = 'hypertrophic cardiomyopathy'
    disease = create_dmwg_disease(ontology, code, name)
    condition = MendelianCondition()
    condition.add_disease(disease)
    return condition

def create_agent():
    agent_id = 'http://examples.com/agent1'
    agent = Agent(agent_id)
    agent.set_name('Gregor Mendel')
    return agent

def create_computational_agent():
    agent_id = 'http://examples.com/agent2'
    agent = Agent(agent_id)
    agent.set_name('ExAC Data Loader v1')
    return agent

def create_assessment(allele,agent):
    assessment_id = 'http://examples.com/assessment1'
    assessment = CriterionAssessment( assessment_id )
    criteria = read_criteria()
    criterion = criteria['PM2']
    assessment.set_criterion(criterion)
    #The library will check the input against allowed codings
    assessment.set_outcome('met')
    assessment.set_variant(allele)
    when = '2017-01-24T16:07:57.082704+00:00'
    contribution = create_contribution(agent, when, DMWG_ASSESSOR_ROLE)
    assessment.add_contribution(contribution)
    return assessment

#The numbers here are not correct; they are only for examples.
def create_frequency_data(allele,agent):
    frequency = AlleleFrequency()
    #the library will look up the code
    frequency.set_ascertainment('ExAC')
    #the library will look up the code
    frequency.set_population('nfe') 
    frequency.set_allele(allele)
    frequency.set_alleleCount(0)
    frequency.set_alleleNumber(1000)
    #The library will not calculate the frequency for you
    frequency.set_alleleFrequency(0) 
    when = '2016-01-24T16:07:57.082704+00:00'
    contribution = create_contribution(agent, when, DMWG_CURATOR_ROLE)
    frequency.add_contribution(contribution)
    return frequency

def create_example():
    #Create the root interpretation
    interpretation_id = 'http://example.com/interpretation_1'
    #Create and add the allele(variant)
    interpretation = VariantInterpretation(interpretation_id)
    allele = create_allele()
    interpretation.set_variant(allele)
    #Create and add the condition (disease)
    condition = create_condition()
    interpretation.add_condition(condition)
    #Call the variant pathogenic for this disease
    interpretation.set_clinicalSignificance( 'Pathogenic' )
    #Create Agent/contribution
    agent = create_agent()
    when = '2017-01-24T16:16:59.073653+00:00'
    contribution = create_contribution(agent, when, DMWG_INTERPRETER_ROLE)
    interpretation.add_contribution(contribution)
    #Create assessment, (with same agent doing assessing & interpreting)
    assessment = create_assessment(allele,agent)
    strength = assessment.get_criterion().get_defaultStrength()
    add_criterion_assessment(interpretation,assessment,strength)
    #Create evidence
    frequency = create_frequency_data(allele,create_computational_agent())
    add_informations( assessment, [frequency] )

    #Write interpretation JSON to file
    outf = file('example1.json','w')
    json.dump(interpretation, outf, sort_keys = True, indent=4, \
            separators=(',',': '), cls = InterpretationEncoder,\
            out_style = 'first')
    outf.close()

if __name__ == '__main__':
    create_example()
