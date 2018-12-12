from clingen_interpretation.interpretation_constants import *

DMWG_LABEL_KEY = 'label'

class Node:
    def __init__(self,identifier=None):
        self.data = {}
        if identifier is not None:
            self.data[DMWG_ID_KEY] = identifier
    #move id tag into entity? Or some kind of flag?
    def get_id(self):
        try:
            return self.data[DMWG_ID_KEY]
        except:
            return self.data[ALLELE_REGISTRY_ID_KEY]
    def set_label(self,label):
        self.data[DMWG_LABEL_KEY] = label
    def get_label(self):
        return self.data[DMWG_LABEL_KEY]

