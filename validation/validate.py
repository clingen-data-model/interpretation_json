from jsonschema import validate
import json
import sys

def go(in_json):
    with open('interpretation_schema.json','r') as inf:
        schema = json.load(inf)
    with open(in_json,'r') as inf:
        input_json = json.load(inf)
    validate(input_json ,schema)


if __name__ == '__main__':
    go(sys.argv[1])
