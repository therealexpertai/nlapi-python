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

PHRASE_TYPE_VALUES = {
    "AP": "Adjective Phrase",
    "CP": "Conjunction Phrase",
    "CR": "Blank lines",
    "DP": "Adverb Phrase",
    "NP": "Noun Phrase",
    "PN": "Nominal Predicate ",
    "PP": "Preposition Phrase",
    "RP": "Relative Phrase",
    "VP": "Verb Phrase",
    "NA": "Not Applicable",
}


class PhraseType:
    def __init__(self, key="", description=""):
        self._key = key
        self._description = description

    @property
    def key_from_description(self):
        return dict((v, k) for k, v in PHRASE_TYPE_VALUES.items()).get(
            self._description
        )

    @property
    def description_from_key(self):
        return PHRASE_TYPE_VALUES.get(self._key)

    @property
    def key(self):
        return self._key

    @property
    def description(self):
        return self._description
