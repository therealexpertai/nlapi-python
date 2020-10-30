from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "Michael Jordan was one of the best basketball players of all time. Scoring was Jordan's stand-out skill, but he still holds a defensive NBA record, with eight steals in a half." 
language= 'en'

output = client.specific_resource_analysis(
    body={"document": {"text": text}}, 
    params={'language': language, 'resource': 'disambiguation'
})

# Output tokens' data

print("Output tokens' data:");

print (f'{"TEXT":{20}} {"LEMMA":{40}} {"POS":{6}}')
print (f'{"----":{20}} {"-----":{40}} {"---":{6}}')

for token in output.tokens:
    print (f'{text[token.start:token.end]:{20}} {token.lemma:{40}} {token.pos:{6}}')

