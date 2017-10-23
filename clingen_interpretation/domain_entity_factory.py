import os
import json
from functools import wraps

class DomainEntityFactory:
    """Enables creation of Domain Entities from codes or display names.

    This factory reads the ValueSets from disk, and associates them
    with particular subclassess of domain enitities. It can then be
    searched to find values that match a string either by id, code, or
    display name, then creates the right kind of DomainEntity, sets the
    values correctly and returns it."""
    def __init__(self,vsdir=''):
        """Read value sets from disk.  Create maps of the value set entries
           and relationship with particular domain entities"""
        self.vsets = {}
        self.entity_types = {}
        if vsdir == '':
            this_dir, this_filename = os.path.split(__file__)
            vsdir = os.path.join(this_dir, 'ValueSets')
        files = os.listdir(vsdir)
        for f in files:
            if f.startswith('VS'):
                print vsdir, f
                inf = file('%s/%s'% (vsdir,f),'r')
                valueset = json.load(inf)
                vsid = valueset['id']
                try:
                    concepts = valueset['includesConcept']
                except KeyError:
                    concepts = {}
                self.vsets[vsid] = concepts
                self.entity_types[valueset['name']] = vsid
    def lookup_entity(self,entity_type_name,lookup):
        """Given a lookup value, return a well-formed Domain Entity.

        Given the lookup value, and a value set id, look in the value set
        for a value that matches either the id, the code or the display.
        Create the correct type of DomainEntity, set its values and return 
        it"""
        valueset_id = self.entity_types[entity_type_name]
        vset = self.vsets[valueset_id]
        import entities_generated
        entity_class = getattr(entities_generated, entity_type_name)
        for key in ['id','code','display']:
            for coding in vset:
                if coding[key] == lookup:
                    e = entity_class(coding['id'])
                    e.set_label(coding['display'])
                    #e.set_description(coding['description'])
                    return e
        #If we didn't find the value, we create without the IRI, and set label
        e = entity_class()
        e.set_label(lookup)
        return e

the_factory = DomainEntityFactory()

def get_factory_entity(domain_entity_typename):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            from entities_generated import DomainEntity
            if isinstance(args[1], DomainEntity):
                return func(*args,**kwargs)
            coding = the_factory.lookup_entity(domain_entity_typename,args[1])
            alist = list(args)
            alist[1] = coding
            return func(*alist,**kwargs)
        return wrapper
    return decorate
        
