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

from unittest.mock import patch

from nlapi.cloud.object_mapper import ObjectMapper
from tests import BaseTestCase


class DeepLinguisticAnalysis(BaseTestCase):
    @patch("nlapi.common.model.data_model.Token")
    @patch("nlapi.common.model.data_model.Paragraph")
    @patch("nlapi.common.model.data_model.Phrase")
    @patch("nlapi.common.model.data_model.Knowledge")
    @patch("nlapi.common.model.data_model.Sentence")
    def test_the_response_is_passed_to_the_object_mapper(
        self,
        patched_sentence,
        patched_knowledge,
        patched_phrase,
        patched_paragraph,
        patched_token,
    ):
        """
        ...then verify that expected nested classes are invoked
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
                            {
                                "type": "DBpediaId",
                                "value": "dbpedia.org/page/Facebook,_Inc.",
                            },
                            {"type": "WikiDataId", "value": "Q380"},
                        ],
                        "syncon": 288110,
                    }
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
                            {
                                "start": 79,
                                "end": 83,
                                "type": "NOU",
                                "lemma": "time",
                            },
                        ],
                    }
                ],
                "phrases": [
                    {"tokens": [0], "type": "PP", "start": 54, "end": 65},
                    {"tokens": [0], "type": "DP", "start": 14, "end": 26},
                    {"tokens": [0], "type": "AP", "start": 1, "end": 2},
                ],
                "sentences": [{"phrases": [0, 2], "start": 0, "end": 66}],
                "paragraphs": [{"sentences": [0], "start": 177, "end": 232}],
            },
        }

        omapper = ObjectMapper()
        omapper.read_json(response_json)
        self.assertEqual(patched_sentence.call_count, 1)
        self.assertEqual(patched_knowledge.call_count, 1)
        self.assertEqual(patched_phrase.call_count, 3)
        self.assertEqual(patched_paragraph.call_count, 1)
        self.assertEqual(patched_token.call_count, 1)
