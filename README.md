<img style="float: right;" src="https://docs.expert.ai/logo.png" width="150px">


# expert.ai Natural Language API for Python


Python client for the expert.ai Natural Language API leverage Natural Language understanding for your Python apps.
You can use either the [cloud API interface](https://docs.expert.ai/nlapi/v2) or the [Edge API interface](https://docs.expert.ai/nlapi/v2). Either way you have to create a [developer account](https://developer.expert.ai/ui) on expert.ai.

 


## Installation (development)

You can use pip to install the library:

```bash
$ pip install expertai-nlapi
```


## Installation (contributor)

Clone the repository and run the following script:

```bash
$ cd nlapi-python
$ pip install -r requirements-dev.txt
```

> As good practice it's recommended to work in an isolated Python environment, creating a virtual environment with [virtualenv package](https://virtualenv.pypa.io/en/stable/installation.html) before building the package. You can create your environment with the command

 ```bash
$ virtualenv expertai
$ source expertai/bin/activate
```


## Usage


Before making requests to the API, you need to create an instance of the `ExpertClient`. You have to set your [API Credentials](https://developer.expert.ai/ui/login) as environment variables:

For Linux:
```bash
export EAI_USERNAME=YOUR_USER
export EAI_PASSWORD=YOUR_PASSWORD
```

For Windows:
```bash
SET EAI_USERNAME=YOUR_USER
SET EAI_PASSWORD=YOUR_PASSWORD
```


or to define them as part of your code

```python
import os
os.environ["EAI_USERNAME"] = 'your@account.email'
os.environ["EAI_PASSWORD"] = 'yourpwd'
```


Currently, the API supports five languages, i.e. English, French, Spanish, Italian and German. You have to define the text you want to process and the language model to use for the analysis.


```python
# cloud API
from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()
```

or

```python
# Edge API
from expertai.nlapi.edge.client import ExpertAiClient
client = ExpertAiClient()
```

```python
text = 'Facebook is looking at buying an American startup for $6 million based in Springfield, IL .' 
language= 'en'
```

### Quick run
Let's start with the first API call just sending the text. 


```python
# cloud API
document = client.specific_resource_analysis(
    body={"document": {"text": text}}, 
    params={'language': language, 'resource': 'disambiguation'
})
```

or

```python
# Edge API
document = client.deep_linguistic_analysis(text)
```


This analysis returns all the information that the Natural Language engine comprehended from the text. Let's see in the details the API response.

### Tokenization & Lemmatization
Lemmatization looks beyond word reduction, and considers a language's full vocabulary to apply a *morphological analysis* to words. The lemma of 'was' is 'be' and the lemma of 'mice' is 'mouse'. Further, the lemma of 'meeting' might be 'meet' or 'meeting' depending on its use in a sentence.


```python
print (f'{"TOKEN":{20}} {"LEMMA":{8}}')

for token in document.tokens:
    print (f'{text[token.start:token.end]:{20}} {token.lemma:{8}}')
```

    TOKEN                LEMMA   
    Facebook             Facebook Inc.
    is                   is      
    looking at           look at 
    buying               buy     
    an                   an      
    American             American
    startup              startup 
    for                  for     
    $6 million           6,000,000 dollar
    based                base    
    in                   in      
    Springfield, IL      Springfield
    .                    .       
    

###  Part of Speech 
We also looked at the part-of-speech information assigned to each token; PoS values are from the [Universal Dependencies](https://universaldependencies.org/) framework


```python
print (f'{"TOKEN":{18}} {"PoS":{4}}')

for token in document.tokens:
    print (f'{text[token.start:token.end]:{18}} {token.pos:{4}}  ' )
```

    TOKEN              PoS   
    Facebook           PROPN  
    is                 AUX    
    looking at         VERB   
    buying             VERB   
    an                 DET    
    American           ADJ    
    startup            NOUN   
    for                ADP    
    $6 million         NOUN   
    based              VERB   
    in                 ADP    
    Springfield, IL    PROPN  
    .                  PUNCT   
     

### Dependency Parsing information
The analysis returns the dependency parsing information assigned to each token, using the Universal Dependencies framework as well.


```python
print (f'{"TOKEN":{18}} {"Dependency label":{8}}')

for token in document.tokens:
    print (f'{text[token.start:token.end]:{18}} {token.dependency.label:{4}} ' )
```

    TOKEN              Dependency label
    Facebook           nsubj 
    is                 aux  
    looking at         root 
    buying             advcl 
    an                 det  
    American           amod 
    startup            obj  
    for                case 
    $6 million         obl  
    based              acl  
    in                 case 
    Springfield, IL    obl  
    .                  punct 
    

### Named Entities
Going a step beyond tokens, *named entities* add another layer of context.  Named entities are obtained with the `entities` analysis.

```python
# cloud API
document = client.specific_resource_analysis(
    body={"document": {"text": text}}, 
    params={'language': language, 'resource': 'entities'})
```

or

```python
# Edge API
document = client.named_entity_recognition(text)
```


```python
print (f'{"ENTITY":{40}} {"TYPE":{10}})
       
for entity in document.entities:
    print (f'{entity.lemma:{40}} {entity.type_{10}}')
```

    ENTITY               TYPE
    6,000,000 dollar     MON        
    Springfield          GEO        
    Facebook Inc.        COM
    

In addition to the entity type, the API provides some metadata from Linked Open Data sources such as WikiData and GeoNames.
For example, you can get the open data connected with the entity `Springfield, IL` 


```python
print(document.entities[1].lemma)
```

    Springfield
    


```python
for entry in document.knowledge:
    if (entry.syncon == document.entities[1].syncon):
            for prop in entry.properties:
                print (f'{prop.type_:{12}} {prop.value:{30}}')
    
```

    Coordinate   Lat:39.47.58N/39.799446;Long:89.39.18W/-89.654999
    DBpediaId    dbpedia.org/page/Springfield  
    GeoNamesId   4250542                       
    WikiDataId   Q28515                        
    

Springfield has been recognized as [Q28515](https://www.wikidata.org/wiki/Q28515) on Wikidata, that is the Q-id for Springfield, IL (i.e.not for Springfield in Vermont o in California)

### Key Elements
*Key elements* are obtained with the `relevants` analysis and identified from the document as main sentences, main keywords, main lemmas and relevant topics; let's focus on the main lemmas of the document; each lemma is provided with a relevance score.

```python
# cloud API
document = client.specific_resource_analysis(
    body={"document": {"text": text}}, 
    params={'language': language, 'resource': 'relevants'})
```

or

```python
# Edge API
document = client.keyphrase_extraction(text)
```

```python
print (f'{"LEMMA":{20}} {"SCORE":{5}} ')
       
for mainlemma in document.main_lemmas:
    print (f'{mainlemma.value:{20}} {mainlemma.score:{5}}')
```

    LEMMA                SCORE 
    Facebook Inc.         43.5
    startup               40.4
    Springfield             15
    
### Sentiment

*Sentiment* is obtained with the `sentiment` analysis and it determines how positive or negative the tone of the text is.

```
text='Today is a good day. I love to go to mountain.'
```


```python
# cloud API
document = client.specific_resource_analysis(
    body={"document": {"text": text}}, 
    params={'language': language, 'resource': 'sentiment'})
```

or

```python
# Edge API
document = client.sentiment(text)
```

```python
print("sentiment:", response.sentiment.overall)
```

### Relations

*Relations* are obtained with the `relations` analysis and they identify labels concepts expressed in the text with their semantic role.


```
text='Barack Obama is the former president of United States of America.'
```

```python
# cloud API
document = client.specific_resource_analysis(
    body={"document": {"text": text}}, 
    params={'language': language, 'resource': 'relations'})
```

or

```python
# Edge API
document = client.relations(text)
```

```python
for rel in document.relations:
   print("Verb:", rel.verb.lemma)
   for r in rel.related:
      print("Relation:", r.relation, "Lemma:", r.lemma )
```

### Classification
Let's see how to classify documents according to the [**IPTC Media Topics Taxonomy**](https://iptc.org/standards/media-topics/); we're going to use a text that has more textual information and then we'll use the matplot lib to show a bar chart with the categorization results


```python
text = """Strategic acquisitions have been important to the growth of Facebook (FB). 
Mark Zuckerberg founded the company in 2004, and since then it has acquired scores of companies, 
ranging from tiny two-person start-ups to well-established businesses such as WhatsApp. For 2019, 
Facebook reported 2.5 billion monthly active users (MAU) and $70.69 billion in revenue."""
```


```python
# cloud API
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('ggplot')

taxonomy='iptc'

document = client.classification(body={"document": {"text": text}}, params={'language': language})

categories = []
scores = []

print (f'{"CATEGORY":{27}} {"IPTC ID":{10}} {"FREQUENCY":{8}}')
for category in document.categories:
    categories.append(category.label)
    scores.append(category.frequency)
    print (f'{category.label:{27}} {category.id_:{10}}{category.frequency:{8}}')
    
    
```

or

```python
# Edge API
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('ggplot')

document = client.classification(text)

categories = []
scores = []

print (f'{"CATEGORY":{27}} {"ID":{10}} {"FREQUENCY":{8}}')
for category in document.categories:
    categories.append(category.label)
    scores.append(category.frequency)
    print (f'{category.label:{27}} {category.id_:{10}}{category.frequency:{8}}')
    
    
```

    CATEGORY                    ID           FREQUENCY
    Earnings                    20000178     29.63
    Social networking           20000769     21.95

```python
plt.bar(categories, scores, color='#17a2b8')
plt.xlabel("Categories")
plt.ylabel("Frequency")
plt.title("Media Topics Classification")

plt.show()

```


    
![png](https://raw.githubusercontent.com/therealexpertai/nlapi-python/master/chart_output.png)  


Good job! You're an expert in the expert.ai community! :clap: :tada:

Check out other language SDKs available on our [Github page](https://github.com/therealexpertai).


## Capabilites

These are all the analysis and classification capabilities of the API.

### Cloud API interface

#### Document Analysis

* [Full document analysys](https://docs.expert.ai/nlapi/v2/guide/full-analysis/)
* Partial analyses:

    * [Deep linguistic analysis (text subdivision, part-of-speech tagging, morphological analysis, lemmatization, syntactic analysis, semantic analysis)](https://docs.expert.ai/nlapi/v2/guide/linguistic-analysis/)
    * [Keyphrase extraction](https://docs.expert.ai/nlapi/v2/guide/keyphrase-extraction/)
    * [Named entities recognition](https://docs.expert.ai/nlapi/v2/guide/entity-recognition/)
    * [Relation extraction](https://docs.expert.ai/nlapi/v2/guide/relation-extraction/)
    * [Sentiment analysis](https://docs.expert.ai/nlapi/v2/guide/sentiment-analysis/)

#### Document Classification

* [IPTC Media Topics and geographic classification](https://docs.expert.ai/nlapi/v2/guide/classification/)

### Edge API interface

++++++++++++++++++  TO DO !!! - cambiare i link +++++++++++++++++++++

#### Document Analysis

* [Full document analysys](https://docs.expert.ai/nlapi/v2/guide/full-analysis/)
* Partial analyses:

    * [Deep linguistic analysis (text subdivision, part-of-speech tagging, morphological analysis, lemmatization, syntactic analysis, semantic analysis)](https://docs.expert.ai/nlapi/v2/guide/linguistic-analysis/)
    * [Keyphrase extraction](https://docs.expert.ai/nlapi/v2/guide/keyphrase-extraction/)
    * [Named entities recognition](https://docs.expert.ai/nlapi/v2/guide/entity-recognition/)
    * [Relation extraction](https://docs.expert.ai/nlapi/v2/guide/relation-extraction/)
    * [Sentiment analysis](https://docs.expert.ai/nlapi/v2/guide/sentiment-analysis/)

#### Document Classification

* [Classification](https://docs.expert.ai/nlapi/v2/guide/classification/)

#### Document Extraction

* [Extraction](https://docs.expert.ai/nlapi/v2/guide/extraction/)

