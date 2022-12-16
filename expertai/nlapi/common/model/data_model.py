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

from expertai.nlapi.common.model.category import Category
from expertai.nlapi.common.model.entity import Entity
from expertai.nlapi.common.model.iptc import Iptc
from expertai.nlapi.common.model.knowledge import Knowledge
from expertai.nlapi.common.model.main_lemma import MainLemma
from expertai.nlapi.common.model.main_phrase import MainPhrase
from expertai.nlapi.common.model.main_sentence import MainSentence
from expertai.nlapi.common.model.main_syncon import MainSyncon
from expertai.nlapi.common.model.paragraph import Paragraph
from expertai.nlapi.common.model.phrase import Phrase
from expertai.nlapi.common.model.sentence import Sentence
from expertai.nlapi.common.model.sentiment import Sentiment
from expertai.nlapi.common.model.relation import Relation
from expertai.nlapi.common.model.standard import Standard
from expertai.nlapi.common.model.token import Token
from expertai.nlapi.common.model.topic import Topic
from expertai.nlapi.common.model.context import Context
from expertai.nlapi.common.model.taxonomy import TaxonomyList
from expertai.nlapi.common.model.taxonomy import Taxonomy
from expertai.nlapi.common.model.template import Template
from expertai.nlapi.common.model.template import Field
from expertai.nlapi.common.model.extraction import Extraction

class DataModel:
    """
    This class can be considered the root of the data model structure.

    All other classes are initialised from here. The ObjectMapper handles
    the JSON contained in the API response to this class. Not all the
    arguments might be valued. It depends on the type of document analysis
    that was requested.

    No intrigued logic is stored inside these classes, aside from the
    getter/setter methods. This choice was intentional so that it would be
    possible, with a small effort, to replaces those classes with the
    definition of a database tables.
    """

    def __init__(
        self,
        content="",
        language="",
        version="",
        knowledge=[],
        tokens=[],
        phrases=[],
        sentences=[],
        paragraphs=[],
        topics=[],
        main_sentences=[],
        main_phrases=[],
        main_lemmas=[],
        main_syncons=[],
        entities=[],
        sentiment={},
        relations=[],
        categories=[],
        iptc={},
        standard={},
        contexts=[],
        taxonomies=[],
        templates=[],        
        extractions=[],                
        data=[],
        extra_data={},
        detectors=[],
        **kwargs
    ):
        self._content = content
        self._language = language
        self._version = version
        self._knowledge = [Knowledge(**kw) for kw in knowledge]
        self._tokens = [Token(**tok) for tok in tokens]
        self._phrases = [Phrase(**ph) for ph in phrases]
        self._sentences = [Sentence(**s) for s in sentences]
        self._paragraphs = [Paragraph(**par) for par in paragraphs]
        self._topics = [Topic(**t) for t in topics]
        self._main_sentences = [MainSentence(**ms) for ms in main_sentences]
        self._main_phrases = [MainPhrase(**mp) for mp in main_phrases]
        self._main_lemmas = [MainLemma(**ml) for ml in main_lemmas]
        self._main_syncons = [MainSyncon(**ms) for ms in main_syncons]
        self._entities = [Entity(**ent) for ent in entities]
        self._sentiment = Sentiment(**sentiment) if sentiment else None
        self._relations = [Relation(**rel) for rel in relations]
        self._categories = [Category(**cat) for cat in categories]
        self._iptc = Iptc(**iptc) if iptc else None
        self._standard = Standard(**standard) if standard else None
        self._contexts = [Context(**ctx) for ctx in contexts]
        self._taxonomies = [TaxonomyList(**txn) for txn in taxonomies]
        self._taxonomy = [Taxonomy(**dtx) for dtx in data]
        self._templates = [Template(**tpl) for tpl in templates]
        self._extractions = [Extraction(**ext) for ext in extractions]
        self._extra_data = extra_data
        self._detectors = [Context(**ctx) for ctx in detectors]

    @property
    def content(self):
        return self._content

    @property
    def language(self):
        return self._language

    @property
    def version(self):
        return self._version

    @property
    def knowledge(self):
        return self._knowledge

    @property
    def tokens(self):
        return self._tokens

    @property
    def phrases(self):
        return self._phrases

    @property
    def sentences(self):
        return self._sentences

    @property
    def paragraphs(self):
        return self._paragraphs

    @property
    def topics(self):
        return self._topics

    @property
    def main_sentences(self):
        return self._main_sentences

    @property
    def main_phrases(self):
        return self._main_phrases

    @property
    def main_lemmas(self):
        return self._main_lemmas

    @property
    def main_syncons(self):
        return self._main_syncons

    @property
    def entities(self):
        return self._entities

    @property
    def sentiment(self):
        return self._sentiment

    @property
    def relations(self):
        return self._relations

    @property
    def categories(self):
        return self._categories

    @property
    def iptc(self):
        return self._iptc

    @property
    def standard(self):
        return self._standard

    @property
    def contexts(self):
        return self._contexts

    @property
    def detectors(self):
        return self._detectors

    @property
    def taxonomies(self):
        return self._taxonomies        

    @property
    def taxonomy(self):
        return self._taxonomy                

    @property
    def templates(self):
        return self._templates                

    @property
    def extractions(self):
        return self._extractions  
    
    @property
    def extra_data(self):
        return self._extra_data
