from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "Michael Jordan was one of the best basketball players of all time. Scoring was Jordan's stand-out skill, but he still holds a defensive NBA record, with eight steals in a half." 
language= 'en'

output = client.contexts()

# Contexts

print("Contexts:")

for context in output.contexts:
    print(context.name)
    print("\tLanguages:")
    for language in context.languages:
        print("\t", language.code)
