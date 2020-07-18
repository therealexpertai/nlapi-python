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
from unittest import skip
from unittest.mock import PropertyMock, mock_open, patch, MagicMock


import requests

from tests import ExpertTestCase

from lib import constants
from lib.expert import ExpertAuth, ExpertClient, ExpertRequest, ExpertResponse
from lib.errors import CredentialsError, ExpertRequestError, MissingParameterError


class ExpertAuthTestCase(ExpertTestCase):

    def setUp(self):
        self.auth_class = ExpertAuth()
        super().setUp()

    @patch('lib.expert.ExpertAuth.fetch_token_value')
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
        self.patched_requests.post.assert_called_once_with(
            url=constants.OAUTH2_TOKEN_URL,
            headers=constants.CONTENT_TYPE_HEADER,
            json={"username": "user@eai", "password": "pw"}
        )

    def test_fetch_token_value_content(self):
        token =  "-1RDVOdFM1UHJBar"
        response = MagicMock()
        response.text = token
        response.ok = True

        self.patched_requests.post.return_value = response
        self.assertEqual(self.auth_class.fetch_token_value(), token)
        
    def test_token_request_failure(self):
        response = MagicMock()
        response.status_code = 500
        response.ok = False

        self.patched_requests.post.return_value = response
        self.assertRaises(
            ExpertRequestError,
            self.auth_class.fetch_token_value,
        )
        
    @patch('lib.expert.open')
    def test_write_token_timestamp(self, mocked_open_file):
        self.auth_class.write_token_timestamp()
        mocked_open_file.assert_called_once_with(
            constants.TK_TIMESTAMP_FILENAME,
            'w'
        )

    @skip('')
    @patch('lib.expert.open')
    def test_token_is_valid(self, mocked_open_file):
        mocked_open_file.side_effect = mock_open(read_data='')
        self.assertFalse(self.auth_class.is_token_valid())

        
class ExpertRequestTestCase(ExpertTestCase):

    def setUp(self):
        super().setUp()
        plain_txt_value = "-1RDVOdFM1UHJBar"
        self.expected_headers = dict(
            **constants.CONTENT_TYPE_HEADER,
            **{constants.AUTH_HEADER_KEY: constants.AUTH_HEADER_VALUE.format(
                plain_txt_value
            )}
        )

        file_token_value = patch('lib.expert.ExpertAuth.fetch_token_value')
        self.file_token_value = file_token_value.start()
        self.file_token_value.return_value = plain_txt_value
        self.addCleanup(file_token_value.stop)

    @patch('lib.expert.ExpertAuth.header', new_callable=PropertyMock)
    def test_setup_raw_request_get(self, patched_header):
        request_obj = ExpertRequest(self.endpoint_path, 'GET')
        method, _ = request_obj.setup_raw_request()

        self.assertEqual(method, self.patched_requests.get)
        patched_header.assert_called_once_with()
 
    @patch('lib.expert.ExpertRequest.setup_raw_request')
    def test_setup_raw_request_called(self, patched_setup_raw_request):
        patched_setup_raw_request.return_value = self.patched_requests, {}
        request_obj = ExpertRequest(self.endpoint_path, 'POST', **{})
        request_obj.send()

        patched_setup_raw_request.assert_called_once_with()

    def test_setup_raw_request_post(self):
        data = {'language': 'en'}
        request_obj = ExpertRequest(
            self.endpoint_path,
            'POST',
            body=data
        )
        method, req_params = request_obj.setup_raw_request()

        self.assertEqual(method, self.patched_requests.post)
        self.assertEqual(
            req_params, {
                'url': "{}/{}".format(constants.BASE_API_URL, self.endpoint_path),
                'json': data,
                'headers': self.expected_headers
            })

    def test_send_method(self):
        json_data = {"lang": "en"}
        request_obj = ExpertRequest(self.endpoint_path, 'POST', body=json_data)
        request_obj.send()

        self.patched_requests.post.assert_called_once_with(
            url="{}/{}".format(constants.BASE_API_URL, self.endpoint_path),
            headers=self.expected_headers,
            json=json_data
        )

    def test_send_method_returns_response_object(self):
        self.patched_requests.get.return_value = "fake response"
        request_obj = ExpertRequest(self.endpoint_path, 'GET', **{})
        response = request_obj.send()

        self.assertEqual("fake response", response)


class NetworkErrorTestCase(ExpertTestCase):
    def test_connection_error(self):
        self.patched_requests.get.side_effect = requests.exceptions.ConnectionError
        request_obj = ExpertRequest(self.endpoint_path, 'GET', **{})

        self.assertRaises(ExpertRequestError, request_obj.send)

    def test_timeout_error(self):
        self.patched_requests.get.side_effect = requests.exceptions.Timeout
        request_obj = ExpertRequest(self.endpoint_path, 'GET', **{})

        self.assertRaises(ExpertRequestError, request_obj.send)

    def test_too_manyredirects_error(self):
        self.patched_requests.get.side_effect = requests.exceptions.TooManyRedirects
        request_obj = ExpertRequest(self.endpoint_path, 'GET', **{})

        self.assertRaises(ExpertRequestError, request_obj.send)


