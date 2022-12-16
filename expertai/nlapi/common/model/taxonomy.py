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

class TaxoLanguage:
    def __init__(self, code, name="", **kwargs):
        self._code = code
        self._name = name

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

class TaxonomyList:
    def __init__(self, name, description, languages, contract="", **kwargs):
        self._name = name
        self._description = description
        self._contract = contract
        self._languages = []

        if not isinstance(languages, list):
            raise ETypeError(languages, list)

        for lng in languages:
            if not isinstance(lng, dict):
                raise ETypeError(expected=dict, current=lng)

            if not lng:
                raise EValueError(lng, "Context.language")
            self._languages.append(TaxoLanguage(**lng))

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def contract(self):
        return self._contract


    @property
    def languages(self):
        return self._languages

class Categories:
    def __init__(self, id, label="", categories=[], **kwargs):
        self._id = id
        self._label = label
        self._categories = []

        if not isinstance(categories, list):
            raise ETypeError(categories, list)

        for ctg in categories:
            if not isinstance(ctg, dict):
                raise ETypeError(expected=dict, current=ctg)

            if not ctg:
                raise EValueError(ctg, "Category.categories")
            self._categories.append(Categories(**ctg))

    @property
    def id(self):
        return self._id

    @property
    def label(self):
        return self._label

    @property
    def categories(self):
        return self._categories        

class Taxonomy:
    def __init__(self, namespace, taxonomy, **kwargs):
        self._namespace = namespace
        self._categories = []

        if not isinstance(taxonomy, list):
            raise ETypeError(taxonomy, list)

        for txn in taxonomy:
            if not isinstance(txn, dict):
                raise ETypeError(expected=dict, current=txn)

            if not txn:
                raise EValueError(txn, "Taxonomy.taxonomy")
            self._categories.append(Categories(**txn))

    @property
    def namespace(self):
        return self._namespace

    @property
    def categories(self):
        return self._categories        