# Copyright (c) 2020 original authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an \"AS IS\" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest.mock import MagicMock

from tests import ExpertAiTestCase
from expertai.client import ExpertAiClient


class ExpertAiIntegrationTests(ExpertAiTestCase):

    def test_get_iptc_taxonomies(self):
        response_data = {
            "taxonomies": {
                "iptc": {
                    "description": "string",
                    "languages": [{
                        "name": "en",
                        "description": "English"
                    }]
                }
            }
        }
        response = MagicMock()
        response.status_code = 200
        response.ok = True
        response.json.return_value = response_data

        self.patched_get.return_value = response
        client = ExpertAiClient()
        response = client.iptc_taxonomies()
        self.assertEqual(response.json, response_data)
        self.assertEqual(self.patched_post.call_count, 1)

        
    def test_post_classification(self):
        response = MagicMock(text="e@i")
        response.status_code = 200
        response.json.return_value = {"response": "data"}
        self.patched_post.return_value = response

        client = ExpertAiClient()
        request_body = {"document": {"text": "text"}}
        response = client.full_analysis(body=request_body, params={'language': 'es'})

        # two POST requests are made, one for the token and one for analysis
        self.assertEqual(self.patched_post.call_count, 2)
        self.assertEqual(response.json, {"response": "data"})
