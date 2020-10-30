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

from expertai.nlapi.cloud.client import ExpertAiClient
from tests import ExpertAiTestCase


class Taxonomies(ExpertAiTestCase):
    def test_a_taxonomies_request_is_executed(self):
        """
        ...then verify that whole flow works as expected
        """
        response_json = {
            "success": True,
            "taxonomies": [
                {
                "description": "The iptc document classification resource classifies texts based on the IPTC Media Topics taxonomy",
                "languages": [
                    {
                    "code": "en",
                    "name": "English"
                    },
                    {
                    "code": "es",
                    "name": "Spanish"
                    },
                    {
                    "code": "fr",
                    "name": "French"
                    },
                    {
                    "code": "de",
                    "name": "German"
                    },
                    {
                    "code": "it",
                    "name": "Italian"
                    }
                ],
                "name": "iptc"
                },
                {
                "contract": "https://github.com/therealexpertai/nlapi-openapi-specification/blob/master/geotax.yaml",
                "description": "The geotax document classification resource recognizes geographic places cited in the text and returns corresponding countries' names. In addition, when requested with a specific query-string parameter, it returns extra-data containing equivalent GeoJSON objects. See the specific OpenAPI document (https://github.com/therealexpertai/nlapi-openapi-specification/blob/master/geotax.yaml) for information about the way to obtain and interpret GeoJSON data.",
                "languages": [
                    {
                    "code": "en",
                    "name": "English"
                    },
                    {
                    "code": "es",
                    "name": "Spanish"
                    },
                    {
                    "code": "fr",
                    "name": "French"
                    },
                    {
                    "code": "de",
                    "name": "German"
                    },
                    {
                    "code": "it",
                    "name": "Italian"
                    }
                ],
                "name": "geotax"
                }
            ]
        }
        response = MagicMock()
        response.status_code = 200
        response.ok = True
        response.json.return_value = response_json

        self.patched_get.return_value = response
        client = ExpertAiClient()
        dm = client.taxonomies()
        self.assertEqual(dm.taxonomies[1].name, "geotax")
        self.assertEqual(dm.taxonomies[0].languages[2].code, "fr")

    def test_taxonomy_iptc_is_executed(self):
        """
        ...then verify that whole flow works as expected
        """
        response_json = {
            "success": True,
            "data": [
                {
                    "namespace": "iptc_en_1.0",
                    "taxonomy": [{
                            "categories": [{
                                    "categories": [{
                                            "categories": [{
                                                    "id": "20000003",
                                                    "label": "Animation"
                                                }, {
                                                    "id": "20000004",
                                                    "label": "Cartoon"
                                                }, {
                                                    "categories": [{
                                                            "id": "20000006",
                                                            "label": "Film festival"
                                                        }
                                                    ],
                                                    "id": "20000005",
                                                    "label": "Cinema"
                                                }, {
                                                    "categories": [{
                                                            "id": "20000008",
                                                            "label": "Ballet"
                                                        }, {
                                                            "id": "20000009",
                                                            "label": "Modern dance"
                                                        }, {
                                                            "id": "20000010",
                                                            "label": "Traditional dance"
                                                        }
                                                    ],
                                                    "id": "20000007",
                                                    "label": "Dance"
                                                }
                                            ],
                                            "id": "01000000",
                                            "label": "Arts, culture and entertainment"
                                        }
                                    ],
                                    "id": "V16000000",
                                    "label": "Conflicts, war and peace"
                                }
                            ],
                            "id": "MEDIATOPIC_TAX",
                            "label": "MEDIATOPIC_TAX"
                        }
                    ]
                }                
            ]
        }
        response = MagicMock()
        response.status_code = 200
        response.ok = True
        response.json.return_value = response_json

        self.patched_get.return_value = response
        client = ExpertAiClient()
        dm = client.taxonomy_iptc(params={ "language" : "en" })
        self.assertEqual(dm.taxonomy[0].categories[0].id, "MEDIATOPIC_TAX")
        self.assertEqual(dm.taxonomy[0].categories[0].categories[0].label, "Conflicts, war and peace")
