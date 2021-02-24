# Demonstrates the full document analysis capability of the expert.ai (Cloud based) Natural Language API

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "Michael Jordan was one of the best basketball players of all time. Scoring was Jordan's stand-out skill, but he still holds a defensive NBA record, with eight steals in a half.'" 
language= 'en'

output = client.full_analysis(body={"document": {"text": text}}, params={'language': language})


# Output arrays size

print("Output arrays size:");

print("knowledge: ", len(output.knowledge))
print("paragraphs: ", len(output.paragraphs))
print("sentences: ", len(output.sentences))
print("phrases: ", len(output.phrases))
print("tokens: ", len(output.tokens))
print("mainSentences: ", len(output.main_sentences))
print("mainPhrases: ", len(output.main_phrases))
print("mainLemmas: ", len(output.main_lemmas))
print("mainSyncons: ", len(output.main_syncons))
print("topics: ", len(output.topics))
print("entities: ", len(output.entities))
print("relations: ", len(output.relations))
print("sentiment.items: ", len(output.sentiment.items))
