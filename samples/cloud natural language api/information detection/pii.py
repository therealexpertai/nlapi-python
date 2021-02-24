# Demonstrates the Personally Identifiable Information (PII) detection capability of the expert.ai (Cloud based) Natural Language API

import json
from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "CREDIT CARD CANCELLATION REQUEST\nPERSONAL INFORMATION:\nNAME: Anne Cuthbert\nADDRESS: 3239 Rardin Drive, Broad Run, VA, 20137\nBORN: 02/06/1992, Charlottetown, Canada\nPHONE NUMBER: 985-281-4501\nEMAIL: acut@mails.com\nDear Sir or madam,\nOn April 8, 2017, I lost my credit card while I was abroad. Please find below the credit card's details:\nCard Type: American Express 4242 8978 2056 4987, Expiration date 09/2019, CVV 987.\nAs soon as I realized the card was lost, I phoned the company and asked that it be cancelled.\nThis letter is to request that you issue me a replacement card as soon as possible. The cancelled card should be not authorized under any circumstances.\nThank you for your attention.\nIf you have any questions, I can be reached at the phone number or email above mentioned\nSincerely,\nAnne Cuthbert"

detector = 'pii'
language= 'en'

output = client.detection(body={"document": {"text": text}}, params={'detector': detector, 'language': language})

# Output extra data containing the JSON-LD object

print("extra_data: ",json.dumps(output.extra_data, indent=4, sort_keys=True))
