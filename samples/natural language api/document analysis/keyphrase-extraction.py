# Demonstrates the keyphrase extraction capability of the expert.ai (Cloud based) Natural Language API performed by the 'relevants' resource

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

file = open("document.txt")
text = file.read()
file.close()

language= 'en'

output = client.specific_resource_analysis(body={"document": {"text": text}}, params={'language': language, 'resource': 'relevants'})


# Main lemmas

print("Main lemmas:")

for lemma in output.main_lemmas:
    print(lemma.value)
