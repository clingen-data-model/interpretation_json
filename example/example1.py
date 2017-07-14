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
    
    #Write interpretation JSON to file
    outf = file('example1.json','w')
    json.dump(interpretation, outf, sort_keys = True, indent=4, \
            separators=(',',': '), cls = InterpretationEncoder,\
            out_style = 'first')
    outf.close()

if __name__ == '__main__':
    create_example()
