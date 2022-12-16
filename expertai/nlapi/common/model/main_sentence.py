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

from expertai.nlapi.common.model.position import Position


class MainSentence(Position):
    def __init__(self, value, score, start, end, **kwargs):
        super().__init__(start=start, end=end)
        self._value = value
        self._score = score

    @property
    def value(self):
        return self._value

    @property
    def score(self):
        return self._score
