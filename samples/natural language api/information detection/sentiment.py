# Demonstrates the Personally Identifiable Information (PII) detection capability of the expert.ai (Cloud based) Natural Language API

import json
from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "Les viennoiseries du Café de Flore sont une tuerie."

detector = 'sentiment'
language= 'fr'

output = client.detection(body={"document": {"text": text}}, params={'detector': detector, 'language': language})

print(client.get_json_response())


