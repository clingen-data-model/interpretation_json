from interpretation_constants import *
from node import Node

class CodeableConcept(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CODEABLECONCEPT_TYPE 
    def set_text(self,x):
        self.data[DMWG_CODEABLECONCEPT_TEXT_KEY] = x
    def get_text(self):
        return self.data[DMWG_CODEABLECONCEPT_TEXT_KEY]
    def add_coding(self,x):
        if not DMWG_CODEABLECONCEPT_CODING_KEY in self.data:
            self.data[DMWG_CODEABLECONCEPT_CODING_KEY] = []
        self.data[DMWG_CODEABLECONCEPT_CODING_KEY].append( x ) 
    def get_coding(self):
        return self.data[DMWG_CODEABLECONCEPT_CODING_KEY]

class Coding(Node):
    def __init__(self,iri=None):
        self.data = {}
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = DMWG_CODING_TYPE 
    def set_display(self,x):
        self.data[DMWG_CODING_DISPLAY_KEY] = x
    def get_display(self):
        return self.data[DMWG_CODING_DISPLAY_KEY]
    def set_system(self,x):
        self.data[DMWG_CODING_SYSTEM_KEY] = x
    def get_system(self):
        return self.data[DMWG_CODING_SYSTEM_KEY]
    def set_code(self,x):
        self.data[DMWG_CODING_CODE_KEY] = x
    def get_code(self):
        return self.data[DMWG_CODING_CODE_KEY]

