from interpretation_constants import *

class Node:
    def __init__(self):
        pass
    #move id tag into entity? Or some kind of flag?
    def get_id(self):
        try:
            return self.data[DMWG_ID_KEY]
        except:
            return self.data[ALLELE_REGISTRY_ID_KEY]

