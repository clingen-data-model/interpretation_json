import sys
from jsonschema import validate
import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse
from clingen_interpretation.domain_entity_factory import DomainEntityFactory

def validate_with_schema(in_json):
    """Apply the json schema to a json file and see if the file matches the schema"""
    with open('interpretation_schema.json','r') as inf:
        schema = json.load(inf)
    with open(in_json,'r') as inf:
        input_json = json.load(inf)
    validate(input_json ,schema)

def validate_with_values(in_json):
    """Attributes can be annotated with ValueSets.  If the ValueSet is not extensible than the
       value of the attribute must be from the value set.  This checks these non-extensible attributes to make
       sure that this is the case.

       If the value set is extensible, the validator prints a warning if it finds a value that is not in the value
       set."""
    with open(in_json,'r') as inf:
        input_json = json.load(inf)
    factory = DomainEntityFactory()
    vsets = factory.get_value_sets()
    extents = factory.get_extensibility()
    errors = []
    warnings = []
    with open('value_set_information.txt','r') as infile:
        for line in infile:
            x = line.strip().split('\t')
            e_type = x[0]
            a_name = x[1]
            vs_id  = x[2]
            #if vs_id.startswith('SEPIO:'):
            #    print("I don't recognize this ValueSet: %s" % vs_id)
            #    continue
            if 'label' not in extents[vs_id] or extents[vs_id]['label'] == 'fixed':
                accumulator = errors
            elif extents[vs_id]['label'] == 'extensible':
                accumulator = warnings
            check_valueset(in_json, e_type, a_name, vsets[vs_id], accumulator)
    if len(errors) > 0:
        print('Entity Validation Failed:')
        for entity,attiribute,value_set,value in errors:
            print('%s is an invalid value for fixed value set %s (%s.%s)' % (value,value_set,entity,attribute))
    if len(warnings) > 0:
        print('Entity Validation Warnings:')
        for entity,attiribute,value_set,value in errors:
            print('%s not in extensible value set %s (%s.%s)' % (value,value_set,entity,attribute))

def check_valueset(ijson, etype, aname, vset, acc):
    jpstring = '$..*[?(@.type="%s")].%s'% (etype, aname)
    json_path = parse( jpstring )
    values = [ m.value for m in json_path.find(ijson) ]
    for v in values:
        if isinstance(v, dict):
            vid = v['id']
        else:
            vid = v
        if vid not in vset:
            acc.append( (etype,aname,vset,vid) )

def go(in_json):
    validate_with_schema(in_json)
    validate_with_values(in_json)

if __name__ == '__main__':
    go(sys.argv[1])
