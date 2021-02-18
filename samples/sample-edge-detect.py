import json
from expertai.nlapi.edge.client import ExpertAiClient
client = ExpertAiClient()

text = "Matteo Renzi lives in Rome"
output = client.detect(text)

#print(client.get_json_response())
# Output arrays size
print("Output arrays size:")
print("knowledge: ", len(output.knowledge))
print("extractions: ", len(output.extractions))
print("paragraphs: ", len(output.paragraphs))
print("sentences: ", len(output.sentences))
print("phrases: ", len(output.phrases))
print("tokens: ", len(output.tokens))
print("entities: ", len(output.entities))
print("extradata: ",json.dumps(output.extra_data, indent=4, sort_keys=True))
print ("http POST response",json.dumps(client.get_json_response(), indent=4, sort_keys=True))