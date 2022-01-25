# Demonstrates the Writeprint detection capability of the expert.ai (Cloud based) Natural Language API

import json
from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "My dear Bagginses and Boffins, Tooks and Brandybucks, Grubbs, Chubbs, Hornblowers, Bolgers, Bracegirdles and Proudfoots. Today is my one hundred and eleventh birthday! Alas, eleventy-one years is far too short a time to live among such excellent and admirable hobbits. I don't know half of you half as well as I should like, and I like less than half of you half as well as you deserve."

detector = 'writeprint'
language= 'en'

output = client.detection(body={"document": {"text": text}}, params={'detector': detector, 'language': language})

# Output extra data containing the JSON-LD object

print("extra_data: ",json.dumps(output.extra_data, indent=4, sort_keys=True))
