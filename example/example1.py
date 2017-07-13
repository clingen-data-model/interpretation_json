from clingen_interpretation.interpretation_generated import *
from clingen_interpretation.interpretation_extras import *
from clingen_interpretation.interpretation_constants import *
from clingen_interpretation.Allele import Variant
import requests

def create_allele():
    #For this example, we will use this HGVS
    hgvs = 'NC_000014.8:g.23898488G>A'
    # send a GET request with parameter
    url = 'http://reg.genome.network/allele?hgvs='
    # convert symbol > to special code %3E
    url += requests.utils.quote(hgvs)
    #retreive the ClinGen 
    res = requests.get(url)
    txt = res.text
    cardata = json.loads(txt)
    allele = Variant(cardata)
    return allele


def create_example():
    #Create the root interpretation
    interpretation_id = 'http://example.com/interpretation_1'
    interpretation = VariantInterpretation(interpretation_id)
    allele = create_allele()
    interpretation.set_variant(allele)

    #Write interpretation to file
    outf = file('example1.json','w')
    json.dump(interpretation, outf, sort_keys = True, indent=4, \
            separators=(',',': '), cls = InterpretationEncoder,\
            out_style = 'first')
    outf.close()

if __name__ == '__main__':
    create_example()