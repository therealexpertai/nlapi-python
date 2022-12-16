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
from expertai.nlapi.common.model.phrase import Phrase
from expertai.nlapi.common.model.position import Position


class Sentence(Position):
    def __init__(self, phrases, start, end, **kwargs):
        super().__init__(start=start, end=end)
        self._phrases = []
        if not isinstance(phrases, list):
            raise ETypeError(phrases, list)

        for phrase in phrases:
            if not isinstance(phrase, dict):
                raise ETypeError(expected=dict, current=phrase)

            if not phrase:
                raise EValueError(phrase, "Sentence.phrase")

            self._phrases.append(Phrase(**phrase))

    @property
    def phrases(self):
        return self._phrases
