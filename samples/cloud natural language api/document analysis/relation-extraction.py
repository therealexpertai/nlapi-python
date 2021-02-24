# Demonstrates the relation extraction capability of the expert.ai (Cloud based) Natural Language API performed by the 'relations' resource

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "Michael Jordan was one of the best basketball players of all time. Scoring was Jordan's stand-out skill, but he still holds a defensive NBA record, with eight steals in a half." 
language= 'en'

output = client.specific_resource_analysis(
    body={"document": {"text": text}}, 
    params={'language': language, 'resource': 'relations'
})

# Output relations' data

print("Output relations' data:");

for relation in output.relations:
    print(relation.verb.lemma, ":");
    for related in relation.related:
        print("\t", "(", related.relation, ")", related.lemma);
