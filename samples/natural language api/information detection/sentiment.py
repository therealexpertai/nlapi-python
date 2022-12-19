# Demonstrates the sentiment detection capability of the expert.ai (Cloud based) Natural Language API

import json
from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "Les viennoiseries du Café de Flore sont une tuerie."

detector = 'sentiment'
language= 'fr'

output = client.detection(body={"document": {"text": text}}, params={'detector': detector, 'language': language})

print("API JSON response:")

print(client.get_json_response())

print("\nCategorization, list of categories (id and hierarchy):")

for category in output.categories:
    print(category.id_, category.hierarchy, sep="\t")

print("\nExtraction, list of records:")

i = 1
for extraction in output.extractions:
    print("\nRecord #{}:".format(i))
    print("Template: {}".format(extraction.template))
    for field in extraction.fields:
        print("Field: {}, value: {}".format(field.name, field.value))
    i = i + 1


