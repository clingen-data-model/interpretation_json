import json
from shutil import copy
from collections import defaultdict
import os, requests, sys

NAME='name'
FQNAME = 'fullyQualifiedName'
PARENT_KEY = 'parentType'
ENTITY_ID = 'entityId'
CARDINALITY = 'cardinality'
TYPE = 'dataType'
VSID = 'valueSetId'
ATTRIBUTES = 'attributes'
ID = 'id'

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

def write_data_type(types_and_atts,type_id,lib,t_const,a_const):
    dtype = types_and_atts[type_id]
    name = dtype[NAME]
    pname=get_parent_name(dtype,types_and_atts)
    type_const = t_const[type_id]
    lib.write( CLASSDEF % (name, pname, type_const) )
    for att in dtype[ATTRIBUTES]:
        attkey = att[ID]
        eid = att[ENTITY_ID]
        if eid == type_id:
            attconst = a_const[attkey]
            attname = att[NAME]
            if att[TYPE] == 'Coding':
                #ValueSet has an includesCoding attribute that doesn't take a particular VS
                try:
                    print attname, 'Coding', att[VSID]
                    vset = att[VSID]
                    lib.write("\n    @get_factory_coding('%s')" % (vset))
                except:
                    pass
            elif att[TYPE] == 'CodeableConcept':
                try:
                    print attname, 'CodeableConcept', att[VSID]
                    vset = att[VSID]
                    lib.write("\n    @get_factory_concept('%s')" % (vset))
                except:
                    pass
            try:
                if '*' in att[CARDINALITY]:
                    lib.write( LISTSETTER % (attname, attconst, attconst, attconst) )
                else:
                    lib.write( SETTER % (attname,attconst))
            except:
                print attkey
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

def write_library(types_and_atts,libname,codename, enumname):
    t_const, a_const = write_constants( types_and_atts, enumname )
    lib = file(libname,'w')
    lib.write('from interpretation_constants import *\n')
    lib.write('from coding_factory import get_factory_coding, get_factory_concept\n')
    lib.write('from node import Node\n\n')
    codef = file(codename,'w')
    codef.write('from interpretation_constants import *\n')
    codef.write('from node import Node\n\n')
    type_ids = sort_types(types_and_atts)
    for type_id in type_ids:
        if types_and_atts[type_id][NAME] in ['Coding','CodeableConcept']:
            outf = codef
        else:
            outf = lib
        write_data_type(types_and_atts,type_id,outf,t_const,a_const)
    lib.close()
    codef.close()
    

def write_constants(types_and_atts,enumname):
    type_constants = {}
    att_constants = {}
    enum = file(enumname,'w')
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
            attfqname = att[FQNAME]
            attname = att[NAME]
            att_constant = 'DMWG_%s_KEY' % ('_'.join(attfqname.upper().split('.')))
            att_constants[attkey] = att_constant
            if att_constant not in attconsts:
                enum.write("%s = '%s'\n" % (att_constant, attname))
                attconsts.add(att_constant)
    enum.close()
    return type_constants, att_constants


#def go(libdir = '/home/bizon/Projects/ClinGen/NewDataModel/interpretation/data/flattened'):
def go():
    #attributes = json.load(attributefile)
    type_url = 'http://datamodel.clinicalgenome.org/interpretation/master/json/Types'
    t_res = requests.get(type_url)
    json_string = t_res.text
    types_and_atts = json.loads(json_string)
    vsdir = 'ValueSets'
    try:
        os.mkdir(vsdir)
    except:
        pass
    #TODO: FIX UP
    #copy('%s/Criterion.json' % libdir, '%s/Criterion.json' % vsdir)
    for i in range(1,24):
        if i in [1,18,19,20]:
            continue
        VS = 'VS%03d' % i
        url = 'http://datamodel.clinicalgenome.org/interpretation/master/json/%s' % VS
        res = requests.get(url)
        outf = file('%s/%s' % (vsdir,VS),'w')
        text = res.text
        outf.write(text)
        outf.close()
    write_library(types_and_atts, 'interpretation_generated.py', 'coding_generated.py', 'interpretation_constants.py')

if __name__ == '__main__':
    go()
