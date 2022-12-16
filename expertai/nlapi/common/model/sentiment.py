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

class Items:
    def __init__(self, lemma, syncon, sentiment, items=[], **kwargs):
        self._lemma = lemma
        self._syncon = syncon
        self._sentiment = sentiment
        self._items = []

        if not isinstance(items, list):
            raise ETypeError(items, list)

        for itm in items:
            if not isinstance(itm, dict):
                raise ETypeError(expected=dict, current=itm)

            if not itm:
                raise EValueError(itm, "Sentiment.items")

            self._items.append(Items(**itm))

    @property
    def lemma(self):
        return self._lemma

    @property
    def syncon(self):
        return self._syncon

    @property
    def sentiment(self):
        return self._sentiment

    @property
    def items(self):
        return self._items        

class Sentiment:
    def __init__(self, overall, negativity, positivity, items=[], **kwargs):
        self._overall = overall
        self._negativity = negativity
        self._positivity = positivity
        self._items = []

        if not isinstance(items, list):
            raise ETypeError(items, list)

        for itm in items:
            if not isinstance(itm, dict):
                raise ETypeError(expected=dict, current=itm)

            if not itm:
                raise EValueError(itm, "Sentiment.items")

            self._items.append(Items(**itm))

    @property
    def overall(self):
        return self._overall

    @property
    def negativity(self):
        return self._negativity

    @property
    def positivity(self):
        return self._positivity

    @property
    def items(self):
        return self._items