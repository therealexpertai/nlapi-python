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

from nlapi.v1.object_mapper import ObjectMapper
from tests import BaseTestCase


class KeyphraseExtraction(BaseTestCase):
    def test_the_response_is_passed_to_the_object_mapper(self):
        """
        ...then verify that the values are correctly set
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
                        "syncon": 45740,
                    }
                ],
                "topics": [
                    {
                        "id": 223,
                        "label": "mechanics",
                        "score": 3.5,
                        "winner": True,
                    }
                ],
                "mainSentences": [
                    {
                        "value": "The machine is held until ready to start by a sort of trap to be sprung when all is ready; then with a tremendous flapping and snapping of the four-cylinder engine, the huge machine springs aloft.",
                        "score": 13.3,
                        "start": 740,
                        "end": 936,
                    },
                ],
                "mainPhrases": [
                    {
                        "value": "four-cylinder engine",
                        "score": 8,
                        "positions": [{"start": 883, "end": 903}],
                    }
                ],
                "mainSyncons": [
                    {
                        "positions": [{"end": 19, "start": 11}],
                        "score": 35.59,
                        "syncon": 45740,
                    }
                ],
                "mainLemmas": [
                    {
                        "value": "locomotive",
                        "score": 6.5,
                        "positions": [
                            {"start": 1152, "end": 1162},
                            {"start": 1163, "end": 1167},
                            {"start": 1239, "end": 1249},
                            {"start": 1335, "end": 1345},
                            {"start": 1394, "end": 1404},
                        ],
                    }
                ],
            },
        }

        omapper = ObjectMapper()
        data_model = omapper.read_json(response_json)
        self.assertEqual(
            data_model.knowledge[0].properties[0].type_, "WikiDataId"
        )
        self.assertEqual(data_model.main_lemmas[0].score, 6.5)
        self.assertEqual(data_model.main_lemmas[0].positions[1].end, 1167)
        self.assertEqual(data_model.main_syncons[0].syncon, 45740)
