# Demonstrates the sentiment analysis capability of the expert.ai (Cloud based) Natural Language API performed by the 'sentiment' resource

from expertai.nlapi.cloud.client import ExpertAiClient
client2 = ExpertAiClient()

text = "Michael Jordan was one of the best basketball players of all time." 
language= 'en'

output = client2.specific_resource_analysis(
    body={"document": {"text": text}}, 
    params={'language': language, 'resource': 'sentiment'
})

# Output overall sentiment

print("Output overall sentiment:")

print(output.sentiment.overall)

output = client2.specific_resource_analysis(
    body={"document": {"text": text}}, 
    params={'language': language, 'resource': 'sentiment'
})

# Output overall sentiment

print("Output overall sentiment (2):")

print(output.sentiment.overall)

