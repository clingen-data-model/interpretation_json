import json
import requests

def make_def(typedef):
    """The meat of the json schema generation creates a dictionary that
    will serialized into the definitions section of the schema, for a given
    typedef, as read from our json definitions"""
    #These all have structure.  Non-structured are handled with LabeledIRI
    definition = { "type":"object"}
    #Description is special, and goes outside properties
    if 'description' in typedef:
        definition['description'] = typedef['description']
    properties = {}
    attributes=typedef['attributes']
    required=[]
    for attribute in attributes:
        #If minimum cardinality is >0, then the element is required.
        mincard = int(attribute['cardinality'].split('..')[0])
        if mincard > 0 and attribute['name'] != 'description':
            required.append( attribute['name'] )
        #If maximum cardinality is >1, then the element is an array.
        maxcard_str = attribute['cardinality'].split('..')[-1]
        if maxcard_str == '*':
            maxcard = 9999
        else:
            maxcard = int(maxcard_str)
        #This structure is the same whether we're going into an array or not
        # We are defining the type either as a primitive, or as something
        # in our definitions
        dt = attribute['dataType']
        if dt == 'string' or dt == 'Datetime':
            prop = { 'type': 'string' }
        elif dt == 'integer':
            prop = { 'type': 'integer' }
        elif dt == '@id' or dt == 'ExternalConcept':
            prop = {'$ref': '#/definitions/LabeledIRI'}
        else:
            prop = { '$ref': '#/definitions/{}'.format(attribute['dataType']) }
        #Wrap the type in an array if necessariy
        if maxcard < 2:
            properties[attribute['name']] = prop
        else:
            properties[attribute['name']] = { 'type': 'array', 'items': prop }
    #construct properties and required elements.
    definition['properties'] = properties
    if len(required) > 0 :
        definition['required'] = required
    #elements can be replaced with identifiers
    wrap_definition = { "anyOf": [ {"type": "string"}, definition ] }
    return wrap_definition

def make_labeled_id():
    """We use a lot of external identifiers, which would usually be "string"
      type in json, but we allow people to make them an object and attach
      a label as well.

      This type is either a string or an object with a string id and
      a string label"""
    definition = { "anyOf": [ {"type": "string"}, {"type":"object", 'properties': {'id': {'type':'string'}, 'label': {'type':'string'}} , 'required': ['id'] } ] }
    return definition

def write_schema(types_and_atts, outfname):
    """Parse the types and attributes to produce a json schema"""
    schema = { '$schema': "http://json-schema.org/schema#", 'definitions': {} }
    #Create definitions in the schema for each entity
    schema['definitions'] = { t['name']: make_def(t)  for t in types_and_atts.values() }
    #make the labeled id element, which is not part of our model per se, but
    # we need in order to validate.
    schema['definitions']['LabeledIRI'] = make_labeled_id()
    #VariantInterpretation created a definition, but because it's the top level
    # class, we need to pull it out of the definitions and add its elements
    # to that top level
    videf = schema['definitions']['VariantPathogenicityInterpretation']
    del schema['definitions']['VariantPathogenicityInterpretation']
    schema['title'] = 'VariantPathogenicityInterpretation'
    schema.update(videf)
    #dump the schema
    with open(outfname,'w') as outf:
        outf.write(json.dumps(schema, indent=4))

def write_value_set(types_and_atts, outname):
    """Write out a list of attributes associated with valuesets to be used
       in validation"""
    keeps = {}
    for t in types_and_atts.values():
        for a in t['attributes']:
            if '@valueSetId' in a and a['@valueSetId'] not in ('','???') :
                keeps[(t['name'],a['name'])] = a['@valueSetId']
    with open(outname,'w') as outf:
        for key,value in keeps.items():
            outf.write('%s\t%s\t%s\n' % (key[0],key[1],value))


def go():
    """Main function for creating json schema."""
    type_url = 'http://dataexchange.clinicalgenome.org/interpretation/master/json/Types'
    t_res = requests.get(type_url)
    json_string = t_res.text
    types_and_atts = json.loads(json_string)
    write_schema(types_and_atts, 'interpretation_schema.json')
    write_value_set(types_and_atts, 'value_set_information.txt')


if __name__ == '__main__':
    go()
