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

from lib import constants
from lib.errors import CredentialsError, ExpertRequestError, MissingParameterError


class ExpertAuth:

    @property
    def header(self):
        value = constants.AUTH_HEADER_VALUE.format(self.fetch_token_value())
        return {constants.AUTH_HEADER_KEY: value}

    @property
    def username(self):
        value = os.getenv(constants.USERNAME_ENV_VARIABLE)
        if not value:
            raise CredentialsError("Missing username env variable")
        return value

    @property
    def password(self):
        value = os.getenv(constants.PASSWORD_ENV_VARIABLE)
        if not value:
            raise CredentialsError("Missing password env variable")
        return value

    def refresh_token_value(self):
        pass

    def write_token_timestamp(self):
        with open(constants.TK_TIMESTAMP_FILENAME, 'w') as fp:
            fp.write(datetime.now().isoformat())
    
    def fetch_token_value(self):
        response = requests.post(
            url=constants.OAUTH2_TOKEN_URL,
            headers=constants.CONTENT_TYPE_HEADER,
            json={"username": self.username, "password": self.password}
        )
        if not response.ok:
            raise ExpertRequestError(
                "Failed to fetch the Bearer Token. Status code: ".format(
                    response.status_code
                )
            )
        return response.text
    

class ExpertRequest:

    def __init__(self, endpoint_path, http_method_name, **kwargs):
        self._endpoint_path = endpoint_path
        self.string_method = http_method_name
        self._body = kwargs.get('body')

    @property
    def url(self):
        return "{}/{}".format(constants.BASE_API_URL, self._endpoint_path)

    @property
    def headers(self):
        header = ExpertAuth().header
        header.update(**{'Content-Type': 'application/json'})
        return header

    def send(self):
        """
        TODO: doc why IOError
        """
        try:
            http_method, req_parameters = self.setup_raw_request()
            return http_method(**req_parameters)
        except IOError as e:
            raise ExpertRequestError(
                "The following error occurred: {exception}".format(
                    exception=e.__class__.__name__))

    def setup_raw_request(self):
        req_parameters = {
            'url': self.url,
            'headers': self.headers
        }
        if self._body:
            req_parameters.update(json=self._body)

        if self.string_method == 'GET':
            http_method = requests.get
        else:
            http_method = requests.post
        return http_method, req_parameters


class ExpertResponse:
    def __init__(self, response, **kwargs):
        """
        :param response: the HTTP Response object (of type requests.Response)
        returned from the request
        Status-code should not be accessed from the outside. The properties 
        should be used instead.
        """
        self.http_response = response
        self._status_code = self.http_response.status_code

    def parse_data(self):
        if not self.successful:
            return None
        return self.http_response.json()

    @property
    def status_code(self):
        return self._status_code
    
    @property
    def json(self):
        return self.parse_data()

    @property
    def invalid_status_code(self):
        return self._status_code is None

    @property
    def successful(self):
        return self._status_code == constants.HTTP_OK

    @property
    def unauthorized(self):
        return self._status_code == constants.HTTP_UNAUTHORIZED

    @property
    def forbidden(self):
        return self._status_code == constants.HTTP_FORBIDDEN

    @property
    def not_found(self):
        return self._status_code == constants.HTTP_NOT_FOUND

    @property
    def error(self):
        return self._status_code in constants.HTTP_ERRORS

    @property
    def bad_request(self):
        return False


class ExpertClient:
    def __init__(self):
        self.response_class = ExpertResponse
        self._endpoint_path = ""

    def need_formatting(self, endpoint_path):
        return endpoint_path.find('{') > 0

    def missing_parameters(self, endpoint_path):
        return re.findall(r'(\{\w+\})', endpoint_path)
    
    def format_enpoint(self, endpoint_path, **kwargs):
        if not self.need_formatting(endpoint_path):
            return endpoint_path
        params = kwargs.get('params', {})
        try:
            endpoint_path = endpoint_path.format(**params)
        except KeyError:
            missing_parameters = self.missing_parameters(endpoint_path)
            raise MissingParameterError(
                "Expecting request parameters: {}".format(missing_parameters)
            )
        return endpoint_path

    def get_method_name_for_endpoint(self, endpoint_path):
        return dict(constants.URLS_AND_METHODS).get(endpoint_path)

    def create_request(self, endpoint_path, params=None, body=None):
        http_method_name = self.get_method_name_for_endpoint(endpoint_path)
        formatted_path = self.format_enpoint(endpoint_path, params=params)

        return ExpertRequest(
            endpoint_path=formatted_path,
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
