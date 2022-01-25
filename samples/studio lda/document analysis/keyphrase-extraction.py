# Demonstrates the keyphrase extraction capability of the expert.ai (local) Edge NL API performed by the 'relevants' resource wrapped in the `relevants` method of the client.

from expertai.nlapi.edge.client import ExpertAiClient
client = ExpertAiClient()
#client.set_host('localhost', 6670)

file = open("document.txt")
text = file.read()
file.close()

output = client.keyphrase_extraction(text)


# Main lemmas

print("Main lemmas:")

for lemma in output.main_lemmas:
    print(lemma.value)
