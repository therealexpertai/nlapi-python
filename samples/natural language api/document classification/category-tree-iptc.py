# Demonstrates the use of the self-documentation resource 'taxonomy' of the expert.ai (Cloud based) Natural Language API for the IPTC document classification taxonomy

from expertai.nlapi.cloud.client import ExpertAiClient

def printCategory(level, category):
    tabs = "    " * level
    print("{}{} ({})".format(tabs, category.id, category.label))
    for nestedCategory in category.categories:
        printCategory(level + 1, nestedCategory)

client = ExpertAiClient()

taxonomy='iptc'
language='en'

output = client.taxonomy(params={'taxonomy': taxonomy, 'language': language})

print("iptc taxonomy category tree:\n")

for category in output.taxonomy[0].categories:
    printCategory(0, category)
