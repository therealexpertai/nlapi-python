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

import os
from unittest.mock import MagicMock, patch

from nlapi.common import constants
from nlapi.common.authentication import ExpertAiAuth
from nlapi.common.errors import CredentialsError, ExpertAiRequestError
from tests import ExpertAiTestCase


class ExpertAiAuthTestCase(ExpertAiTestCase):
    def setUp(self):
        self.auth_class = ExpertAiAuth()
        super().setUp()

    @patch("nlapi.common.authentication.ExpertAiAuth.fetch_token_value")
    def test_when_the_auth_header_property_is_read(
        self, patched_fetch_token_value
    ):
        """
        ...then the fetch_token_value method should be called to
        verify if the value should be refreshed.
        """
        plain_text_token = "-1RDVOdFM1UHJBar"
        patched_fetch_token_value.return_value = plain_text_token
        header_token_value = constants.AUTH_HEADER_VALUE.format(
            plain_text_token
        )
        self.assertEqual(
            self.auth_class.header,
            {constants.AUTH_HEADER_KEY: header_token_value},
        )

    @patch("os.getenv", return_value=None)
    def test_the_username_env_variable_is_not_set(self, patched_getenv):
        """
        ...then an error should be raised
        """
        with self.assertRaises(CredentialsError):
            self.auth_class.username
        patched_getenv.assert_called_once_with(constants.USERNAME_ENV_VARIABLE)

    @patch("os.getenv", return_value=None)
    def test_the_password_env_variable_is_not_set(self, patched_getenv):
        """
        ...then an error should be raised
        """
        with self.assertRaises(CredentialsError):
            self.auth_class.password
        patched_getenv.assert_called_once_with(constants.PASSWORD_ENV_VARIABLE)

    def test_token_need_to_remotely_fetched(self):
        """
        ...then verify that the method is called with the correct arguments

        Values passed in the json are defined inside ExpertAiTestCase class
        """
        self.auth_class.fetch_token_value()
        self.patched_post.assert_called_once_with(
            url=constants.OAUTH2_TOKEN_URL,
            headers=constants.CONTENT_TYPE_HEADER,
            json={"username": "user@eai", "password": "pw"},
        )

    def test_server_replies_with_the_new_token(self):
        """
        ...then verify that the content of the response is correctly parsed
        """
        token = "-1RDVOdFM1UHJBar"
        response = MagicMock(text=token, ok=True)

        self.patched_post.return_value = response
        self.assertEqual(self.auth_class.fetch_token_value(), token)
        self.assertEqual(self.patched_post.call_count, 1)

    def test_something_goes_wrong_with_the_token_request(self):
        """
        ...then and error should be raised
        """
        response = MagicMock(
            status_code=constants.HTTP_INTERNAL_SERVER_ERROR, ok=False
        )

        self.patched_post.return_value = response
        self.assertRaises(
            ExpertAiRequestError, self.auth_class.fetch_token_value,
        )

    @patch(
        "nlapi.common.authentication.ExpertAiAuth.token_is_valid",
        side_effect=[False, True],
    )
    def test_token_is_not_valid(self, patched_token_is_valid):
        """
        ...then it should be fetched, but if then is valid the call to
        the server should not be made
        """
        response = MagicMock(text="")
        self.patched_post.return_value = response

        _ = self.auth_class.fetch_token_value()
        _ = self.auth_class.fetch_token_value()
        self.assertEqual(self.patched_post.call_count, 1)
        self.assertEqual(patched_token_is_valid.call_count, 2)

    def test_token_env_variable_is_empty(self):
        """
        ...then the token should not be considered as valid
        """
        with patch.dict(os.environ, {constants.TOKEN_ENV_VARIABLE: ""}):
            self.assertFalse(self.auth_class.token_is_valid())
