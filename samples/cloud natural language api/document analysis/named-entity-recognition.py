# Demonstrates the named entity recognition capability of the expert.ai (Cloud based) Natural Language API performed by the 'entities' resource

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "Michael Jordan was one of the best basketball players of all time. Scoring was Jordan's stand-out skill, but he still holds a defensive NBA record, with eight steals in a half."
language= 'en'

output = client.specific_resource_analysis(body={"document": {"text": text}}, params={'language': language, 'resource': 'entities'})

print (f'{"ENTITY":{50}} {"TYPE":{10}}')
print (f'{"------":{50}} {"----":{10}}')

for entity in output.entities:
    print (f'{entity.lemma:{50}} {entity.type_:{10}}')