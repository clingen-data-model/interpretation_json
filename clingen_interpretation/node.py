from clingen_interpretation.interpretation_constants import *

PROP_LABEL_KEY = 'label'

class Node:
    def __init__( self, **kwargs ):
        self.data = {}
        identifier = kwargs.get('identifier',None)
        if identifier is not None:
            self.data[ID_KEY] = identifier
    #move id tag into entity? Or some kind of flag?
    def get_id(self):
        try:
            return self.data[ID_KEY]
        except:
            return self.data[ALLELE_REGISTRY_ID_KEY]
    def set_label(self,label):
        self.data[PROP_LABEL_KEY] = label
    def get_label(self):
        return self.data[PROP_LABEL_KEY]
