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


class ExpertAiAuthTestCase(ExpertAiTestCase):

    def setUp(self):
        self.auth_class = ExpertAiAuth()
        super().setUp()

    @patch('expertai.authentication.ExpertAiAuth.fetch_token_value')
    def test_auth_header(self, patched_fetch_token_value):
        plain_text_token =  "-1RDVOdFM1UHJBar"
        patched_fetch_token_value.return_value = plain_text_token
        header_token_value = constants.AUTH_HEADER_VALUE.format(
            plain_text_token
        )
        self.assertEqual(
            self.auth_class.header,
            {constants.AUTH_HEADER_KEY: header_token_value}
        )

    @patch('os.getenv', return_value=None)
    def test_username_is_none(self, patched_getenv):
        with self.assertRaises(CredentialsError):
            self.auth_class.username
        patched_getenv.assert_called_once_with(constants.USERNAME_ENV_VARIABLE)
        
    @patch('os.getenv', return_value=None)
    def test_password_is_none(self, patched_getenv):
        with self.assertRaises(CredentialsError):
            self.auth_class.password
        patched_getenv.assert_called_once_with(constants.PASSWORD_ENV_VARIABLE)

    def test_fetch_token_value_request(self):
        self.auth_class.fetch_token_value()
        self.patched_post.assert_called_once_with(
            url=constants.OAUTH2_TOKEN_URL,
            headers=constants.CONTENT_TYPE_HEADER,
            json={"username": "user@eai", "password": "pw"}
        )

    def test_fetch_token_value_content(self):
        token =  "-1RDVOdFM1UHJBar"
        response = MagicMock(text=token, ok=True)

        self.patched_post.return_value = response
        self.assertEqual(self.auth_class.fetch_token_value(), token)
        self.assertEqual(self.patched_post.call_count, 1)
        
    def test_token_request_failure(self):
        response = MagicMock(status_code=500, ok=False)

        self.patched_post.return_value = response
        self.assertRaises(
            ExpertAiRequestError,
            self.auth_class.fetch_token_value,
        )
        
    @patch('expertai.authentication.ExpertAiAuth.token_is_valid', side_effect=[False, True])
    def test_token_is_reused_for_multiple_calls(self, patched_token_is_valid):
        response = MagicMock(text="")
        self.patched_post.return_value = response

        _ = self.auth_class.fetch_token_value()
        _ = self.auth_class.fetch_token_value()
        self.assertEqual(self.patched_post.call_count, 1)
        self.assertEqual(patched_token_is_valid.call_count, 2)

    def test_token_valid(self):
        with patch.dict(os.environ, {constants.TOKEN_ENV_VARIABLE: ""}):
            self.assertFalse(self.auth_class.token_is_valid())

        
