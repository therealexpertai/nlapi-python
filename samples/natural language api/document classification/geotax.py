# Demonstrates the GeoTax document classification capability of the (Cloud based) expert.ai Natural Language API

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "Italy, officially the Italian Republic, is a country consisting of a peninsula delimited by the Alps and several islands surrounding it"
taxonomy = 'geotax'
language= 'en'

output = client.classification(body={"document": {"text": text}}, params={'taxonomy': taxonomy, 'language': language})

print("Tab separated list of categories:")

for category in output.categories:
    print(category.id_, category.hierarchy, sep="\t")
