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

import re

from expertai.nlapi.v1 import constants
from expertai.nlapi.v1.errors import ExpertAiRequestError, MissingParametersError
from expertai.nlapi.v1.object_mapper import ObjectMapper
from expertai.nlapi.v1.request import ExpertAiRequest
from expertai.nlapi.v1.response import ExpertAiResponse
from expertai.nlapi.v1.validate import ExpertAiValidation


class ExpertAiClient:
    def __init__(self):
        self.response_class = ExpertAiResponse
        self._endpoint_path = ""

    def urlpath_keywords(self, endpoint_path):
        return re.findall(r"\{(\w+)\}", endpoint_path)

    def verify_request(self, endpoint_path, **kwargs):
        """
        Verify that the user has set all the required parameters.

        Some of the endpoint url paths are parameterised, therefore
        the user has to provide some value when setting up the
        endpoint method
        """
        required_params = self.urlpath_keywords(endpoint_path)
        if not required_params:
            return

        params = kwargs.get("params") or {}
        missing_params = set(required_params).difference(set(params.keys()))
        if required_params and missing_params:
            raise MissingParametersError(
                "Missing request parameters: {}".format(
                    ",".join(*[missing_params])
                )
            )
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
            body=body,
        )

    def process_response(self, response):
        if not response.successful:
            raise ExpertAiRequestError(
                "Response status code: {}".format(response.status_code)
            )
        elif response.bad_request:
            return ExpertAiRequestError(
                response.bad_request_message(response.json)
            )
        return ObjectMapper().read_json(response.json)

    def full_analysis(self, params, body):
        request = self.create_request(
            endpoint_path=constants.FULL_ANALYSIS_PATH,
            params=params,
            body=body,
        )
        response = self.response_class(response=request.send())
        return self.process_response(response)

    def specific_resource_analysis(self, params, body):
        request = self.create_request(
            endpoint_path=constants.SPECIFIC_RESOURCE_ANALYSIS_PATH,
            params=params,
            body=body,
        )
        response = self.response_class(response=request.send())
        return self.process_response(response)

    def iptc_media_topics_classification(self, params, body):
        request = self.create_request(
            endpoint_path=constants.IPTC_MEDIA_TOPICS_CLASSIFICATION_PATH,
            params=params,
            body=body,
        )
        response = self.response_class(response=request.send())
        return self.process_response(response)

    def contexts(self):
        request = self.create_request(endpoint_path=constants.CONTEXTS_PATH)
        response = self.response_class(response=request.send())
        return self.process_response(response)

    def contexts_standard(self):
        request = self.create_request(
            endpoint_path=constants.CONTEXTS_STANDARD_PATH
        )
        response = self.response_class(response=request.send())
        return self.process_response(response)

    def iptc_taxonomies_list(self):
        request = self.create_request(
            endpoint_path=constants.TAXONOMIES_LIST_PATH
        )
        response = self.response_class(response=request.send())
        return self.process_response(response)

    def iptc_taxonomies(self):
        request = self.create_request(
            endpoint_path=constants.IPTC_TAXONOMIES_PATH
        )
        response = self.response_class(response=request.send())
        return self.process_response(response)
