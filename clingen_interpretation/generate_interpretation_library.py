import json
from shutil import copy
from collections import defaultdict
import os, requests, sys
import codecs

NAME='name'
FQNAME = 'fullyQualifiedName'
PARENT_KEY = 'parentType'
ENTITY_ID = 'entityId'
CARDINALITY = 'cardinality'
TYPE = 'dataType'
VSID = '@valueSetId'
ATTRIBUTES = 'attributes'
ID = 'id'
DMWG_LABEL_ID = 'LabelIdentifier'

def get_parent_name(dtype,types):
    if PARENT_KEY not in dtype:
        return 'Node'
    parentid = dtype[PARENT_KEY]
    parent = types[parentid]
    return parent[NAME]

CLASSDEF = \
'''class %s(%s):
    def __init__(self,iri=None):
        self.data = {}
        # if iri is None:
        #     iri = the_factory.get_next_blank_iri()
        if iri is not None:
            self.data[DMWG_ID_KEY] = iri
        self.data[DMWG_TYPE_KEY] = %s '''

SETTER = '''
    def set_%s(self,x):
        self.data[%s] = x'''

LISTSETTER = '''
    def add_%s(self,x):
        if not %s in self.data:
            self.data[%s] = []
        self.data[%s].append( x ) '''

GETTER = '''
    def get_%s(self):
        return self.data[%s]'''

def type_is_entity(dtype, types_and_atts):
    """Determine whether a particular type is a DomainEntity"""
    DOMAINENTITY='DomainEntity'
    if dtype[NAME] == DOMAINENTITY:
        return True
    pname = get_parent_name(dtype, types_and_atts)
    if pname == DOMAINENTITY:
        return True
    return False

def attribute_is_entity(attribute, types_and_atts):
    """Determine whether a particular attribute points to a DomainEntity"""
    att_typename = attribute[TYPE]
    #The type is a string name of the type, not the id, so we have to
    # search our type map for it
    for dtype in types_and_atts.values():
        if dtype[NAME] == att_typename:
            return type_is_entity(dtype, types_and_atts)
    #It's not one of our types.  It's "string" or something like that.
    return False

def add_label(dtype):
    """We have an open-world point of view in constructing messages, but the model can't include everything.
    This only really causes a problem when the a transform code wants to do things like set a label on an object.
    We allow anything to have a label, but it's not specifically part of the model, so we add it here to every
    node.  It might make more sense to modify the transform code to handle extra attributes, but this is
    here for convenience sake"""
    LABEL = 'label'
    attribute = {CARDINALITY: '0..1', NAME: LABEL, ENTITY_ID: dtype[ID], ID: DMWG_LABEL_ID }
    dtype[ATTRIBUTES].append(attribute)

def write_data_type(types_and_atts,type_id,lib,t_const,a_const):
    """Write a python class representing a particular type_id."""
    dtype = types_and_atts[type_id]
    name = dtype[NAME]
    # We have these in our sheets, but they need to be broken out.  For now, we have this stuff hardcoded
    # to enable transitions from AR.
    if name in ('CanonicalAllele', 'ContextualAllele'):
        return
    pname=get_parent_name(dtype,types_and_atts)
    type_const = t_const[type_id]
    lib.write( CLASSDEF % (name, pname, type_const) )
    add_label(dtype)
    for att in dtype[ATTRIBUTES]:
        attkey = att[ID]
        eid = att[ENTITY_ID]
        if eid == type_id:
            attconst = a_const[attkey]
            attname = att[NAME]
            if VSID in att and att[VSID] != '':
                try:
                    if att[VSID] != 'SEPIO-CG:65900': #SEPIO-CG:65900 is a marker in the sheets for things we need to generate.
                        lib.write("\n    @get_factory_entity('%s')" % att[VSID] )
                except:
                    pass
            try:
                if '*' in att[CARDINALITY]:
                    lib.write( LISTSETTER % (attname, attconst, attconst, attconst) )
                else:
                    lib.write( SETTER % (attname,attconst))
            except:
                print( attkey )
                exit()
            lib.write( GETTER % (attname, attconst) )
    lib.write('\n\n')


def flatten(childs,typeids,key):
    for d in childs[key]:
        typeids.append(d)
        flatten( childs, typeids, d )

def sort_types(types):
    children = defaultdict(list)
    for typeid in types:
        thistype = types[typeid]
        if PARENT_KEY in thistype:
            parentid = thistype[PARENT_KEY]
        else:
            parentid = 'ROOT'
        children[parentid].append(typeid)
    typeids = []
    flatten(children,typeids,'ROOT')
    return typeids

