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

from nlapi.v1.model.atom import Atom
from nlapi.v1.model.category import Category
from nlapi.v1.model.data_model import DataModel
from nlapi.v1.model.dependency import Dependency
from nlapi.v1.model.entity import Entity
from nlapi.v1.model.entity_type import ENTITY_TYPE_VALUES, EntityType
from nlapi.v1.model.eproperty import Property
from nlapi.v1.model.iptc import Iptc
from nlapi.v1.model.knowledge import Knowledge
from nlapi.v1.model.language import Language
from nlapi.v1.model.main_lemma import MainLemma
from nlapi.v1.model.main_phrase import MainPhrase
from nlapi.v1.model.main_sentence import MainSentence
from nlapi.v1.model.main_syncon import MainSyncon
from nlapi.v1.model.paragraph import Paragraph
from nlapi.v1.model.phrase import Phrase
from nlapi.v1.model.phrase_type import PhraseType
from nlapi.v1.model.pos_tag import PosTag
from nlapi.v1.model.position import Position
from nlapi.v1.model.sentence import Sentence
from nlapi.v1.model.standard import Standard
from nlapi.v1.model.token import Token
from nlapi.v1.model.token_type import TokenType
from nlapi.v1.model.topic import Topic
from nlapi.v1.model.vsyncon import VSyncon

__all__ = [
    "Atom",
    "Category",
    "DataModel",
    "Dependency",
    "Entity",
    "EntityType",
    "ENTITY_TYPE_VALUES",
    "Iptc",
    "Property",
    "Knowledge",
    "Language",
    "MainLemma",
    "MainPhrase",
    "MainSentence",
    "MainSyncon",
    "Paragraph",
    "Phrase",
    "PhraseType",
    "Position",
    "PosTag",
    "Sentence",
    "Standard",
    "Token",
    "TokenType",
    "Topic",
    "VSyncon",
]
