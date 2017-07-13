import os
import json
from functools import wraps
from coding_generated import Coding, CodeableConcept

class CodingFactory:
    def __init__(self,vsdir='ValueSets'):
        self.vsets = {}
        files = os.listdir(vsdir)
        for f in files:
            if f.startswith('VS'):
                inf = file('%s/%s'% (vsdir,f),'r')
                valueset = json.load(inf)
                vsid = valueset['id']
                codings = valueset['includesCoding']
                self.vsets[vsid] = codings
                # our current value sets use a prefix in id.  Put in a fully qualified id
                for c in codings:
                    c['fqid'] = c['system'] + c['code']
    def lookup_coding(self,valueset_id,lookup):
        vset = self.vsets[valueset_id]
        for key in ['fqid','id','code','display']:
            for coding in vset:
                if coding[key] == lookup:
                    c = Coding(coding['fqid'])
                    c.set_display(coding['display'])
                    c.set_system(coding['system'])
                    c.set_code(coding['code'])
                    return c
        #For a coding, if we can't resolve, we should fail
        raise Exception("Cannot translate code %s in ValueSet %s" % (lookup, valueset_id))
    #For a codeable concept, if we can't translate into one of our codings, we want to construct
    # a freetext codeable concept.
    def lookup_concept(self, valueset_id,lookup):
        concept = CodeableConcept()
        try:
            coding = self.lookup_coding(valueset_id, lookup)
            concept.add_coding(coding)
        except:
            # value didn't translate to a coding
            concept.set_text(lookup)
        return concept

the_factory = CodingFactory()

def get_factory_coding(setid):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(args[1], Coding):
                return func(*args,**kwargs)
            coding = the_factory.lookup_coding(setid,args[1])
            alist = list(args)
            alist[1] = coding
            return func(*alist,**kwargs)
        return wrapper
    return decorate

def get_factory_concept(setid):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(args[1], CodeableConcept):
                return func(*args,**kwargs)
            concept = the_factory.lookup_concept(setid,args[1])
            alist = list(args)
            alist[1] = concept
            return func(*alist,**kwargs)
        return wrapper
    return decorate
