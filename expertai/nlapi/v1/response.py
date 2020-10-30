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

from expertai.nlapi.v1 import constants


class ExpertAiResponse:
    def __init__(self, response, **kwargs):
        """
        :param response: the HTTP Response object (of type requests.Response)
        returned from the request
        Status-code should not be accessed from the outside. The properties
        should be used instead.
        """
        self.http_response = response

    @property
    def status_code(self):
        return self.http_response.status_code

    @property
    def status(self):
        if self.status_code in constants.HTTP_ERRORS:
            return constants.HTTP_ERRORS[self.status_code]
        elif self.ok:
            if self.json.get("success") == False or self.json.get("errors"):
                return constants.BAD_REQUEST

            return constants.SUCCESSFUL
        return constants.UNKNOWN

    @property
    def json(self):
        if not self.ok:
            return {}
        return self.http_response.json()

    @property
    def invalid_status_code(self):
        return self.status_code is None

    @property
    def ok(self):
        return self.status_code == constants.HTTP_SUCCESSFUL

    @property
    def error(self):
        return self.status_code in constants.HTTP_ERRORS

    @property
    def successful(self):
        return self.status == constants.SUCCESSFUL

    @property
    def bad_request(self):
        return self.status == constants.BAD_REQUEST

    def bad_request_message(self, json):
        errors = json.get("errors", [])
        return " ".join(
            ["({code}, {message})".format(**err) for err in errors]
        )
