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

from expertai.cloud.client import ExpertAiClient
from tests import ExpertAiTestCase


class Contexts(ExpertAiTestCase):
    def test_a_context_request_is_executed(self):
        """
        ...then verify that whole flow works as expected
        """
        response_json = {
            "success": True,
            "contexts": [
                {
                "description": "Standard context",
                "languages": [
                    {
                    "analyses": [
                        "disambiguation",
                        "relevants",
                        "entities",
                        "sentiment",
                        "relations"
                    ],
                    "code": "en",
                    "name": "English"
                    },
                    {
                    "analyses": [
                        "disambiguation",
                        "relevants",
                        "entities",
                        "relations"
                    ],
                    "code": "es",
                    "name": "Spanish"
                    },
                    {
                    "analyses": [
                        "disambiguation",
                        "relevants",
                        "entities",
                        "relations"
                    ],
                    "code": "fr",
                    "name": "French"
                    },
                    {
                    "analyses": [
                        "disambiguation",
                        "relevants",
                        "entities",
                        "relations"
                    ],
                    "code": "de",
                    "name": "German"
                    },
                    {
                    "analyses": [
                        "disambiguation",
                        "relevants",
                        "entities",
                        "relations"
                    ],
                    "code": "it",
                    "name": "Italian"
                    }
                ],
                "name": "standard"
                }
            ]
        }
        response = MagicMock()
        response.status_code = 200
        response.ok = True
        response.json.return_value = response_json

        self.patched_get.return_value = response
        client = ExpertAiClient()
        dm = client.contexts()
        self.assertEqual(dm.contexts[0].name, "standard")
        self.assertEqual(dm.contexts[0].languages[4].code, "it")
        self.assertEqual(dm.contexts[0].languages[3].analyses[2], "entities")
