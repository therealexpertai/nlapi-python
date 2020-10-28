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

from nlapi.common.model.atom import Atom
from nlapi.common.model.category import Category
from nlapi.common.model.data_model import DataModel
from nlapi.common.model.dependency import Dependency
from nlapi.common.model.entity import Entity
from nlapi.common.model.entity import Attribute
from nlapi.common.model.eproperty import Property
from nlapi.common.model.iptc import Iptc
from nlapi.common.model.knowledge import Knowledge
from nlapi.common.model.language import Language
from nlapi.common.model.main_lemma import MainLemma
from nlapi.common.model.main_phrase import MainPhrase
from nlapi.common.model.main_sentence import MainSentence
from nlapi.common.model.main_syncon import MainSyncon
from nlapi.common.model.paragraph import Paragraph
from nlapi.common.model.phrase import Phrase
from nlapi.common.model.position import Position
from nlapi.common.model.sentence import Sentence
from nlapi.common.model.standard import Standard
from nlapi.common.model.token import Token
from nlapi.common.model.topic import Topic
from nlapi.common.model.vsyncon import VSyncon
from nlapi.common.model.relation import Relation
from nlapi.common.model.relation import Verb
from nlapi.common.model.relation import Related
from nlapi.common.model.sentiment import Sentiment
from nlapi.common.model.sentiment import Items
from nlapi.common.model.context import Context
from nlapi.common.model.taxonomy import TaxonomyList
from nlapi.common.model.taxonomy import Taxonomy

__all__ = [
    "Atom",
    "Category",
    "DataModel",
    "Dependency",
    "Entity",
    "Attribute",
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
    "Position",
    "Sentence",
    "Standard",
    "Token",
    "Topic",
    "VSyncon",
    "Verb",    
    "Related",    
    "Relation",    
    "Sentiment",    
    "Items",    
    "Context",
    "TaxonomyList",
    "Taxonomy"
]
