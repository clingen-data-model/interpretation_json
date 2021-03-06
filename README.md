# interpretation_json
Python library for creating JSON documents conforming to the DMWG interpretation model.

## Introduction

ClinGen interpretations for the clinical pathogenicity of sequence variants are expressed in a JSON-LD format described [here](http://dataexchange.clinicalgenome.org/interpretation/master/index.html). These documents contain both the interpretation as well as the evidence and reasoning that led to the interpretation.

This library facilitates the creation of documents in this format by allowing developers to build documents in code, and then serialize those documents to JSON-LD. Types in JSON-LD are represented as classes in python, with appropriate getters and setters for the attributes defined in the model. In addition, the library contains numerous convenience methods for creating complex structures with minimal coding.

The fundamental definition of the ClinGen model is a series of JSON files hosted at the above site. To create python classes that represent the JSON types, a code generation script is included with this package. However, most users will not need to use this script.

## Installation

 1. (Optional) Generate the python library. This is only required if the model definition has changed. To generate run ```python3 generate_interpretation_library.py``` from the clingen_interpretation folder.

 2. Install the module locally with ```python3 setup.py install``` from the project root. If necessary, this will also install prerequisites.

## Example and Use

A full example of using the library to construct a JSON-LD interpretation is included in examples.py
The structure of an interpretation is described more fully [here](http://dataexchange.clinicalgenome.org/interpretation/master/index.html).

### VariantPathogenicityInterpretation


The root of an interpretation document is a VariantPathogenicityInterpretation, which contains the pathogenicity of a particular variant for a particular disease. A VariantPathogenicityInterpretation requires an identifier; it is up to the user to manage these identifiers. In this example, we create an interpretation with a fictitious id:
```
def create_example():
    #Create the root interpretation
    interpretation_id = 'http://example.com/interpretation_1'
    interpretation = VariantPathogenicityInterpretation(interpretation_id)
```

Now we want to add the necessary attributes to the interpretation. In particular we want to add an allele, a condition, and a pathogenicity. Later we will also add the rules and data that were used to derive the interpretation.

### Variants

Alleles in the interpretation model are represented using the ClinGen allele model as described [here](http://dataexchange.clinicalgenome.org/allele/master/index.html). In particular, the allele about which an interpretation is made is a Canonical Allele: a stable identifier for the allele independent of genome reference version. Given the requirement of either a ClinGen Allele Registry identifier or a set of hgvs names one of which must be a GRCh38 version, we use either of those to construct a canonical allele in the correct format, preserving the source identifier and hgvs representations for each contextual allele that comprise it. The best solution for canonicalizing an allele is the [ClinGen Allele Registry](http://reg.genome.network/allele), however it is possible to construct a canonical allele from the set of hgvs names as well, even though they may not have the full set of detailed information. At this site, we can look up an allele by one of its HGVS representations, returning a JSON. This JSON can then be passed to the constructor for a Variant and added to our interpretation.

The required structured set of named arguments that must be passed to the CanonicalAllele() constructor are as follows:
identifier -> a string in the form ClinVar:<variationId> or CAR:<caid>. One of those two is required.
hgvs_names -> an array of keyed values where the keys are 'GRCh38', 'GRCh37', 'NCBI36' or 'others'. The first three genome build keys would each have a single hgvs string representing the variant for that build. The 'others' key would be an array of hgvs strings that represent alternative forms of the variant.
dbsnp_ids -> an optional array of dbnsnp id strings without the "rs" prefix.
preferred_name -> an optional (but highly recommended) string that is the preferred human-readable name for the variant - typically hgvs. It should start with the refseq accession that is to be used to define the 'preferred' contextual allele from the list of hgvs_names.



```
def create_allele():
    # For this example we will use a ClinVar id as source with the associated hgvs_names, dbsnp_ids and preferred_name
    identifier = "ClinVar:11852"
    hgvs_names = {  "GRCh37": "NC_000011.9:g.76869378G>A", \
                    "GRCh38": "NC_000011.10:g.77158332G>A", \
                    "others": [ \
                        "NG_009086.1:g.35069G>A", \
                        "NM_000260.3:c.905G>A", \
                        "NP_000251.3:p.Arg302His", \
                        "Q13402:p.Arg302His"]}
    dbsnp_ids = [ "41298135" ]
    preferred_name =  "NM_000260.3(MYO7A):c.905G>A (p.Arg302His)"

    return CanonicalAllele( identifier=identifier, \
                            hgvs_names=hgvs_names, \
                            dbsnp_ids=dbsnp_ids, \
                            preferred_name=preferred_name )

def create_example():
    ...
    allele = create_allele()
    interpretation.set_variant(allele)
```

### Conditions and Diseases

In the ClinGen interpretation model, variants are associated with conditions. A condition is a flexible structure that can be used to aggregate multiple diseases or phenotypes. In this example, we will show the most common case: a condition that is a single disease. Diseases are defined through a combination of an ontology (MONDO, Orphanet), a code (the code for the disease in that ontology), and a human readable name (also from the ontology).

Diseases, along with many other controlled vocabularies, are modeled in ClinGen interpretations using Codings and Codeable Concepts, structures that come from the HL7 project [FHIR](https://www.hl7.org/fhir/). While these classes provide some nice features, they can be somewhat complicated to work with. So rather than requiring users of the interpretation model to implement them directly, we provide some utility methods for creating them. One such method is ```create_disease```. Here we use this utility method to create the disease, create the Condition from the disease, and attach the condition to the interpretation:


```
def create_condition():
    ontology = 'http://purl.obolibrary.org/obo/'
    code = 'MONDO_0019501'
    name = 'Usher syndrome'
    disease = create_disease(ontology, code, name)

    condition = GeneticCondition()
    condition.add_disease(disease)
    condition.set_inheritancePattern( "Autosomal recessive inheritance" )

    return condition


def create_example():
    ...
    condition = create_condition()
    interpretation.add_condition(condition)
```

### Significance (Pathogenicity)

We now have an interpretation relating a variant to a condition, and we want to say that this variant was found to be pathogenic. The pathogenicity is a coding, but you are not required to create your own coding entity. if you call ```interpretation.set_clinicalSignificance()``` with the id, code, or display value of a valid coding, the library will complete the structure. The allowed values for the display are "Pathogenic", "Likely Pathogenic", "Uncertain Significance", "Likely Benign", and "Benign". Here we will use "Pathogenic":

```
def create_example():
    ...
    interpretation.set_clinicalSignificance('Pathogenic')
```

### Contributions and Agents

Many elements in the ClinGen interpretation model allow the user to attach information related to the provenance of that element by attaching a Contribution. A Contribution notes who participated in the creation of the element, when they completed their contribution, and their role in creating it. The "who" portion of a contribution is an Agent. An Agent has a user managed ID, as well as a name and description. Role is defined as a codeable concept, meaning that if one of the known codes is passed into the Agent creator, the correct Coding will be found. If an unknown code is passed in, a free-text style CodeableConcept will be created. In other words, if you want to track a contribution role that we have not created a code for, you may enter that role, and use it without problems. The pre-existing values of role are 'curator', 'approver', 'publisher' and 'assessor', which are represented with the package constants PROP_CURATOR_ROLE, PROP_APPROVER_ROLE, PROP_PUBLISHER_ROLE and PROP_ASSESSOR_ROLE. Here, we will create a fictional agent, and a contribution stating that this agent was the interpreter. Current, the timestamp of a contribution is not interpreted as a datetime by the library, but simply as a string that is passed into the output JSON. It is expected, however, that the programmer will use a standard datetime format.

```
def create_agent():
    agent_id = 'http://examples.com/agent1'
    agent = Agent(agent_id)
    agent.set_name('Gregor Mendel')
    return agent

def create_example():
    agent = create_agent()
    when = '2017-01-24T16:16:59.073653+00:00'
    contribution = create_contribution(agent, when, PROP_APPROVER_ROLE)
    interpretation.add_contribution(contribution)
```

### Assessments

At this point, we have a fully specified interpretation. We have the root node (the VariantInterpretation), which is now stating that a given allele is pathogenic for a given disease. Further, we know who made that determination and when. However, we do not yet know the reasoning or data that led the Agent to this interpretation. This extra information can be provided in assessments.

In the AMCG Guidelines for the interpretation of potentially pathogenic variants, interpretations are based on a series of criteria, which are individually evaluated using various types of data. These criteria, which are designated by codes such as "PVS1" or "PP3" can be "met" indicating that the available data meets the criteria, providing evidence about the pathogenicity of the variant. In a real interpretation, many of these criteria may be assessed and attached to the interpretation, but in this case, we will show only a single example.

An assessment has a user-managed ID. Preferably, this would be an IRI that would dereference to a representation of the assessment, though this is not required. The assessment also contains the criteria that was assessed, and the outcome of the assessment, as well as other information, such as the allele being assessed, and a text description of the assessment.

The list of ACMG criteria is available using the ```get_criteria()``` method, which returns a dictionary mapping from the criteria code to the particular criteria structure. Outcomes are codings, and so can be specified just by their code or display value. In the example below we encode an assessment of the given variant for PM2 and found that it is met, providing evidence for calling the variant pathogenic.

When the assessment is attached to the interpretation, a strength parameter must also be set: this defines how much evidence the met assessment provides to the interpretation. Criteria define a default strength, which will most often be used, but ACMG guideline specifically allow an assessor to overrule the default strength if the evidence is sufficient.

```
def create_assessment(allele,agent):
    assessment_id = 'http://examples.com/assessment1'
    assessment = CriterionAssessment( assessment_id )
    criteria = read_criteria()
    criterion = criteria['PM2']
    assessment.set_criterion(criterion)
    #The library will check the input against allowed codings
    assessment.set_statementOutcome('met')
    assessment.set_variant(allele)
    when = '2017-01-24T16:07:57.082704+00:00'
    contribution = create_contribution(agent, when, DMWG_ASSESSOR_ROLE)
    assessment.add_contribution(contribution)
    return assessment

def create_example():
    ...
    assessment = create_assessment(allele,agent)
    strength = assessment.get_criterion().get_defaultStrength()
    add_criterion_assessment(interpretation,assessment,strength)
```

### Evidence

We now are representing that the interpretation is based on a series of criterion assessments (in this example, only a single one). Now, we also want to be able to express the evidence that led to this assessment. The interpretation model specifies a large number of possible data types for this evidence. Many examples of the use of evidence in assessments is shown in the [ClinGen interpretation documentation](http://dataexchange.clinicalgenome.org/interpretation/master/index.html). CriterionAssessments can contain many different pieces of evidence. In the current example, we will simply show one example bit of evidence, an allele frequency from ExAC. In the example, note that the values for population and ascertainment are passed in a strings. The library recognizes the strings and creates codeable concepts from them. Also note that here we are creating a curation contribution node, declaring the agent that contributed to finding the information. Here, that is a computational agent: a data loading program. We could go further and include an contribution for the person that wrote or ran the program; the level at which contributions are captured is up to the implementer.

```
def create_computational_agent():
    agent_id = 'http://examples.com/agent2'
    agent = Agent(agent_id)
    agent.set_name('ExAC Data Loader v1')
    return agent

 #Note numbers here are not correct; they are only for examples.
def create_frequency_data(allele,agent):
    frequency = PopulationAlleleFrequencyStatement()
    #the library will look up the code
    frequency.set_ascertainment('ExAC ascertainment method')
    #the library will look up the code
    frequency.set_population('GNOMAD:nfe')
    frequency.set_allele(allele)
    frequency.set_alleleCount(0)
    frequency.set_alleleNumber(1000)
    #The library will not calculate the frequency for you
    frequency.set_alleleFrequency(0)
    when = '2016-01-24T16:07:57.082704+00:00'
    contribution = create_contribution(agent, when, DMWG_CURATOR_ROLE)
    frequency.add_contribution(contribution)
    return frequency

def create_example():
    ...
    frequency = create_frequency_data(allele,create_computational_agent())
    add_evidenceItems( assessment, [frequency] )
```

### Serialization

We have now created, in code, a structure including an interpretation, the criteria assessments that contributed to the interpretation, and the data that contributed to the assessments. At each stage we have captured information about contributions. Now we would like to export this structure to a JSON document. This is accomplished with the following code:

```
    outf = file('example1.json','w')
    json.dump(interpretation, outf, sort_keys = True, indent=4, \
            separators=(',',': '), cls = InterpretationEncoder,\
            out_style = 'first')
    outf.close()
```

The only unusual portion here is the ```out_style```, which describes how often repeated nodes are expanded. If it is set to 'full', then a node such as variant, which may repeat throughout the document will always be expanded. If it is set to 'first', then the first time it is encountered during serialization it will be fully expanded, and after that each time it will be represented only by the ID of the entity.
