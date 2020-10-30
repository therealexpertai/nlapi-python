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

from expertai.nlapi.common.errors import ETypeError, EValueError
from expertai.nlapi.common.model.language import Language


class Iptc:
    def __init__(self, description, languages):
        self._description = description
        self._languages = []

        if not isinstance(languages, list):
            raise ETypeError(languages, list)

        for language in languages:
            if not isinstance(language, dict):
                raise ETypeError(expected=list, current=language)
            if not language:
                raise EValueError(language, "Iptc.languages")

            self._languages.append(Language(**language))

    @property
    def languages(self):
        return self._languages

    @property
    def description(self):
        return self._description
