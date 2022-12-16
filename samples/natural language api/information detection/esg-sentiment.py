# Demonstrates the ESG Sentiment detection capability of the expert.ai (Cloud based) Natural Language API
# See: https://docs.expert.ai/nlapi/latest/guide/detection/esg-sentiment/

import json
from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "Data centers have an enormous environmental impact."

detector = 'esg-sentiment'
language= 'en'

output = client.detection(body={"document": {"text": text}}, params={'detector': detector, 'language': language})

print("Categorization, list of categories (id and hierarchy):")

for category in output.categories:
    print(category.id_, category.hierarchy, sep="\t")

print("\nExtraction, list of records:")

i = 1
for extraction in output.extractions:
    print("Record #{}, template {}:".format(i, extraction.template))
    for field in extraction.fields:
        print("{} = {}".format(field.name, field.value))
    i = i + 1