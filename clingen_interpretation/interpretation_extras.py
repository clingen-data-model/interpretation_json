from clingen_interpretation.interpretation_generated import *
from clingen_interpretation.entities_generated import *
import json
from clingen_interpretation.domain_entity_factory import the_factory
import os

#UtilityMethods for wrapping things in Evidence Lines
def add_criterion_assessment(interpretation, assessment, strength):
    evidence_line = EvidenceLine()
    evidence_line.add_evidenceItem( assessment )
    evidence_line.set_evidenceStrength( strength )
    interpretation.add_evidenceLine( evidence_line )

def add_evidenceItems( assessment, evidenceItems):
    for item in evidenceItems:
        evidence_line = EvidenceLine()
        evidence_line.add_evidenceItem( item )
        assessment.add_evidenceLine( evidence_line )

DMWG_CURATOR_ROLE = 'curator'
DMWG_ASSESSOR_ROLE = 'assessor'
DMWG_APPROVER_ROLE = 'approver'
DMWG_PUBLISHER_ROLE = 'publisher'

#Utility methods for creating contributions
def create_contribution(agent, ondate, role):
    contribution = Contribution()
    contribution.set_agent(agent)
    contribution.set_contributionDate(ondate)
    contribution.set_contributionRole(role)
    return contribution

#Utility methods for creating contributions
def create_agent(id, label, agent_for=None):
    # if id is None:
    #     id = the_factory.get_next_blank_iri()
    if id is not None:
        agent = Agent(id)
    agent.set_label(label)
    if agent_for is not None:
        agent.set_agentFor(agent_for)
    return agent

#Utility methods for creating assertion methods (VariantPathogenicityInterpretationGuideline)
def create_assertion_method(name, url=None):
    method = VariantPathogenicityInterpretationGuideline()
    method.set_label( name )
    if url is not None:
        method.set_url( url )
    return method

#Utility method for creating diseases. Note that disease is not a type any more
def create_dmwg_disease(system, code, name):
    iri = system+code
    disease = Node(iri)
    disease.set_label(name)
    return disease

#Utility method to make sure that coding gets the ID set correctly
#def create_entity(system,display,code):
#    iri = system+code
#    coding = Coding(iri)
#    coding.set_display(display)
#    coding.set_code(code)
#    coding.set_system(system)
#    return coding

def read_criteria():
    this_dir, this_filename = os.path.split(__file__)
    crit_path = os.path.join(this_dir, 'ValueSets', 'SEPIO:0000395')
    inf = open(crit_path,'r')
    jcrit = json.load(inf)
    inf.close()
    criteria = {}
    for crit in jcrit['concept']:
        criterion = VariantPathogenicityInterpretationCriterion(crit['id'])
        label = crit['label']
        criterion.set_label ( label )
        if label.startswith('PVS'):
            defStrength = 'Pathogenic Very Strong'
        elif label.startswith('PS'):
            defStrength = 'Pathogenic Strong'
        elif label.startswith('PP'):
            defStrength = 'Pathogenic Supporting'
        elif label.startswith('PM'):
            defStrength = 'Pathogenic Moderate'
        elif label.startswith('BS'):
            defStrength = 'Benign Strong'
        elif label.startswith('BP'):
            defStrength = 'Benign Supporting'
        elif label.startswith('BM'):
            defStrength = 'Benign Moderate'
        elif label.startswith('BA'):
            defStrength = 'Benign Stand Alone'
        criterion.set_defaultStrength( defStrength )
        criteria[label] = criterion
    return criteria


#This declutters a bit by only printing the full node the first time we
#encounter it.  But that's not necessarily in the highest node, because of the
#ordering of the keys.  Should probably be smarter, but it works for the moment
class InterpretationEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        if 'out_style' in kwargs:
            self.ostyle = kwargs['out_style']
            del kwargs['out_style']
        else:
            self.ostyle='first'
        if 'context' in kwargs:
            self.context = kwargs['context']
        else:
            self.context = 'http://dataexchange.clinicalgenome.org/interpretation/json/context'
        super(InterpretationEncoder, self).__init__(*args, **kwargs)
        self.written_nodes = set()
    def default(self,obj):
        if isinstance(obj,Node):
            #is this right?  Probably should do it by depth?
            if isinstance(obj,VariantPathogenicityInterpretation):
                obj.data['@context'] = self.context
            if self.ostyle == 'full':
                return obj.data
            if obj not in self.written_nodes:
                self.written_nodes.add(obj)
                return obj.data
            try:
                #try to write it just by id
                return obj.get_id()
            except:
                #but if it doesn't have an id (like a codeable concept), just put all the data
                return obj.data
        else:
            return json.JSONEncoder.default(self,obj)
