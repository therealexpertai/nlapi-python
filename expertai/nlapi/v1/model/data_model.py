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

from expertai.nlapi.v1.model.category import Category
from expertai.nlapi.v1.model.entity import Entity
from expertai.nlapi.v1.model.iptc import Iptc
from expertai.nlapi.v1.model.knowledge import Knowledge
from expertai.nlapi.v1.model.main_lemma import MainLemma
from expertai.nlapi.v1.model.main_phrase import MainPhrase
from expertai.nlapi.v1.model.main_sentence import MainSentence
from expertai.nlapi.v1.model.main_syncon import MainSyncon
from expertai.nlapi.v1.model.paragraph import Paragraph
from expertai.nlapi.v1.model.phrase import Phrase
from expertai.nlapi.v1.model.sentence import Sentence
from expertai.nlapi.v1.model.standard import Standard
from expertai.nlapi.v1.model.token import Token
from expertai.nlapi.v1.model.topic import Topic


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
        categories=[],
        iptc={},
        standard={},
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
        self._categories = [Category(**cat) for cat in categories]
        self._iptc = Iptc(**iptc) if iptc else None
        self._standard = Standard(**standard) if standard else None

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
    def categories(self):
        return self._categories

    @property
    def iptc(self):
        return self._iptc

    @property
    def standard(self):
        return self._standard
