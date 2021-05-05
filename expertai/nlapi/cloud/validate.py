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

from expertai.nlapi.common import constants
from expertai.nlapi.common.errors import ParameterError


class ExpertAiValidation:
    """
    To be consistent, every new method added to verify a value should be
    name according this pattern: [value_name]_value_is_correct
    """

    def language_value_is_correct(self, language):
        return language in constants.LANGUAGES.keys()
    def detector_value_is_correct(self, detector):
        return True;

    def resource_value_is_correct(self, resource):
        return resource in constants.RESOURCES_NAMES

    def context_value_is_correct(self, context):
        return True

    def taxonomy_value_is_correct(self, taxonomy):
        return True

    def check_name(self, param_name):
        if param_name not in constants.PARAMETER_NAMES:
            raise ParameterError("{} - invalid name".format(param_name))

    def check_value(self, param_name, value):
        method_name = "{}_value_is_correct".format(param_name)
        method = getattr(self, method_name)
        if not method(**{param_name: value}):
            raise ParameterError(
                "{} - invalid value: {}".format(param_name, value)
            )

    def check_parameters(self, params):
        for p_name, p_value in params.items():
            self.check_name(p_name)
            self.check_value(p_name, p_value)
