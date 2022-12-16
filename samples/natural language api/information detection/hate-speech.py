# Demonstrates the Hate speech detection capability of the expert.ai (Cloud based) Natural Language API
# See: https://docs.expert.ai/nlapi/latest/guide/detection/hate-speech/

import json
from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "We should hang John Doe"

detector = 'hate-speech'
language= 'en'

output = client.detection(body={"document": {"text": text}}, params={'detector': detector, 'language': language})

print("Categorization, list of categories (id and hierarchy):")

for category in output.categories:
    print(category.id_, category.hierarchy, sep="\t")

print("\nExtraction, list of records (record template: Hate_speech_detection):")

i = 1
for extraction in output.extractions:
    print("Record #{}:".format(i))
    for field in extraction.fields:
        print("{} = {}".format(field.name, field.value))
    i = i + 1