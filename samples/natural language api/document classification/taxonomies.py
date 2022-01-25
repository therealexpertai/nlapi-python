# Demonstrates the use of the self-documentation resource 'taxonomies' of the expert.ai (Cloud based) Natural Language API

from expertai.nlapi.cloud.client import ExpertAiClient

client = ExpertAiClient()

output = client.taxonomies()

print("Taxonomies:\n")

for taxonomy in output.taxonomies:
    print(taxonomy.name)
    print("\tLanguages:")
    for language in taxonomy.languages:
        print("\t\t{0}".format(language.code))
