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

class Verb:
    def __init__(self, text, lemma, syncon, phrase, relevance, type=None, type_=None, **kwargs):
        self._text = text
        self._lemma = lemma
        self._syncon = syncon
        self._phrase = phrase
        self._relevance = relevance
        self._type = type or type_

    @property
    def text(self):
        return self._text        

    @property
    def lemma(self):
        return self._lemma

    @property
    def syncon(self):
        return self._syncon

    @property
    def phrase(self):
        return self._phrase

    @property
    def relevance(self):
        return self._relevance

    @property
    def type_(self):
        return self._type        

class Related:
    def __init__(self, relation, text, lemma, syncon, phrase, relevance, related=[], type=None, type_=None, **kwargs):
        self._relation = relation
        self._text = text
        self._lemma = lemma
        self._syncon = syncon
        self._phrase = phrase
        self._relevance = relevance
        self._type = type or type_
        self._related = []

        if not isinstance(related, list):
            raise ETypeError(related, list)

        for rel in related:
            if not isinstance(rel, dict):
                raise ETypeError(expected=dict, current=rel)

            if not rel:
                raise EValueError(rel, "Relation.related")

            self._related.append(Related(**rel))

    @property
    def relation(self):
        return self._relation        

    @property
    def text(self):
        return self._text        

    @property
    def lemma(self):
        return self._lemma

    @property
    def syncon(self):
        return self._syncon

    @property
    def phrase(self):
        return self._phrase

    @property
    def relevance(self):
        return self._relevance

    @property
    def type_(self):
        return self._type        

    @property
    def related(self):
        return self._related        

class Relation:
    def __init__(self, verb, related=[], **kwargs):
        self._verb = {}
        self._related = []

        if not isinstance(verb, dict):
            raise ETypeError(verb, dict)
        if not verb:
            raise EValueError(verb, "Relation.verb")
        self._verb = Verb(**verb)

        if not isinstance(related, list):
            raise ETypeError(related, list)

        for rel in related:
            if not isinstance(rel, dict):
                raise ETypeError(expected=dict, current=rel)

            if not rel:
                raise EValueError(rel, "Relation.related")

            self._related.append(Related(**rel))

    @property
    def verb(self):
        return self._verb

    @property
    def related(self):
        return self._related