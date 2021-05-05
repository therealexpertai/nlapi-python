# Demonstrates the IPTC Media Topics document classification capability of the (Cloud based) expert.ai Natural Language API

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "I experience a mix of conflicting emotions: the approach of the fateful date scares me, but at the same time I can't wait for it to arrive. I have moments of elation and others of pure panic, but I would say that I am mostly happy."
taxonomy = 'emotional-traits'
language= 'en'

output = client.classification(body={"document": {"text": text}}, params={'taxonomy': taxonomy, 'language': language})

print("Tab separated list of categories:")

for category in output.categories:
    print(category.id_, category.hierarchy, sep="\t")
