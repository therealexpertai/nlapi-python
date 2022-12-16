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

from expertai.nlapi.common.errors import MissingArgumentError
from expertai.nlapi.common.model.position import Position


class Atom(Position):
    def __init__(self, lemma, start, end, type=None, type_=None, **kwargs):
        """Initialise the Atom object

        To minimise the `abuse` of the Python `type` keyword, the
        initialisation method also accepts `type_`. The former argument
        is used when the initialisation is nested inside other
        data-model classes. In these cases the __init__ receives a
        dictionary containing `type` not `type_`, because that how the
        response the server sends is defined. Otherwise when the object
        can be directly initialised using the second alternative.
        Again, to mitigate this name clash with the keyword the property
        was suffixed with the underscore.
        """
        super().__init__(start=start, end=end)

        self._type = type_ or type
        if not self._type:
            raise MissingArgumentError("Missing required argument type")
        self._lemma = lemma

    @property
    def type_(self):
        return self._type

    @property
    def lemma(self):
        return self._lemma
