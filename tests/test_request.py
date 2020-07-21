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

from datetime import datetime
import os
from unittest import skip
from unittest.mock import PropertyMock, patch, MagicMock


import requests

from tests import ExpertAiTestCase

from expertai import constants
from expertai.authentication import ExpertAiAuth
from expertai.client import ExpertAiClient
from expertai.response import ExpertAiResponse
from expertai.request import ExpertAiRequest
from expertai.errors import CredentialsError, ExpertAiRequestError


class ExpertAiRequestTestCase(ExpertAiTestCase):

    def setUp(self):
        super().setUp()
        plain_txt_value = "-1RDVOdFM1UHJBar"
        self.expected_headers = dict(
            **constants.CONTENT_TYPE_HEADER,
            **{constants.AUTH_HEADER_KEY: constants.AUTH_HEADER_VALUE.format(
                plain_txt_value
            )}
        )

        file_token_value = patch('expertai.authentication.ExpertAiAuth.fetch_token_value')
        self.file_token_value = file_token_value.start()
        self.file_token_value.return_value = plain_txt_value
        self.addCleanup(file_token_value.stop)

    @patch('expertai.authentication.ExpertAiAuth.header', new_callable=PropertyMock)
    def test_setup_raw_request_get(self, patched_header):
        request_obj = ExpertAiRequest(self.endpoint_path, 'GET')
        method, _ = request_obj.setup_raw_request()

        self.assertEqual(method, self.patched_get)
        patched_header.assert_called_once_with()
 
    @patch('expertai.request.ExpertAiRequest.setup_raw_request')
    def test_setup_raw_request_called(self, patched_setup_raw_request):
        patched_setup_raw_request.return_value = self.patched_post, {}
        request_obj = ExpertAiRequest(self.endpoint_path, 'POST', **{})
        request_obj.send()

        patched_setup_raw_request.assert_called_once_with()

    def test_setup_raw_request_post(self):
        data = {'language': 'en'}
        request_obj = ExpertAiRequest(
            self.endpoint_path,
            'POST',
            body=data
        )
        method, req_params = request_obj.setup_raw_request()

        self.assertEqual(method, self.patched_post)
        self.assertEqual(
            req_params, {
                'url': "{}/{}".format(constants.BASE_API_URL, self.endpoint_path),
                'json': data,
                'headers': self.expected_headers
            })

    def test_send_method(self):
        json_data = {"lang": "en"}
        request_obj = ExpertAiRequest(self.endpoint_path, 'POST', body=json_data)
        request_obj.send()

        self.patched_post.assert_called_once_with(
            url="{}/{}".format(constants.BASE_API_URL, self.endpoint_path),
            headers=self.expected_headers,
            json=json_data
        )

    def test_send_method_returns_response_object(self):
        self.patched_get.return_value = "fake response"
        request_obj = ExpertAiRequest(self.endpoint_path, 'GET', **{})
        response = request_obj.send()

        self.assertEqual("fake response", response)


class NetworkErrorTestCase(ExpertAiTestCase):

    def test_connection_error(self):
        self.patched_get.side_effect = requests.exceptions.ConnectionError
        request_obj = ExpertAiRequest(self.endpoint_path, 'GET', **{})

        self.assertRaises(ExpertAiRequestError, request_obj.send)

    def test_timeout_error(self):
        self.patched_get.side_effect = requests.exceptions.Timeout
        request_obj = ExpertAiRequest(self.endpoint_path, 'GET', **{})

        self.assertRaises(ExpertAiRequestError, request_obj.send)

    def test_too_manyredirects_error(self):
        self.patched_get.side_effect = requests.exceptions.TooManyRedirects
        request_obj = ExpertAiRequest(self.endpoint_path, 'GET', **{})

        self.assertRaises(ExpertAiRequestError, request_obj.send)
   
