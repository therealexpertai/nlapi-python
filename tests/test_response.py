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


class ExpertAiResponseTestCase(ExpertAiTestCase):
    def test_success_response(self):
        response = ExpertAiResponse(MagicMock(status_code=200))
        self.assertEqual(response.successful, True)

    def test_unauthorized_response(self):
        response = ExpertAiResponse(MagicMock(status_code=401))
        self.assertEqual(response.unauthorized, True)

    def test_forbidden_response(self):
        response = ExpertAiResponse(MagicMock(status_code=403))
        self.assertEqual(response.forbidden, True)

    def test_not_found_response(self):
        response = ExpertAiResponse(MagicMock(status_code=404))
        self.assertEqual(response.not_found, True)

    @skip('')
    def test_bad_request_response(self):
        """
        """
        self.http_response.status_code = 200
        response = ExpertAiResponse(self.http_response)
        self.assertEqual(response.bad_request, True)

    def test_error_response(self):
        response = ExpertAiResponse(MagicMock(status_code=500))
        self.assertEqual(response.error, True)

    @patch('expertai.response.ExpertAiResponse.parse_data')
    def test_error_response_json(self, patched_parse_data):
        response = ExpertAiResponse(MagicMock(status_code=401))
        patched_parse_data.assert_not_called()
        

