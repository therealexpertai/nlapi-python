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

from expertai.nlapi.v1.object_mapper import ObjectMapper
from tests import BaseTestCase


class NamedEntityRecognition(BaseTestCase):
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
                        "label": "person",
                        "properties": [
                            {"type": "WikiDataId", "value": "Q215627"}
                        ],
                        "syncon": 38324,
                    }
                ],
                "entities": [
                    {
                        "type": "GEO",
                        "lemma": "Swansea",
                        "syncon": 38324,
                        "positions": [{"start": 373, "end": 380}],
                    }
                ],
            },
        }

        omapper = ObjectMapper()
        data_model = omapper.read_json(response_json)
        self.assertEqual(data_model.knowledge[0].label, "person")
        self.assertEqual(data_model.knowledge[0].syncon, 38324)
        self.assertEqual(data_model.entities[0].syncon, 38324)
        self.assertEqual(data_model.entities[0].lemma, "Swansea")
