import os,sys
import json
from functools import wraps
from clingen_interpretation.node import Node

LABEL='label'

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
        # self.next_sequence = 0
        self.vsets = {}
        self.extensibility = {}
        self.entity_types = {}
        if vsdir == '':
            this_dir, this_filename = os.path.split(__file__)
            vsdir = os.path.join(this_dir, 'ValueSets')
        files = os.listdir(vsdir)
        for f in files:
            fname='%s/%s'% (vsdir,f)
            inf = open(fname,'r')
            valueset = json.load(inf)
            vsid = valueset['id']
            try:
                concepts = valueset['concept']
            except KeyError:
                concepts = {}
            self.vsets[vsid] = concepts
            self.extensibility[vsid] = valueset['valueSetExtensibility']
            for c in concepts:
                try:
                    etype = c['type']
                    #Workaround for now CB 6/11/2018
                    if etype == 'Entity':
                        continue
                    #End workaround
                    if etype in self.entity_types:
                        if self.entity_types[etype] != vsid:
                            print('Type %s occurs in 2 Value Sets' % etype)
                            print(vsid, self.entity_types[etype])
                            print('Need to make entity_types point to sets')
                            print('But have not yet')
                            sys.exit(1)
                    else:
                        self.entity_types[etype] = vsid
                except KeyError:
                    #This concept doesn't have a type. That's ok, and in fact pretty common these days.
                    pass

    def get_value_sets(self):
        return self.vsets

    def get_extensibility(self):
        return self.extensibility

    # def get_next_blank_iri(self):
        # iri = "_:b"+str(self.next_sequence)
        # self.next_sequence += 1
        # return iri

    def lookup_entity(self,valueset_id,lookup):
        """Given a lookup value, return a well-formed Domain Entity.

        Given the lookup value, and a value set id, look in the value set
        for a value that matches either the id, the code or the display.
        Create the correct type of DomainEntity, set its values and return
        it"""
        #valueset_id = self.entity_types[entity_type_name]
        vset = self.vsets[valueset_id]
        found = False
        extensible = self.extensibility[valueset_id]['id'] == 'SEPIO:0000365'
        for key in ['id','label']:
            for coding in vset:
                if coding[key].upper() == lookup.upper():
                    found = True
                    node = Node( identifier=coding['id'] )
                    node.set_label(coding[LABEL])
                    return node
        if not found and not extensible:
            raise Exception("Did not find %s in %s" % (lookup, valueset_id))

        import clingen_interpretation.entities_generated as entities_generated
        try:
            entity_class = getattr(entities_generated, valueset_id)
        except AttributeError:
            entity_class = Node
        e = entity_class()
        e.set_label(lookup)
        return e

the_factory = DomainEntityFactory()

def get_factory_entity(domain_entity_typename):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            from clingen_interpretation.node import Node
            if isinstance(args[1], Node):
                return func(*args,**kwargs)
            coding = the_factory.lookup_entity(domain_entity_typename,args[1])
            alist = list(args)
            alist[1] = coding
            return func(*alist,**kwargs)
        return wrapper
    return decorate
