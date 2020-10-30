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

from unittest.mock import MagicMock, patch

from expertai.nlapi.common import constants
from expertai.nlapi.cloud.client import ExpertAiClient
from expertai.nlapi.common.errors import MissingParametersError
from tests import ExpertAiTestCase


class ExpertAiClientTestCase(ExpertAiTestCase):
    def setUp(self):
        super().setUp()
        self.expert_client = ExpertAiClient()
        self.test_body = {"document": {"text": "text"}}
        self.test_endpoint_path = "endpoint/{language}/{resource}"

    @patch("expertai.nlapi.cloud.client.ExpertAiClient.get_method_name_for_endpoint")
    def test_a_request_is_created(self, patched_get_method_name_for_endpoint):
        """
        ...then the proper HTTP method should be set
        """

        def fake_get_method(self):
            return {url: "GET"}.get(url)

        url = self.endpoint_path
        expert_client = ExpertAiClient()
        patched_get_method_name_for_endpoint.side_effect = fake_get_method
        new_request = expert_client.create_request(self.endpoint_path)

        self.assertEqual(new_request.string_method, "GET")
        patched_get_method_name_for_endpoint.assert_called_once_with(
            self.endpoint_path
        )

    @patch("expertai.nlapi.cloud.validate.ExpertAiValidation.check_parameters")
    def test_a_request_is_verified(self, patched_check_parameters):
        """
        ...then check_parameters method should be called
        """
        self.expert_client.verify_request(
            endpoint_path="path/{language}", params={"language": "en"}
        )

        patched_check_parameters.assert_called_once_with(
            params={"language": "en"}
        )

    @patch("expertai.nlapi.cloud.validate.ExpertAiValidation.check_parameters")
    def test_parameters_are_not_required(self, patched_check_parameters):
        """
        ...then the check_parameters method should not be called
        """
        self.expert_client.verify_request(endpoint_path="/path", params=None)
        patched_check_parameters.assert_not_called()

    def test_required_parameters_are_not_provided(self):
        """
        ...then an error should be raised, indicating which parameter
        is missing
        """
        self.assertRaises(
            MissingParametersError,
            self.expert_client.verify_request,
            endpoint_path="path/{lang}",
        )

    def test_a_parameterized_urlpath(self):
        """
        ...then keywords should be extracted
        """
        self.assertEqual(
            self.expert_client.urlpath_keywords("path/{language}/{resource}"),
            ["language", "resource"],
        )

    @patch("expertai.nlapi.cloud.client.ExpertAiClient.verify_request")
    def test_create_request_method_is_called(self, patched_verify_request):
        """
        ...then the verify_request() should also be invoked with the
        correct arguments
        """
        expert_client = ExpertAiClient()
        expert_client.create_request(
            endpoint_path="resource_urlpath",
            params={"language": "en"},
            body={"text": "text"},
        )

        patched_verify_request.assert_called_with(
            "resource_urlpath", params={"language": "en"},
        )

    @patch("expertai.nlapi.cloud.client.ObjectMapper")
    def test_a_bad_request_is_received(self, patched_object_mapper):
        """
        ...then the ObjectMapper should not be called
        """

        def response_json():
            return {
                "errors": [
                    {
                        "code": "PREPARE_DOCUMENT_FAILED",
                        "message": "missing layout key in json",
                    }
                ],
                "success": False,
            }

        fake_response = MagicMock(
            status_code=constants.HTTP_SUCCESSFUL, json=response_json
        )
        expert_client = ExpertAiClient()
        expert_client.process_response(fake_response)
        patched_object_mapper.assert_not_called()