class ExpertResponseTestCase(ExpertTestCase):
    def setUp(self):
        self.http_response = MagicMock()
        super().setUp()

    def test_success_response(self):
        self.http_response.status_code = 200
        response = ExpertResponse(self.http_response)
        self.assertEqual(response.successful, True)

    def test_unauthorized_response(self):
        self.http_response.status_code = 401
        response = ExpertResponse(self.http_response)
        self.assertEqual(response.unauthorized, True)

    def test_forbidden_response(self):
        self.http_response.status_code = 403
        response = ExpertResponse(self.http_response)
        self.assertEqual(response.forbidden, True)

    def test_not_found_response(self):
        self.http_response.status_code = 404
        response = ExpertResponse(self.http_response)
        self.assertEqual(response.not_found, True)

    @skip('')
    def test_bad_request_response(self):
        """
        """
        self.http_response.status_code = 200
        response = ExpertResponse(self.http_response)
        self.assertEqual(response.bad_request, True)

    def test_error_response(self):
        self.http_response.status_code = 500
        response = ExpertResponse(self.http_response)
        self.assertEqual(response.error, True)

    @patch('lib.expert.ExpertResponse.parse_data')
    def test_error_response_json(self, patched_parse_data):
        self.http_response.status_code = 401
        response = ExpertResponse(self.http_response)
        patched_parse_data.assert_not_called()
        

class ExpertClientTestCase(ExpertTestCase):

    def setUp(self):
        super().setUp()
        self.expert_client = ExpertClient()
        self.test_body = {"document": {"text": "text"}}
        self.test_endpoint_path = "endpoint/{language}/{resource}"

    @patch('lib.expert.ExpertClient.get_method_name_for_endpoint')
    def test_request_creation(self, patched_get_method_name_for_endpoint):
        url = self.endpoint_path

        def fake_get_method(self):
            return {url: 'GET'}.get(url)

        expert_client = ExpertClient()
        patched_get_method_name_for_endpoint.side_effect = fake_get_method
        new_request = expert_client.create_request(self.endpoint_path)
        self.assertEqual(new_request.string_method, 'GET')
        patched_get_method_name_for_endpoint.assert_called_once_with(self.endpoint_path)

    def test_format_enpoint_method(self):
        url = self.expert_client.format_enpoint(
            endpoint_path=self.test_endpoint_path,
            params={"language": "en", "resource": "entities"}
        )
        self.assertEqual(url, "endpoint/en/entities")

    def test_need_formatting(self):
        self.assertTrue(self.expert_client.need_formatting("path/{url}"))

    def test_format_enpoint_key_error(self):
        self.assertRaises(
            MissingParameterError,
            self.expert_client.format_enpoint,
            self.test_endpoint_path,
            params={'language': 'en'}
        )

    def test_missing_parameters(self):
        self.assertEqual(
            self.expert_client.missing_parameters("path/{lang}/{res}"),
            ['{lang}', '{res}']
        )
    

class APIEndPointMethods(ExpertTestCase):
    def setUp(self):
        super().setUp()
        self.expert_client = ExpertClient()


class EndPointMethodsTests(APIEndPointMethods):

    @patch('lib.expert.ExpertClient.format_enpoint')
    def test_format_enpoint_invocation_with_kwargs(self, patched_format_enpoint):
        self.expert_client.full_analysis(
            params={'language': 'en'},
            body={'text': 'text'},
        )
        patched_format_enpoint.assert_called_with(
            constants.FULL_ANALYSIS_PATH,
            params={'language': 'en'},
        )

    @patch('lib.expert.ExpertClient.format_enpoint')
    def test_format_enpoint_invocation_without_kwargs(self, patched_format_enpoint):
        self.expert_client.iptc_taxonomies_list()
        patched_format_enpoint.assert_called_with(
            constants.TAXONOMIES_LIST_PATH,
            params=None
        )

    @patch('lib.expert.ExpertRequest')
    def test_create_method_invocation_with_post(self, patched_request_class):
        self.expert_client.specific_resource_analysis(
            params={'language': 'en', 'resource': 'res'},
            body={'text': 'text'},
        )

        expected_url = constants.SPECIFIC_RESOURCE_ANALYSIS_PATH.format(
            **{'language': 'en', 'resource': 'res'}
        )
        patched_request_class.assert_called_with(
            endpoint_path=expected_url,
            http_method_name='POST',
            body={'text': 'text'},
        )

    @skip
    def test_iptc_media_topics_classification_method(self):
        self.expert_client.iptc_media_topics_classification()
        self.patched_create_request.assert_called_with(
            url=constants.IPTC_MEDIA_TOPICS_CLASSIFICATION_PATH)

    @skip
    def test_contexts_method(self):
        self.expert_client.contexts()
        self.patched_create_request.assert_called_with(
            url=constants.CONTEXTS_PATH)

    @skip
    def test_contexts_standard_method(self):
        self.expert_client.contexts_standard()
        self.patched_create_request.assert_called_with(
            url=constants.CONTEXTS_STANDARD_PATH)

    @skip
    def test_iptc_taxonomies_method(self):
        self.expert_client.iptc_taxonomies()
        self.patched_create_request.assert_called_with(
            url=constants.IPTC_TAXONOMIES_PATH)
