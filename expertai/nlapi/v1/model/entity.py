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

from expertai.nlapi.v1.errors import ETypeError, EValueError, MissingArgumentError
from expertai.nlapi.v1.model.entity_type import EntityType
from expertai.nlapi.v1.model.position import Position


class Entity:
    def __init__(self, syncon, lemma, positions, type=None, type_=None):
        """Initialise the Entity object

        To minimise the `abuse` of the Python `type` keyword, the
        initialisation method also accepts `type_`. The former argument
        is used when the initialisation is nested inside other
        data-model classes. In these cases the __init__ receives a
        dictionary containing `type` not `type_`, because that how the
        response the server sends is defined. Otherwise when the object
        can be directly initialised using the second alternative.
        Again, to mitigate this name clash with the keyword the property
        was suffixed with the underscore.

        In the remote case a position dictionary is empty, the Position
        is not initialised to prevent an error to be raised.
        """
        self._syncon = syncon
        self._positions = []
        if not (type or type_):
            raise MissingArgumentError("Missing required argument type")

        self._type = EntityType(key=type_ or type)
        self._lemma = lemma

        if not isinstance(positions, list):
            raise ETypeError(positions, list)

        for position in positions:
            if not isinstance(position, dict):
                raise ETypeError(expected=dict, current=position)
            if not position:
                raise EValueError(position, "Entity.positions")

            self._positions.append(Position(**position))

    @property
    def syncon(self):
        return self._syncon

    @property
    def type_(self):
        return self._type

    @property
    def lemma(self):
        return self._lemma

    @property
    def positions(self):
        return self._positions
