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

class Field:
    def __init__(self, name, type, **kwargs):
        self._name = name
        self._type = type

    @property
    def name(self):
        return self._name

    @property
    def type_(self):
        return self._type

class Template:
    def __init__(self, name, fields, **kwargs):
        self._name = name
        self._fields = []

        if not isinstance(fields, list):
            raise ETypeError(fields, list)

        for fld in fields:
            if not isinstance(fld, dict):
                raise ETypeError(expected=dict, current=fld)

            if not fld:
                raise EValueError(fld, "Template.fields")
            self.fields.append(Field(**fld))

    @property
    def name(self):
        return self._name

    @property
    def fields(self):
        return self._fields
