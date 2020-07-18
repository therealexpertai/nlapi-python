# expert.ai Natural Language API for Python

Python client for the [expert.ai Natural Language API](https://developer.expert.ai/). Leverage Natural Language understanding from your Python apps.


Installation
---------------

Clone the repository and run the following script:

```bash
$ cd nlapi-python
$ pip install -r requirements-dev.txt
```

> As good practice it's recommended to work in a isolated Python environment, creating a virtual environment with [virtualenv package](https://virtualenv.pypa.io/en/stable/installation.html) before building the package. You can create an isolated environment with the command

 ```bash
$ virtualenv expertai
$ source expertai/bin/activate
```


Usage
------


Before making requests to the API, you need to create an instance of the `ExpertClient`. You will set your [API Credentials](https://developer.expert.ai/ui/login) as environment variables:

```bash
export EAI_USERNAME=YOUR_USER
export EAI_PASSWORD=YOUR_PASSWORD
```

and then you can code as follows:

```python
from lib.expert import ExpertClient
# Instantiate the client Using your API key
eai = ExpertClient()
```


### Requests

From the client instance, you can call any endpoint (check the [available endpoints](#available-endpoints) below). For example, you can get [named entities](#document-analysis) from a text document:


```python
text = 'Facebook is looking at buying U.S. startup for $6 million' 
language= 'en'

##get Named Entities
response = eai.specific_resource_analysis,
      body={"document": {"text": text}},
      params={'language': language, 'resource': 'entities'}
   )
```

or to [classify it](#document-classification) according the IPTC Media Topics taxonomy:


```python
text = 'Facebook is looking at buying U.S. startup for $6 million' 
language= 'en'

##get Media Topics Classification
response = eai.iptc_media_topics_classification,
      body={"document": {"text": text}},
      params={'language': language}
```


### Responses

The response object returned by every endpoint call is a JSON file as detailed in the [Output reference](https://docs.expert.ai/nlapi/v1/reference/output/):

For Named Entity extraction:

```python
pprint(response.json)
```

```json
{
  "content": "Facebook is looking at buying U.S. startup for $6 million",
  "entities": [
    {
      "lemma": "6,000,000 dollar",
      "positions": [
        {
          "end": 57,
          "start": 47
        }
      ],
      "syncon": -1,
      "type": "MON"
    },
    {
      "lemma": "Facebook Inc.",
      "positions": [
        {
          "end": 8,
          "start": 0
        }
      ],
      "syncon": 288110,
      "type": "COM"
    }
  ],
  "knowledge": [
    {
      "label": "organization.company",
      "properties": [
        {
          "type": "DBpediaId",
          "value": "dbpedia.org/page/Facebook,_Inc."
        },
        {
          "type": "WikiDataId",
          "value": "Q380"
        }
      ],
      "syncon": 288110
    }
  ],
  "language": "en",
  "version": "sensei: 3.1.0; disambiguator: 15.0-QNTX-2016"
}
```
For Document classification:

```python
pprint(response.json)
```

```json
{
  "categories": [
    {
      "frequency": 64.63,
      "hierarchy": [
        "Economy, business and finance",
        "Business information",
        "Strategy and marketing",
        "Merger or acquisition"
      ],
      "id": "20000204",
      "label": "Merger or acquisition",
      "namespace": "iptc_en_1.0",
      "positions": [
        {
          "end": 8,
          "start": 0
        },
        {
          "end": 29,
          "start": 23
        },
        {
          "end": 42,
          "start": 35
        }
      ],
      "score": 1335,
      "winner": true
    }
  ],
  "content": "Facebook is looking at buying U.S. startup for $6 million",
  "language": "en",
  "version": "sensei: 3.1.0; disambiguator: 14.5-QNTX-2016"
}
```


Available endpoints
------------------------

These are all the endpoints of the API. For more information about each endpoint, check out the [API documentation](https://docs.expert.ai/nlapi/v1/).


### Document Analysis


* [Deep linguistic analysis](https://docs.expert.ai/nlapi/v1/reference/output/linguistic-analysis/)	
* [Keyphrase extraction](https://docs.expert.ai/nlapi/v1/reference/output/keyphrase-extraction/)	
* [Named entities recognition](https://docs.expert.ai/nlapi/v1/reference/output/entity-recognition/)
* [Full document analysis](https://docs.expert.ai/nlapi/v1/reference/output/full-analysis/)


### Document Classification


* [IPTC Media Topics classification](https://docs.expert.ai/nlapi/v1/reference/output/classification/)



Demo mode
--------

You find a demo script in the package that you can use as starting poing for developing your application.

```bash
python demo.py
```
