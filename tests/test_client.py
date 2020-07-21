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
from expertai.validate import ExpertAiValidation
from expertai.errors import CredentialsError, ExpertAiRequestError, MissingParametersError, ParameterError


class ExpertAiClientTestCase(ExpertAiTestCase):

    def setUp(self):
        super().setUp()
        self.expert_client = ExpertAiClient()
        self.test_body = {"document": {"text": "text"}}
        self.test_endpoint_path = "endpoint/{language}/{resource}"

    @patch('expertai.client.ExpertAiClient.get_method_name_for_endpoint')
    def test_request_creation(self, patched_get_method_name_for_endpoint):
        url = self.endpoint_path

        def fake_get_method(self):
            return {url: 'GET'}.get(url)

        expert_client = ExpertAiClient()
        patched_get_method_name_for_endpoint.side_effect = fake_get_method
        new_request = expert_client.create_request(self.endpoint_path)
        self.assertEqual(new_request.string_method, 'GET')
        patched_get_method_name_for_endpoint.assert_called_once_with(self.endpoint_path)

    @patch('expertai.validate.ExpertAiValidation.check_parameters')
    def test_verify_request(self, patched_check_parameters):
        self.expert_client.verify_request(
            endpoint_path="path/{lang}",
            params={"language": "en"}
        )
        patched_check_parameters.assert_called_once_with(params={"language": "en"})

    @patch('expertai.validate.ExpertAiValidation.check_parameters')
    def test_no_required_parameters(self, patched_check_parameters):
        self.expert_client.verify_request(
            endpoint_path="/path",
            params=None
        )
        patched_check_parameters.assert_not_called()
    
    def test_required_params_not_there(self):
        self.assertRaises(
            MissingParametersError,
            self.expert_client.verify_request,
            endpoint_path="path/{lang}",
        )
        
    def test_endpoint_url_parameters(self):
        self.assertEqual(
            self.expert_client.endpoint_url_parameters("path/{url}/{node}"),
            ['{url}', '{node}']
        )


class APIEndPointMethods(ExpertAiTestCase):
    def setUp(self):
        super().setUp()
        self.expert_client = ExpertAiClient()


class EndPointMethodsTests(APIEndPointMethods):

    @patch('expertai.client.ExpertAiClient.verify_request')
    def test_expect_post_verification(self, patched_verify_request):
        self.expert_client.full_analysis(
            params={'language': 'en'},
            body={'text': 'text'},
        )
        patched_verify_request.assert_called_with(
            constants.FULL_ANALYSIS_PATH,
            params={'language': 'en'},
        )

    @patch('expertai.client.ExpertAiRequest')
    def test_create_method_invocation_with_post(self, patched_request_class):
        params = {'language': 'en', 'resource': 'disambiguation'}
        expected_url = constants.SPECIFIC_RESOURCE_ANALYSIS_PATH.format(
            **params
        )
        self.expert_client.specific_resource_analysis(
            params=params,
            body={'text': 'text'},
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
