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

from nlapi.v1.client import ExpertAiClient
from tests import ExpertAiTestCase


class Contexts(ExpertAiTestCase):
    def test_a_taxonomies_request_is_executed(self):
        """
        ...then verify that whole flow works as expected
        """
        response_json = {
            "success": True,
            "contexts": {
                "standard": {
                    "description": "Standard",
                    "languages": [
                        {"description": "English", "name": "en"},
                        {"description": "German", "name": "de"},
                        {"description": "Spanish", "name": "es"},
                        {"description": "French", "name": "fr"},
                        {"description": "Italian", "name": "it"},
                    ],
                }
            },
        }
        response = MagicMock()
        response.status_code = 200
        response.ok = True
        response.json.return_value = response_json

        self.patched_get.return_value = response
        client = ExpertAiClient()
        dm = client.iptc_taxonomies()
        self.assertEqual(dm.standard.description, "Standard")
        self.assertEqual(
            dm.standard.languages[4].get_language_by_description, "it"
        )
