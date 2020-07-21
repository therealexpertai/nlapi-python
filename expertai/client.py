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
import logging
import os
import re
import requests

from expertai import constants
from expertai.request import ExpertAiRequest
from expertai.response import ExpertAiResponse
from expertai.validate import ExpertAiValidation
from expertai.errors import CredentialsError, ExpertAiRequestError, MissingParametersError


class ExpertAiClient:
    def __init__(self):
        self.response_class = ExpertAiResponse
        self._endpoint_path = ""

    def endpoint_url_parameters(self, endpoint_path):
        return re.findall(r'(\{\w+\})', endpoint_path)
    
    def verify_request(self, endpoint_path, **kwargs):
        required_params = self.endpoint_url_parameters(endpoint_path)
        if required_params:
            params = kwargs.get('params', {})
            if not params:
                raise MissingParametersError("Missing request parameters {}".format(
                    ",".join(*[required_params])
                ))
            ExpertAiValidation().check_parameters(params=params)

    def get_method_name_for_endpoint(self, endpoint_path):
        return dict(constants.URLS_AND_METHODS).get(endpoint_path)

    def create_request(self, endpoint_path, params=None, body=None):
        http_method_name = self.get_method_name_for_endpoint(endpoint_path)
        if params:
            self.verify_request(endpoint_path, params=params)
            endpoint_path = endpoint_path.format(**params)

        return ExpertAiRequest(
            endpoint_path=endpoint_path,
            http_method_name=http_method_name,
            body=body
        )

    def full_analysis(self, params, body):
        request = self.create_request(
            endpoint_path=constants.FULL_ANALYSIS_PATH,
            params=params,
            body=body
        )
        return self.response_class(response=request.send())

    def specific_resource_analysis(self, params, body):
        request = self.create_request(
            endpoint_path=constants.SPECIFIC_RESOURCE_ANALYSIS_PATH,
            params=params,
            body=body
        )
        return self.response_class(response=request.send())

    def iptc_media_topics_classification(self, params, body):
        request = self.create_request(
            endpoint_path=constants.IPTC_MEDIA_TOPICS_CLASSIFICATION_PATH,
            params=params,
            body=body
        )
        return self.response_class(response=request.send())

    def contexts(self):
        request = self.create_request(endpoint_path=constants.CONTEXTS_PATH)
        return self.response_class(response=request.send())

    def contexts_standard(self):
        request = self.create_request(endpoint_path=constants.CONTEXTS_STANDARD_PATH)
        return self.response_class(response=request.send())

    def iptc_taxonomies_list(self):
        request = self.create_request(endpoint_path=constants.TAXONOMIES_LIST_PATH)
        return self.response_class(response=request.send())

    def iptc_taxonomies(self):
        request = self.create_request(endpoint_path=constants.IPTC_TAXONOMIES_PATH)
        return self.response_class(response=request.send())
