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


class Property:
    """
    This  a module is named eproperty to avoid clashing with
    the Python's reserved keyword `property`.
    """

    def __init__(self, value, type=None, type_=None, **kwargs):
        """Initialise the Property object

        To minimise the `abuse` of the Python `type` keyword, the
        initialisation method also accepts `type_`. The former argument
        is used when the initialisation is nested inside other
        data-model classes. In these cases the __init__ receives a
        dictionary containing `type` not `type_`, because that how the
        response the server sends is defined. Otherwise when the object
        can be directly initialised using the second alternative.

        Again, to mitigate this name clash with the reserved keyword
        the property was suffixed with the underscore.
        """
        self._type = type_ or type
        self._value = value

    @property
    def type_(self):
        return self._type

    @property
    def value(self):
        return self._value
