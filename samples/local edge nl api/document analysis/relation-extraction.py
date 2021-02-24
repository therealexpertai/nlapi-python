# Demonstrates the relation extraction capability of the expert.ai (local) Edge NL API performed by the 'relations' resource wrapped in the `relations` method of the client.

from expertai.nlapi.edge.client import ExpertAiClient
client = ExpertAiClient()

text = "Michael Jordan was one of the best basketball players of all time. Scoring was Jordan's stand-out skill, but he still holds a defensive NBA record, with eight steals in a half." 

output = client.relations(text)

# Output relations' data

print("Output relations' data:");

for relation in output.relations:
    print(relation.verb.lemma, ":");
    for related in relation.related:
        print("\t", "(", related.relation, ")", related.lemma);
