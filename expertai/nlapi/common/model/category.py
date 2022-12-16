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


class Category:
    def __init__(
        self,
        namespace,
        label,
        hierarchy,
        frequency,
        score,
        winner,
        positions,
        id=None,
        id_=None,
        **kwargs
    ):
        """Initialise the Category object

        To minimise the `abuse` of the Python `type` id, the
        initialisation method also accepts `id_`. The former argument
        is used when the initialisation is nested inside other
        data-model classes. In these cases the __init__ receives a
        dictionary containing `type` not `id_`, because that how the
        response the server sends is defined. Otherwise when the object
        can be directly initialised using the second alternative.

        Again, to mitigate this name clash with the reserved keyword
        the property was suffixed with the underscore.
        """
        if id is None and id_ is None:
            raise MissingArgumentError("Missing required argument: id")
        if id is not None:
            self._id = id
        else:
            self._id = id_        

        self._namespace = namespace
        self._label = label
        self._hierarchy = hierarchy
        self._frequency = frequency
        self._score = score
        self._winner = winner
        self._positions = []
        if not isinstance(positions, list):
            raise ETypeError(list, positions)

        for position in positions:
            if not isinstance(position, dict):
                raise ETypeError(dict, position)
            if not position:
                raise EValueError(position, "Category.positions")

            self._positions.append(Position(**position))

    @property
    def id_(self):
        return self._id

    @property
    def namespace(self):
        return self._namespace

    @property
    def label(self):
        return self._label

    @property
    def hierarchy(self):
        return self._hierarchy

    @property
    def frequency(self):
        return self._frequency

    @property
    def score(self):
        return self._score

    @property
    def winner(self):
        return self._winner

    @property
    def positions(self):
        return self._positions
