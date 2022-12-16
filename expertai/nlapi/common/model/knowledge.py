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
from expertai.nlapi.common.model.eproperty import Property


class Knowledge:
    def __init__(self, syncon, label, properties=[], **kwargs):
        self._syncon = syncon
        self._label = label
        self._properties = []

        if not isinstance(properties, list):
            raise ETypeError(properties, list)

        for prop in properties:
            if not isinstance(prop, dict):
                import pdb

                pdb.set_trace()
                raise ETypeError(expected=dict, current=prop)
            if not prop:
                raise EValueError(prop, "Knowledge.properties")

            self._properties.append(Property(**prop))

    @property
    def syncon(self):
        return self._syncon

    @property
    def label(self):
        return self._label

    @property
    def properties(self):
        return self._properties
