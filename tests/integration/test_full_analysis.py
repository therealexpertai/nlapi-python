# Copyright (c) 2020 original authors
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest.mock import MagicMock

from expertai.client import ExpertAiClient
from tests import ExpertAiTestCase


class FullAnalysis(ExpertAiTestCase):
    def test_a_full_analysis_request_is_executed(self):
        """
        ...then verify that whole flow works as expected
        """
        response_json = {
            "success": True,
            "data": {
                "content": "Facebook is looking at buying U.S. startup for $6 million",
                "language": "en",
                "version": "sensei: 3.1.0; disambiguator: 15.0-QNTX-2016",
                "knowledge": [
                    {
                        "label": "organization.company",
                        "properties": [
                            {"type": "WikiDataId", "value": "Q380"}
                        ],
                        "syncon": 288110,
                    }
                ],
                "phrases": [
                    {"tokens": [0], "type": "PP", "start": 54, "end": 65},
                ],
                "tokens": [
                    {
                        "syncon": 62653,
                        "start": 74,
                        "end": 83,
                        "type": "NOU",
                        "lemma": "long time",
                        "pos": "NOUN",
                        "dependency": {"id": 11, "head": 7, "label": "nmod"},
                        "morphology": "Number=Sing",
                        "paragraph": 0,
                        "sentence": 0,
                        "phrase": 4,
                        "atoms": [
                            {
                                "start": 74,
                                "end": 78,
                                "type": "ADJ",
                                "lemma": "long",
                            },
                        ],
                    }
                ],
                "mainSentences": [],
                "mainPhrases": [],
                "mainLemmas": [],
                "mainSyncons": [],
                "entities": [],
                "topics": [],
                "sentences": [{"phrases": [0], "start": 0, "end": 100}],
                "paragraphs": [],
            },
        }

        response = MagicMock(text="e@i")
        response.status_code = 200
        response.json.return_value = response_json
        self.patched_post.return_value = response

        client = ExpertAiClient()
        request_body = {"document": {"text": "text"}}
        data_model = client.full_analysis(
            body=request_body, params={"language": "es"}
        )

        # two POST requests are made, one for the token and one for analysis
        self.assertEqual(self.patched_post.call_count, 2)
        self.assertEqual(data_model.sentences[0].phrases[0].type_.key, "PP")
