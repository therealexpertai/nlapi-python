# Demonstrates the sentiment analysis capability of the expert.ai (local) Edge NL API performed by the 'sentiment' resource wrapped in the `sentiment` method of the client.

from expertai.nlapi.edge.client import ExpertAiClient
client = ExpertAiClient()

text = "Michael Jordan was one of the best basketball players of all time. Scoring was Jordan's stand-out skill, but he still holds a defensive NBA record, with eight steals in a half." 

output = client.sentiment(text)

# Output overall sentiment

print("Output overall sentiment:")

print(output.sentiment.overall)
