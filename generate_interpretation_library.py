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

def write_data_type(types,type_id,attributes,lib,t_const,a_const):
    dtype = types[type_id]
    name = dtype[NAME]
    pname=get_parent_name(dtype,types)
    type_const = t_const[type_id]
    lib.write( CLASSDEF % (name, pname, type_const) )
    for attkey in attributes:
        att=attributes[attkey]
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

def write_library(types,attributes,libname,codename, enumname):
    t_const, a_const = write_constants( types, attributes, enumname )
    lib = file(libname,'w')
    lib.write('from interpretation_constants import *\n')
    lib.write('from coding_factory import get_factory_coding, get_factory_concept\n')
    lib.write('from node import Node\n\n')
    codef = file(codename,'w')
    codef.write('from interpretation_constants import *\n')
    codef.write('from node import Node\n\n')
    type_ids = sort_types(types)
    for type_id in type_ids:
        if types[type_id][NAME] in ['Coding','CodeableConcept']:
            outf = codef
        else:
            outf = lib
        write_data_type(types,type_id,attributes,outf,t_const,a_const)
    lib.close()
    codef.close()
    

def write_constants(types,attributes,enumname):
    type_constants = {}
    att_constants = {}
    enum = file(enumname,'w')
    enum.write("ALLELE_REGISTRY_ID_KEY = '@id'\n\n")
    enum.write("DMWG_ID_KEY = 'id'\n")
    enum.write("DMWG_TYPE_KEY = 'type'\n\n")
    for typekey in types:
        dtype = types[typekey]
        dname = dtype[NAME]
        type_constant = 'DMWG_%s_TYPE' % (dname.upper())
        type_constants[typekey] = type_constant
        enum.write("%s = '%s'\n" % (type_constant, dname))
    enum.write('\n')
    for attkey in attributes:
        if attkey == ' ':
            #skip blank rows in the table
            continue
        att = attributes[attkey]
        attfqname = att[FQNAME]
        attname = att[NAME]
        att_constant = 'DMWG_%s_KEY' % ('_'.join(attfqname.upper().split('.')))
        att_constants[attkey] = att_constant
        enum.write("%s = '%s'\n" % (att_constant, attname))
    enum.close()
    return type_constants, att_constants


def go(libdir = '/home/bizon/Projects/ClinGen/NewDataModel/interpretation/data/flattened'):
    typefile = file('%s/%s' % (libdir,'Type.json'),'r')
    attributefile = file('%s/%s' % (libdir,'Attribute.json'),'r')
    types = json.load(typefile)
    attributes = json.load(attributefile)
    typefile.close()
    attributefile.close()
    vsdir = 'ValueSets'
    try:
        os.mkdir(vsdir)
    except:
        pass
    copy('%s/Criterion.json' % libdir, '%s/Criterion.json' % vsdir)
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
    write_library(types,attributes,'interpretation_generated.py', 'coding_generated.py', 'interpretation_constants.py')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        go(sys.argv[1])
    else:
        go()
