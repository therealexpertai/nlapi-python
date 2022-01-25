# Demonstrates the use of the self-documentation resource 'contexts' of the expert.ai (Cloud based) Natural Language API

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

output = client.contexts()

# Contexts

print("Contexts:\n")

for context in output.contexts:
    print(context.name)
    print("\tLanguages:")
    for language in context.languages:
        print("\t\t{}".format(language.code))
