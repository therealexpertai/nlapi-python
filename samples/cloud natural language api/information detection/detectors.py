# Demonstrates the use of the self-documentation resource 'detectors' of the expert.ai (Cloud based) Natural Language API

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

output = client.detectors()

# Detectors

print("Detectors:\n")

for detector in output.detectors:
    print(detector.name)
    print("\tLanguages:")
    for language in detector.languages:
        print("\t\t{}".format(language.code))
    print("\tContract: {}".format(detector.contract))
