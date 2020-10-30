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

from expertai.nlapi.v1 import constants
from expertai.nlapi.v1.response import ExpertAiResponse
from tests import ExpertAiTestCase


class ExpertAiResponseTestCase(ExpertAiTestCase):
    def test_server_returns_a_200(self):
        """
        ...then the EAI Response should be set to Successful
        """
        response = ExpertAiResponse(
            MagicMock(status_code=constants.HTTP_SUCCESSFUL, json=dict)
        )
        self.assertEqual(response.status, constants.SUCCESSFUL)

    def test_server_returns_a_401(self):
        """
        ...then the EAI Response should be set to Unauthorized
        """
        response = ExpertAiResponse(
            MagicMock(status_code=constants.HTTP_UNAUTHORIZED)
        )
        self.assertEqual(
            response.status, constants.HTTP_ERRORS[constants.HTTP_UNAUTHORIZED]
        )

    def test_server_returns_a_403(self):
        """
        ...then the EAI Response status should be set to Forbidden
        """
        response = ExpertAiResponse(
            MagicMock(status_code=constants.HTTP_FORBIDDEN)
        )
        self.assertEqual(
            response.status, constants.HTTP_ERRORS[constants.HTTP_FORBIDDEN]
        )

    def test_server_returns_a_404(self):
        """
        ...then the EAI Response status should be set to Not Found
        """
        response = ExpertAiResponse(
            MagicMock(status_code=constants.HTTP_NOT_FOUND)
        )
        self.assertEqual(
            response.status, constants.HTTP_ERRORS[constants.HTTP_NOT_FOUND]
        )

    def test_server_returns_a_200_but_the_json_contains_error_key(self):
        """
        ...then the EAI Response status should be set to bad-request
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
        response = ExpertAiResponse(fake_response)
        self.assertEqual(response.status, constants.BAD_REQUEST)

    def test_a_error_response(self):
        """
        ...then the response status should report the right information
        """
        response = ExpertAiResponse(
            MagicMock(status_code=constants.HTTP_INTERNAL_SERVER_ERROR)
        )
        self.assertEqual(
            response.status,
            constants.HTTP_ERRORS[constants.HTTP_INTERNAL_SERVER_ERROR],
        )

    def test_a_bad_request_message_has_to_be_returned(self):
        """
        ...then it should be pre-formatted
        """
        error_json = {
            "errors": [
                {"code": "code 1", "message": "message 1"},
                {"code": "code 2", "message": "message 2"},
            ],
            "success": False,
        }
        fake_response = MagicMock(status_code=constants.HTTP_SUCCESSFUL)
        response = ExpertAiResponse(fake_response)
        self.assertEqual(
            response.bad_request_message(error_json),
            "(code 1, message 1) (code 2, message 2)",
        )
