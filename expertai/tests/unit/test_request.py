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

from unittest.mock import PropertyMock, patch

import requests

from nlapi.common import constants
from nlapi.common.errors import ExpertAiRequestError
from nlapi.cloud.request import ExpertAiRequest
from tests import ExpertAiTestCase


class ExpertAiRequestTestCase(ExpertAiTestCase):
    def setUp(self):
        super().setUp()
        plain_txt_value = "-1RDVOdFM1UHJBar"
        self.expected_headers = dict(
            **constants.CONTENT_TYPE_HEADER,
            **{
                constants.AUTH_HEADER_KEY: constants.AUTH_HEADER_VALUE.format(
                    plain_txt_value
                )
            }
        )

        file_token_value = patch(
            "nlapi.common.authentication.ExpertAiAuth.fetch_token_value"
        )
        self.file_token_value = file_token_value.start()
        self.file_token_value.return_value = plain_txt_value
        self.addCleanup(file_token_value.stop)

    @patch(
        "nlapi.common.authentication.ExpertAiAuth.header",
        new_callable=PropertyMock,
    )
    def test_a_raw_request_is_generated_out_of_a_request_object(
        self, patched_header
    ):
        """
        ...then verify that the HTTP method name is the right one
        and the authentication header set into the request
        """
        request_obj = ExpertAiRequest(self.endpoint_path, "GET")
        method, _ = request_obj.setup_raw_request()

        self.assertEqual(method, self.patched_get)
        patched_header.assert_called_once_with()

    @patch("nlapi.cloud.request.ExpertAiRequest.setup_raw_request")
    def test_the_send_method_is_invoked(self, patched_setup_raw_request):
        """
        ...then verify that the setup_raw_request method is called
        """
        patched_setup_raw_request.return_value = self.patched_post, {}
        request_obj = ExpertAiRequest(self.endpoint_path, "POST", **{})
        request_obj.send()

        patched_setup_raw_request.assert_called_once_with()

    def test_the_setup_raw_request_method_is_called_for_a_post(self):
        """
        ...then verify that the paramters are correctly setup
        """
        data = {"language": "en"}
        request_obj = ExpertAiRequest(self.endpoint_path, "POST", body=data)
        method, req_params = request_obj.setup_raw_request()

        self.assertEqual(method, self.patched_post)
        self.assertEqual(
            req_params,
            {
                "url": "{}/{}".format(
                    constants.BASE_API_URL, self.endpoint_path
                ),
                "json": data,
                "headers": self.expected_headers,
            },
        )

    def test_expert_post_request_is_send(self):
        """
        ...then verify that the HTTP post is actually trigger with the
        correct parameters
        """
        json_data = {"lang": "en"}
        request_obj = ExpertAiRequest(
            self.endpoint_path, "POST", body=json_data
        )
        request_obj.send()

        self.patched_post.assert_called_once_with(
            url="{}/{}".format(constants.BASE_API_URL, self.endpoint_path),
            headers=self.expected_headers,
            json=json_data,
        )


class NetworkErrorTestCase(ExpertAiTestCase):
    def test_a_requests_connection_error_is_raised(self):
        """
        ...then is caught and the custom exception raised instead
        """
        self.patched_get.side_effect = requests.exceptions.ConnectionError
        request_obj = ExpertAiRequest(self.endpoint_path, "GET", **{})

        self.assertRaises(ExpertAiRequestError, request_obj.send)

    def test_a_requests_timeout_error_is_raised(self):
        """
        ...then is caught and the custom exception raised instead
        """
        self.patched_get.side_effect = requests.exceptions.Timeout
        request_obj = ExpertAiRequest(self.endpoint_path, "GET", **{})

        self.assertRaises(ExpertAiRequestError, request_obj.send)

    def test_a_requests_too_manyredirects_error_is_raised(self):
        """
        ...then is caught and the custom exception raised instead
        """
        self.patched_get.side_effect = requests.exceptions.TooManyRedirects
        request_obj = ExpertAiRequest(self.endpoint_path, "GET", **{})

        self.assertRaises(ExpertAiRequestError, request_obj.send)
