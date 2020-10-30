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

import requests

from expertai.nlapi.common import constants
from expertai.nlapi.common.authentication import ExpertAiAuth
from expertai.nlapi.common.errors import ExpertAiRequestError


class ExpertAiRequest:
    def __init__(self, endpoint_path, http_method_name, **kwargs):
        self._endpoint_path = endpoint_path
        self.string_method = http_method_name
        self._body = kwargs.get("body")

    @property
    def url(self):
        return "{}/{}".format(constants.BASE_EDGE_URL, self._endpoint_path)

    @property
    def headers(self):
        header = ExpertAiAuth().header
        header.update(**{"Content-Type": "text/plain"})
        header.update(**{"Cache-Control": "no-cache"})
        return header

    def send(self):
        """
        Transmits the real HTTP request

        The reason why the Exception being caught is IOError is that
        pure network exceptions triggered by the request library are
        subclasses of IOError.

        Although all exceptions that Requests explicitly raises
        inherit from requests.exceptions.RequestException, the only
        way to catch them is to user the super-super class, which
        in this case is IOError
        """
        try:
            http_method, req_parameters = self.setup_raw_request()
            return http_method(**req_parameters)
        except IOError as e:
            raise ExpertAiRequestError(
                "The following error occurred: {exception}".format(
                    exception=e.__class__.__name__
                )
            )

    def setup_raw_request(self):
        req_parameters = {"url": self.url, "headers": self.headers}
        if self._body:
            req_parameters.update(json=self._body)

        if self.string_method == constants.HTTP_GET:
            http_method = requests.get
        else:
            http_method = requests.post
        return http_method, req_parameters

        