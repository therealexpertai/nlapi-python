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
import re
import hashlib
import json
import requests

from expertai.nlapi.common import constants
from expertai.nlapi.common.errors import ExpertAiRequestError, MissingParametersError
from expertai.nlapi.edge.object_mapper import ObjectMapper
from expertai.nlapi.edge.request import ExpertAiRequest
from expertai.nlapi.edge.response import ExpertAiResponse
from expertai.nlapi.edge.validate import ExpertAiValidation

def MD5_hash(s):
    m = hashlib.md5()
    m.update(s.encode())
    return m.hexdigest()

class ExpertAiClient:
    def __init__(self):
        self.response_class = ExpertAiResponse
        self._endpoint_path = ""
        self._host = "127.0.0.1"
        self._port = "6699"
        self._response = None
        self._resource = None
        self._use_https = False

    def _analysis(self, text, options):
        host = self._host + ":" + self._port

        ekey = self._get_execution_key(text)
        
        # call internal server with execution key for analysis
        body = {'document': {'text' : text}, 'options': options, 'resource': self._resource }
        header = {'Content-Type' : 'application/json', 'execution-key' : ekey}
        response = self.response_class(self.post_request(host, '/api/analyze', json.dumps(body), header))
        return self.process_response(response)

    def _get_execution_key(self, text):
        ekey = ""
        if (os.getenv(constants.USERNAME_ENV_VARIABLE)!=None) or (os.getenv(constants.TOKEN_ENV_VARIABLE)!=None):
            params = self.set_param(text)

            request = self.create_request(
                endpoint_path=constants.EXECUTION_KEY_PATH,
                params=params)
            response = request.send()
            if response.status_code != 200:
                raise ExpertAiRequestError(
                    "Response status code: {}".format(response.status_code)
                )
            ekey_response = json.loads(response.content.decode())
            if "key" in ekey_response:
                ekey = ekey_response["key"]
        return ekey

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
        self._response = response
        if not response.successful:
            raise ExpertAiRequestError(
                "Response status code: {}".format(response.status_code)
            )
        elif response.bad_request:
            return ExpertAiRequestError(
                response.bad_request_message(response.json)
            )
        return ObjectMapper().read_json(response.json)
    def get_json_response(self):
        if self._response:
            return self._response.json
        else:
            return {}

    def get_proto(self):
        if self._use_https:
            return 'https://'
        return 'http://'
    
    def post_request(self, host, uri, data, header={'Content-Type': 'application/json'}):
        curi = self.get_proto() + host + uri
        response = requests.post(curi, data=data, headers=header)    
        #return response.status_code, response.content.decode('utf-8')
        return response

    def get_request(self, host, uri):
        curi = self.get_proto() + host + uri
        return requests.get(curi)

    def set_host(self, host="127.0.0.1", port=6699):
        self._host = host
        self._port = str(port)

    def set_param(self, text):
        params = {}
        params["footprint"] = MD5_hash(text)
        return params

    def set_options(self, analysis=[], features=[]):
        options = {}
        features.append("syncpos")
        options["analysis"] = analysis
        options["features"] = features
        return options

    def set_resource(self, resource=None):
        self._resource = resource

    def use_https(self, https=True):
        self._use_https = https

    def full_analysis(self, text):
        options=self.set_options([ "disambiguation", "relevants", "entities", "sentiment", "relations" ], [ "knowledge", "dependency"])
        return self._analysis(text, options)

    def deep_linguistic_analysis(self, text):
        options=self.set_options([ "disambiguation" ], [ "knowledge", "dependency"])
        return self._analysis(text, options)

    def keyphrase_extraction(self, text):
        options=self.set_options([ "relevants" ], [ "knowledge" ])
        return self._analysis(text, options)

    def named_entity_recognition(self, text):
        options=self.set_options([ "entities" ], [ "knowledge" ])
        return self._analysis(text, options)

    def relations(self, text):
        options=self.set_options([ "relations" ], [ "knowledge", "dependency" ])
        return self._analysis(text, options)

    def sentiment(self, text):
        options=self.set_options([ "sentiment" ], [ "knowledge" ])
        return self._analysis(text, options)

    def classification(self, text):
        options=self.set_options([ "categories" ])
        return self._analysis(text, options)

    def extraction(self, text):
        options=self.set_options([ "extractions" ])
        return self._analysis(text, options)

    def taxonomy(self):
        host = self._host + ":" + self._port
        body = { "info" : "taxonomy", "resource" : self._resource } 
        header = {'Content-Type' : 'application/json' }    
        response = self.response_class(self.post_request(host, '/api/model', json.dumps(body), header))
        return self.process_response(response)

    def detection(self,text):
        options=self.set_options([ "disambiguation", "entities",'extractions' ], [ "knowledge","syncpos","extradata"])
        return self._analysis(text, options)

    def templates(self):
        host = self._host + ":" + self._port
        body = { "info" : "templates", "resource" : self._resource }
        header = {'Content-Type' : 'application/json' }    
        response = self.response_class(self.post_request(host, '/api/model', json.dumps(body), header))
        return self.process_response(response)

    def resources(self):
        host = self._host + ":" + self._port
        body = ""
        header = {'Content-Type' : 'application/json' }
        http_response = self.post_request(host, "/essex/packages", body, header)
        if http_response.status_code==constants.HTTP_SUCCESSFUL:
            j = http_response.json()
            if 'data' in j:
                return j['data']
        return []

    def statistics(self):
        host = self._host + ":" + self._port
        body = ""
        header = {'Content-Type' : 'application/json' }
        http_response = self.post_request(host, "/essex/statistics", body, header)
        if http_response.status_code==constants.HTTP_SUCCESSFUL:
            j = http_response.json()
            if 'data' in j:
                return j['data']
        return {}

    def health(self):
        host = self._host + ":" + self._port
        http_response = self.get_request(host, '/health')
        if http_response.status_code==constants.HTTP_SUCCESSFUL:
            return True
        return False
