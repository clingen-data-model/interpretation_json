# interpretation_json
Python library for creating JSON documents conforming to the DMWG interpretation model.

## Introduction

ClinGen interpretations for the clinical pathogenicity of sequence variants are expressed in a JSON-LD format described [here](http://datamodel.clinicalgenome.org/interpretation/master/index.html).  These documents contain both the interpretation as well as the evidence and reasoning that led to the interpretation.

This library facilitates the creation of documents in this format by allowing developers to build documents in code, and then serialize those documents to JSON-LD.  Types in JSON-LD are represented as classes in python, with appropriate getters and setters for the attributes defined in the model.  In addition, the library contains numerous convenience methods for creating complex structures with minimal coding.

The fundamental definition of the ClinGen model is a series of JSON files hosted at the above site.   To create python classes that represent the JSON types, a code generation script is included with this package.  However, most users will not need to use this script.

## Installation

 1. (Optional) Generate the python library.   This is only required if the model definition has changed.

 2. Install the module locally with ```python setup.py install```.   If necessary, this will also install prerequisites.

## Example and Use

A full example of using the library to construct a JSON-LD interpretation is included in examples.py
The structure of an interpretation is described more fully [here](http://datamodel.clinicalgenome.org/interpretation/master/index.html).

The root of an interpretation document is a VariantInterpretation, which contains the pathogenicity of a particular variant for a particular disease. A VariantInterpretation requires an identifier; it is up to the user to manage these identifiers.  In this example, we create an intepretation with a fictitious id:
```
def create_example():
    #Create the root interpretation
    interpretation_id = 'http://example.com/interpretation_1'
    interpretation = VariantInterpretation(interpretation_id)
```

Now we want to add the necessary attributes to the interpretation.  In particular we want to add an allele, a condition, and a pathogenicity.  Later we will also add the rules and data that were used to derive the interpretation.

Alleles in the interpretation model are represented using the ClinGen allele model as described [here](http://datamodel.clinicalgenome.org/allele/master/index.html].   In particular, the allele about which an interpretation is made is a Canonical Allele: a stable identifier for the allele independent of genome reference version.   Given a particular representation, such as an HGVS, we must obtain a canonical allele, and represent it in the correct format.  The best solution for canonicalizing an allele is the [ClinGen Allele Registry](http://reg.genome.network/allele).  At this site, we can look up an allele by one of its HGVS representations, returning a JSON.  This JSON can then be passed to the constructor for a Variant and added to our interpretation.
  

