# Demonstrates the Temporal information detection capability of the expert.ai (Cloud based) Natural Language API

import json
from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "I went to Australia for the first time in 1998. Ten years later I returned to stay there, but from 2011 to 2013 I lived in New Zealand."

detector = 'temporal-information'
language= 'en'

output = client.detection(body={"document": {"text": text}}, params={'detector': detector, 'language': language})

# Output extra data containing the JSON-LD object

print("extra_data: ",json.dumps(output.extra_data, indent=4, sort_keys=True))
