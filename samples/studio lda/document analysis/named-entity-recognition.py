# Demonstrates the named entity recognition capability of the expert.ai (local) Edge NL API performed by the 'entities' resource wrapped in the `entities` method of the client.

from expertai.nlapi.edge.client import ExpertAiClient
client = ExpertAiClient()

text = "Michael Jordan was one of the best basketball players of all time. Scoring was Jordan's stand-out skill, but he still holds a defensive NBA record, with eight steals in a half."

output = client.named_entity_recognition(text)

print (f'{"ENTITY":{50}} {"TYPE":{10}}')
print (f'{"------":{50}} {"----":{10}}')

for entity in output.entities:
    print (f'{entity.lemma:{50}} {entity.type_:{10}}')