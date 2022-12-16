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

from expertai.nlapi.common.errors import ETypeError, EValueError, MissingArgumentError
from expertai.nlapi.common.model.position import Position

class ExtractionField:
    def __init__(self, name, value, positions=[], **kwargs):
        self._name = name
        self._value = value

        self._positions = []
        if not isinstance(positions, list):
            raise ETypeError(positions, list)

        for position in positions:
            if not isinstance(position, dict):
                raise ETypeError(expected=dict, current=position)
            if not position:
                raise EValueError(position, "ExtractionField.positions")

            self._positions.append(Position(**position))        

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @property
    def positions(self):
        return self._positions
        
class Extraction:
    def __init__(
        self,
        namespace,
        template,
        fields,
        **kwargs
    ):

        if not template:
            raise MissingArgumentError("Missing required argument: template")
        self._template = template

        self._namespace = namespace
        self._fields = []

        if not isinstance(fields, list):
            raise ETypeError(list, fields)

        for fld in fields:
            if not isinstance(fld, dict):
                raise ETypeError(dict, fld)
            if not fld:
                raise EValueError(fld, "Extraction.fields")

            self._fields.append(ExtractionField(**fld))

    @property
    def namespace(self):
        return self._namespace

    @property
    def template(self):
        return self._template

    @property
    def fields(self):
        return self._fields
