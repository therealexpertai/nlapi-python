from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "     John Smith lives in Rome"
language= 'en'

output = client.detect(body={"document": {"text": text}}, params={'language': language,'detector':'pii'})


#print(client.get_json_response())
# Output arrays size
print("Output arrays size:")
print("knowledge: ", len(output.knowledge))
print("paragraphs: ", len(output.paragraphs))
print("sentences: ", len(output.sentences))
print("phrases: ", len(output.phrases))
print("tokens: ", len(output.tokens))
print("entities: ", len(output.entities))
print("extra_data: ", output.extra_data)
