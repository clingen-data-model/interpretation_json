from interpretation_generated import *
from coding_generated import *
import json
from coding_factory import the_factory

#UtilityMethods for wrapping things in Evidence Lines
def add_criterion_assessment(interpretation, assessment, strength):
    evidence_line = EvidenceLine()
    evidence_line.add_information( assessment )
    evidence_line.set_evidenceStrength( strength )
    interpretation.add_evidence( evidence_line )

def add_informations( assessment, information_list):
    for information in information_list:
        evidence_line = EvidenceLine()
        evidence_line.add_information( information )
        assessment.add_evidence( evidence_line )

DMWG_CURATOR_ROLE = 'curator'
DMWG_INTERPRETER_ROLE = 'interpreter'
DMWG_ASSESSOR_ROLE = 'assessor'
#Utility methods for creating contributions
def create_contribution(agent, ondate, role):
    contribution = Contribution()
    contribution.set_agent(agent)
    contribution.set_onDate(ondate)
    #roleconcept = CodeableConcept()
    # Populate from somewhere?
    #coding = create_coding('http://clinicalgenome.org/datamodel/contributory-role',role,role)
    #roleconcept.add_coding(coding)
    contribution.set_role(role)
    return contribution

#Utility method for creating diseases
def create_dmwg_disease(system, code, name):
    cc = CodeableConcept()
    coding = create_coding(system, name, code )
    cc.add_coding(coding)
    return cc

#Utility method to make sure that coding gets the ID set correctly
def create_coding(system,display,code):
    iri = system+code
    coding = Coding(iri)
    coding.set_display(display)
    coding.set_code(code)
    coding.set_system(system)
    return coding

def read_criteria():
    inf = file('ValueSets/Criterion.json','r')
    jcrit = json.load(inf)
    inf.close()
    criteria = {}
    for rulenum in jcrit:
        crit = jcrit[rulenum]
        criterion = Criterion(crit['id'])
        criterion.set_description (crit['description'] )
        criterion.set_shortDescription ( crit['shortDescription'] )
        criterion.set_defaultStrength( crit['defaultStrength'] )
        criteria[rulenum] = criterion
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
        super(InterpretationEncoder, self).__init__(*args, **kwargs)
        self.written_nodes = set()
    def default(self,obj):
        if isinstance(obj,Node):
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
