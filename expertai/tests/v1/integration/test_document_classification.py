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


class DocumentClassification(BaseTestCase):
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
                "categories": [
                    {
                        "frequency": 70.62,
                        "hierarchy": [
                            "Sport",
                            "Competition discipline",
                            "Basketball",
                        ],
                        "id": "20000851",
                        "label": "Basketball",
                        "namespace": "iptc_en_1.0",
                        "positions": [
                            {"end": 14, "start": 0},
                            {"end": 53, "start": 35},
                            {"end": 139, "start": 136},
                        ],
                        "score": 4005.0,
                        "winner": True,
                    }
                ],
            },
        }

        omapper = ObjectMapper()
        data_model = omapper.read_json(response_json)
        self.assertEqual(data_model.categories[0].hierarchy[2], "Basketball")
        self.assertEqual(data_model.categories[0].id_, "20000851")
        self.assertTrue(data_model.categories[0].winner)
        self.assertEqual(data_model.categories[0].score, 4005.0)
