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
from expertai.authentication import ExpertAiAuth
from expertai.errors import CredentialsError, ExpertAiRequestError


class ExpertAiResponse:
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



