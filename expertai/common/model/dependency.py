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

from expertai.common.errors import MissingArgumentError


class Dependency:
    def __init__(self, head, label, id=None, id_=None):
        """Initialise the Dependency object

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
        self._head = head
        self._label = label
        if id is None and id_ is None:
            raise MissingArgumentError("Missing required argument: id")
        self._id = id or id_

    @property
    def id_(self):
        return self._id

    @property
    def head(self):
        return self._head

    @property
    def label(self):
        return self._label
