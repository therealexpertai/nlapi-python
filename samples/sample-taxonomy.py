from expertai.nlapi.cloud.client import ExpertAiClient

def printCategory(level, category):
    tabs = "\t" * level
    print(tabs, category.id, "(", category.label, ")")
    for nestedCategory in category.categories:
        printCategory(level + 1, nestedCategory)

client = ExpertAiClient()

taxonomy='geotax'
language='en'

output = client.taxonomy(params={'taxonomy': taxonomy, 'language': language})

print("geotax categories' tree:")

for category in output.taxonomy[0].categories:
    printCategory(1, category)
