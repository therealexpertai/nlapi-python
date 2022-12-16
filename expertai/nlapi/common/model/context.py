# Copyright (c) 2020 original authors
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from expertai.nlapi.common import constants
from expertai.nlapi.common.errors import ETypeError, EValueError

class ContextLanguage:
    def __init__(self, code, name="", analyses=[], **kwargs):
        self._code = code
        self._name = name
        self._analyses = analyses

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def analyses(self):
        return self._analyses        

class Context:
    def __init__(self, name, description, languages, contract=None, **kwargs):
        self._name = name
        self._description = description
        self._languages = []
        self._contract = contract

        if not isinstance(languages, list):
            raise ETypeError(languages, list)

        for lng in languages:
            if not isinstance(lng, dict):
                raise ETypeError(expected=dict, current=lng)

            if not lng:
                raise EValueError(lng, "Context.language")
            self._languages.append(ContextLanguage(**lng))

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def languages(self):
        return self._languages

    @property
    def contract(self):
        return self._contract
