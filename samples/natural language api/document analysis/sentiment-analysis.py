# Demonstrates the sentiment analysis capability of the expert.ai (Cloud based) Natural Language API performed by the 'sentiment' resource

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "Michael Jordan was one of the best basketball players of all time. Scoring was Jordan's stand-out skill, but he still holds a defensive NBA record, with eight steals in a half." 
language= 'en'

output = client.specific_resource_analysis(
    body={"document": {"text": text}}, 
    params={'language': language, 'resource': 'sentiment'
})

# Output overall sentiment

print("Output overall sentiment:")

print(output.sentiment.overall)