def write_library(types_and_atts,libname,entname, enumname):
    """Create a set of python classes representing data model classes.

    Arguments: types_and_atts: a structure parsed from a JSON definition of
                               model types.
               libname: output file name for the generated library
               enumname: output file name for enumerations """
    t_const, a_const = write_constants( types_and_atts, enumname )
    lib = open(libname,'w')
    lib.write('from clingen_interpretation.interpretation_constants import *\n')
    lib.write('from clingen_interpretation.domain_entity_factory import get_factory_entity\n')
    lib.write('from clingen_interpretation.node import Node\n\n')
    entf = open(entname,'w')
    entf.write('from clingen_interpretation.interpretation_constants import *\n')
    entf.write('from clingen_interpretation.interpretation_generated import Entity\n')
    entf.write('from clingen_interpretation.domain_entity_factory import get_factory_entity\n')
    entf.write('from clingen_interpretation.node import Node\n\n')
    type_ids = sort_types(types_and_atts)
    for type_id in type_ids:
        if type_is_entity(types_and_atts[type_id], types_and_atts):
            outf = entf
        else:
            outf = lib
        write_data_type(types_and_atts,type_id,outf,t_const,a_const)
    lib.close()
    entf.close()


def write_constants(types_and_atts,enumname):
    type_constants = {}
    att_constants = {}
    enum = open(enumname,'w')
    enum.write("ALLELE_REGISTRY_ID_KEY = '@id'\n\n")
    enum.write("DMWG_ID_KEY = 'id'\n")
    enum.write("DMWG_TYPE_KEY = 'type'\n\n")
    for typekey in types_and_atts:
        dtype = types_and_atts[typekey]
        dname = dtype[NAME]
        type_constant = 'DMWG_%s_TYPE' % (dname.upper())
        type_constants[typekey] = type_constant
        enum.write("%s = '%s'\n" % (type_constant, dname))
    enum.write('\n')
    attconsts = set()
    for typekey in types_and_atts:
        dtype = types_and_atts[typekey]
        attributes = dtype[ ATTRIBUTES ]
        for att in attributes:
            attkey = att[ID]
            attname = att[NAME]
            try:
                attfqname = att[FQNAME]
            except:
                #print 'Missing fqname for %s' % attkey
                attfqname = '%s.%s' % (attkey, attname)
            att_constant = 'DMWG_%s_KEY' % ('_'.join(attfqname.upper().split('.')))
            att_constants[attkey] = att_constant
            if att_constant not in attconsts:
                enum.write("%s = '%s'\n" % (att_constant, attname))
                attconsts.add(att_constant)
    #Add label
    att_constants[DMWG_LABEL_ID] = DMWG_LABEL_ID
    enum.write("%s = 'label'\n" % DMWG_LABEL_ID)
    #for aid in att_constants:
    #    print aid,att_constants[aid]
    enum.close()
    return type_constants, att_constants

def pull_value_sets(vsdir,types_and_atts):
    """Pull the value set definitions from dataexchange.clinicalgenome.org.
    We look for the value sets that are bound to attributes"""
    typeids = sort_types(types_and_atts)
    value_set_set = set()
    for type_id in typeids:
        dtype = types_and_atts[type_id]
        for att in dtype[ATTRIBUTES]:
            if VSID in att and att[VSID] != '':
                value_set_set.add(att[VSID])
    try:
        os.mkdir(vsdir)
    except:
        pass
    for VS in value_set_set:
        if ':' not in VS: #don't pull down "???" or other garbage
            continue
        url = 'http://dataexchange.clinicalgenome.org/interpretation/master/json/%s' % VS
        res = requests.get(url)
        outf = codecs.open('%s/%s' % (vsdir,VS),'w',encoding='utf-8')
        text = res.text
        outf.write(text)
        outf.close()


def go():
    """Main function for creating library.

    In order to create JSON objects, we want to pull Type/Attribute/Value
    definitions from the web and use those definitions to create python
    classes and constants"""
    type_url = 'http://dataexchange.clinicalgenome.org/interpretation/master/json/Types'
    t_res = requests.get(type_url)
    with open('types.json','w') as outf:
        outf.write(json.dumps(t_res.json(),indent=4))
    json_string = t_res.text
    types_and_atts = json.loads(json_string)
    pull_value_sets('ValueSets',types_and_atts)
    write_library(types_and_atts, 'interpretation_generated.py', 'entities_generated.py', 'interpretation_constants.py')

if __name__ == '__main__':
    go()
