from expertai.nlapi.cloud.client import ExpertAiClient

client = ExpertAiClient()

output = client.taxonomies()

print("Taxonomies:")

for taxonomy in output.taxonomies:
    print(taxonomy.name)
    print("\tLanguages:")
    for language in taxonomy.languages:
        print("\t", language.code)
