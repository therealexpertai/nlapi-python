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

from expertai.nlapi.v1 import constants


class Language:
    def __init__(self, name="", description=""):
        self._name = name
        self._description = description

    @property
    def get_language_by_name(self):
        return constants.LANGUAGES.get(self._name)

    @property
    def get_language_by_description(self):
        inv = dict((v, k) for k, v in constants.LANGUAGES.items())
        return inv.get(self._description)
