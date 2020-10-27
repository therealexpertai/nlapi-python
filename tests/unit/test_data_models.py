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

from expertai.common.errors import ETypeError, EValueError, MissingArgumentError
from expertai.common.model import *
from tests import BaseTestCase


class DataModelsTestCase(BaseTestCase):

    def test_a_sentiment_object_is_initialised(self):
        stm = Sentiment(overall=-14.8, negativity=-14.89, positivity=0.1)
        self.assertEqual(stm.overall, -14.8)
        self.assertEqual(stm.negativity, -14.89)        
        self.assertEqual(stm.positivity, 0.1)

    def test_a_sentiment_object_is_initialised_json(self):
        stm = Sentiment(**{
            "overall": -14.8,
            "negativity": -14.89,
            "positivity": 0.1,
            "items": [
                {
                    "lemma": "Salman",
                    "syncon": -1,
                    "sentiment": 0.0,
                    "items": [{
                            "lemma": "government",
                            "syncon": 103596,
                            "sentiment": 3.5,
                            "items": [{
                                    "lemma": "call on",
                                    "syncon": 72091,
                                    "sentiment": 3.5
                                }
                            ]
                        }, {
                            "lemma": "threat",
                            "syncon": 59667,
                            "sentiment": -3.5,
                            "items": [{
                                    "lemma": "confront",
                                    "syncon": 65803,
                                    "sentiment": -3.5
                                }
                            ]
                        }
                    ]
                }            
            ]
          }
        )    
        self.assertEqual(stm.overall, -14.8)
        self.assertEqual(stm.negativity, -14.89)        
        self.assertEqual(stm.positivity, 0.1)
        self.assertEqual(stm.items[0].lemma, "Salman")
        self.assertEqual(stm.items[0].items[0].syncon, 103596)
        self.assertEqual(stm.items[0].items[0].items[0].sentiment, 3.5)


    def test_a_verb_object_is_initialised(self):
        """
        ...then verify that type_ argument is correctly handled
        """
        vrb = Verb(text="called on", lemma="call on", syncon=72091, phrase=2, type="MOV", relevance=12)
        self.assertEqual(vrb.type_, "MOV")
        self.assertEqual(vrb.text, "called on")        
        self.assertEqual(vrb.lemma, "call on")
        self.assertEqual(vrb.syncon, 72091)
        self.assertEqual(vrb.phrase, 2)
        self.assertEqual(vrb.relevance, 12)

    def test_a_related_object_is_initialised(self):
        """
        ...then verify that type_ argument is correctly handled
        """
        rel = Related(relation="sbj_who", text="Saudi King Salman", lemma="Salman", syncon=-1, phrase=2, type="NPH", relevance=12)
        self.assertEqual(rel.relation, "sbj_who")
        self.assertEqual(rel.type_, "NPH")
        self.assertEqual(rel.text, "Saudi King Salman")        
        self.assertEqual(rel.lemma, "Salman")
        self.assertEqual(rel.syncon, -1)
        self.assertEqual(rel.phrase, 2)
        self.assertEqual(rel.relevance, 12)

    def test_a_related_object_is_initialised_json(self):
        """
        ...then verify that type_ argument is correctly handled
        """
        rel = Related(**{
                        "relation": "obj_who",
                        "text": "governments",
                        "lemma": "government",
                        "syncon": 103596,
                        "type": "org",
                        "phrase": 5,
                        "relevance": 3
                    }
        )  
        self.assertEqual(rel.relation, "obj_who")
        self.assertEqual(rel.type_, "org")
        self.assertEqual(rel.text, "governments")        
        self.assertEqual(rel.lemma, "government")
        self.assertEqual(rel.syncon, 103596)
        self.assertEqual(rel.phrase, 5)
        self.assertEqual(rel.relevance, 3)             

    def test_a_relation_object_is_initialised_json(self):
        rel = Relation(**{
                "verb": {
                    "text": "called on",
                    "lemma": "call on",
                    "syncon": 72091,
                    "phrase": -1,
                    "type": "MOV",
                    "relevance": 12
                },
                "related": [{
                        "relation": "sbj_who",
                        "text": "Saudi King Salman",
                        "lemma": "Salman",
                        "syncon": -1,
                        "type": "NPH",
                        "phrase": 3,
                        "relevance": 12
                    }, {
                        "relation": "obj_who",
                        "text": "governments",
                        "lemma": "government",
                        "syncon": 103596,
                        "type": "org",
                        "phrase": 5,
                        "relevance": 3
                    }, {
                        "relation": "around_what",
                        "text": "around the world",
                        "lemma": "world",
                        "syncon": 99794,
                        "type": "",
                        "phrase": 6,
                        "relevance": 2
                    }
                ]
            }
        )
        self.assertEqual(rel.verb.lemma, "call on")
        self.assertEqual(rel.related[0].phrase, 3)
        self.assertEqual(rel.related[1].lemma, "government")
        self.assertEqual(rel.related[2].relevance, 2)

    def test_a_atom_object_is_initialised(self):
        """
        ...then verify that type_ argument is correctly handled
        """
        atom = Atom(end=45, lemma="basketball", start=35, type_="NOU")
        self.assertEqual(atom.type_, "NOU")
        self.assertEqual(atom.lemma, "basketball")
        self.assertEqual(atom.start, 35)
        self.assertEqual(atom.end, 45)

    def test_a_atom_object_is_initialised_but_the_type_is_not_provided(self):
        """
        ...then verify that an error is raised because Type
        must be provided
        """
        self.assertRaises(MissingArgumentError, Atom, lemma=0, start=1, end=2)

    def test_a_category_object_is_initialised(self):
        """
        ...then verify that the id_ field is correctly handled
        """
        category = Category(
            **{
                "frequency": 70.62,
                "hierarchy": ["Sport", "Competition discipline", "Basketball"],
                "id": 20000851,
                "label": "Basketball",
                "namespace": "iptc_en_1.0",
                "positions": [{"end": 139, "start": 136}],
                "score": 4005.0,
                "winner": True,
            }
        )
        self.assertEqual(category.id_, 20000851)
        self.assertEqual(category.namespace, "iptc_en_1.0")
        self.assertEqual(category.label, "Basketball")
        self.assertEqual(
            category.hierarchy,
            ["Sport", "Competition discipline", "Basketball"],
        )
        self.assertEqual(category.frequency, 70.62)
        self.assertEqual(category.score, 4005.0)
        self.assertEqual(category.winner, True)
        self.assertEqual(category.positions[0].start, 136)
        self.assertEqual(category.positions[0].end, 139)
        self.assertTrue(category.winner)

    def test_a_dependency_object_is_initialised(self):
        """
        ...then verify that the id_ field is correctly handled
        """
        dependency = Dependency(id_=0, head=7, label="nmod")
        self.assertEqual(dependency.id_, 0)
        self.assertEqual(dependency.head, 7)
        self.assertEqual(dependency.label, "nmod")

    def test_a_entity_object_is_initialised(self):
        """
        ...then verify that the type_ field is correctly handled
        """
        entity = Entity(
            type_="GEO",
            lemma="Swansea",
            syncon=38324,
            positions=[{"start": 373, "end": 380}],
        )
        self.assertEqual(entity.syncon, 38324)
        self.assertEqual(entity.lemma, "Swansea")
        self.assertEqual(entity.positions[0].start, 373)
        self.assertEqual(entity.positions[0].end, 380)

    def test_a_entity_object_is_initialised_with_relevance(self):
        """
        ...then verify that the type_ field is correctly handled
        """
        entity = Entity(
            type_="GEO",
            lemma="Swansea",
            syncon=38324,
            positions=[{"start": 373, "end": 380}],
            relevance=4
        )
        self.assertEqual(entity.syncon, 38324)
        self.assertEqual(entity.lemma, "Swansea")
        self.assertEqual(entity.positions[0].start, 373)
        self.assertEqual(entity.positions[0].end, 380)
        self.assertEqual(entity.relevance, 4)

    def test_a_entity_object_is_initialized_with_attributes(self):
        """
        ...then verify that the type_ field is correctly handled
        """
        entity = Entity(
            type_="GEO",
            lemma="Swansea",
            syncon=38324,
            positions=[{"start": 373, "end": 380}],
            relevance=4,
            attributes=[
                    {
                        "attribute": "gender",
                        "lemma": "male",
                        "syncon": -1,
                        "type": ""
                    },
                    {
                        "attribute": "role",
                        "lemma": "King",
                        "syncon": 43350,
                        "type": "nph",
                        "attributes": [
                            {
                                "attribute": "placespec",
                                "lemma": "Saudi Arabia",
                                "syncon": 38596,
                                "type": "GEO"
                            }
                        ]
                    }
                ]
        )
        self.assertEqual(entity.syncon, 38324)
        self.assertEqual(entity.lemma, "Swansea")
        self.assertEqual(entity.positions[0].start, 373)
        self.assertEqual(entity.positions[0].end, 380)
        self.assertEqual(entity.relevance, 4)
        self.assertEqual(entity.attributes[0].attribute, "gender")
        self.assertEqual(entity.attributes[1].lemma, "King")
        self.assertEqual(entity.attributes[1].attributes[0].type_, "GEO")

    def test_a_dependency_object_is_initialised_with_an_invalid_position(self):
        """
        ...then EValueError should be raised
        """
        self.assertRaises(
            EValueError,
            Entity,
            syncon=3292812,
            type_="ADR",
            lemma="lemma",
            positions=[{}],
        )

    def test_a_iptc_is_correctly_initialised(self):
        """
        ...then properties should return the expected values
        """
        iptc = Iptc(
            **{
                "description": "IPTC Media Topics",
                "languages": [
                    {"description": "English", "name": "en"},
                    {"description": "German", "name": "de"},
                ],
            }
        )
        self.assertEqual(iptc.description, "IPTC Media Topics")
        self.assertEqual(iptc.languages[1].description, "German")

    def test_a_knowledge_object_is_initialised(self):
        """
        ...then verify that the type_ field is correctly handled
        """
        knowledge = Knowledge(
            **{
                "label": "group.human_group.organization.sport_association",
                "properties": [
                    {
                        "type_": "DBpediaId",
                        "value": "dbpedia.org/page/National_Basketball_Association",
                    },
                    {"type_": "WikiDataId", "value": "Q155223"},
                ],
                "syncon": 206693,
            }
        )
        self.assertEqual(knowledge.syncon, 206693)
        self.assertEqual(
            knowledge.label, "group.human_group.organization.sport_association"
        )
        self.assertEqual(knowledge.properties[1].type_, "WikiDataId")
        self.assertEqual(knowledge.properties[1].value, "Q155223")

    def test_main_lemma_is_correctly_initialised(self):
        """
        ...then properties should return the expected values
        """
        lemma = MainLemma(
            **{
                "value": "locomotive",
                "score": 6.5,
                "positions": [{"start": 1163, "end": 1167}],
            }
        )
        self.assertEqual(lemma.value, "locomotive")
        self.assertEqual(lemma.score, 6.5)
        self.assertEqual(lemma.positions[0].start, 1163)
        self.assertEqual(lemma.positions[0].end, 1167)

    def test_main_phrase_is_correctly_initialised(self):
        """
        ...then properties should return the expected values
        """
        phrase = MainPhrase(
            **{
                "value": "four-cylinder engine",
                "score": 8,
                "positions": [{"start": 883, "end": 903}],
            }
        )
        self.assertEqual(phrase.value, "four-cylinder engine")
        self.assertEqual(phrase.score, 8)
        self.assertEqual(phrase.positions[0].start, 883)
        self.assertEqual(phrase.positions[0].end, 903)

    def test_main_sentence_is_correctly_initialised(self):
        """
        ...then properties should return the expected values
        """
        sentence = MainSentence(
            **{
                "value": "The machine is held...",
                "score": 13.3,
                "start": 740,
                "end": 936,
            }
        )
        self.assertEqual(sentence.start, 740)
        self.assertEqual(sentence.end, 936)
        self.assertEqual(sentence.value, "The machine is held...")
        self.assertEqual(sentence.score, 13.3)

    def test_a_main_syncon_contains_an_invalid_position(self):
        """
        ...then an error should be raised
        """
        self.assertRaises(
            EValueError,
            MainSyncon,
            **{"positions": [{}], "score": 35.59, "syncon": 45740}
        )

    def test_a_main_syncon_is_correctly_initialized_without_lemma(self):
        msyn = MainSyncon(
            **{
                "score": 13.3,
                "syncon": 123456,
                "positions" : [ { "start": 740, "end": 936 } ]
            }
        )
        self.assertEqual(msyn.syncon, 123456)
        self.assertEqual(msyn.score, 13.3)
        self.assertEqual(msyn.lemma, "")

    def test_a_main_syncon_is_correctly_initialized_lemma(self):
        msyn = MainSyncon(
            **{
                "score": 13.3,
                "lemma" : "test",
                "syncon": 123456,
                "positions" : [ { "start": 740, "end": 936 } ]
            }
        )
        self.assertEqual(msyn.syncon, 123456)
        self.assertEqual(msyn.score, 13.3)
        self.assertEqual(msyn.lemma, "test")

    def test_a_phrase_is_initialised(self):
        """
        ...then also nested classes should be correctly initialised
        """
        phrase = Phrase(
            start=30,
            end=100,
            tokens=[
                {
                    "syncon": 62653,
                    "start": 74,
                    "end": 83,
                    "type": "NOU",
                    "lemma": "long time",
                    "pos": "NOUN",
                    "dependency": {"id": 11, "head": 7, "label": "nmod"},
                    "morphology": "Number=Sing",
                    "paragraph": 0,
                    "sentence": 0,
                    "phrase": 4,
                    "atoms": [
                        {
                            "start": 74,
                            "end": 78,
                            "type_": "ADJ",
                            "lemma": "long",
                        },
                        {
                            "start": 79,
                            "end": 83,
                            "type_": "NOU",
                            "lemma": "time",
                        },
                    ],
                }
            ],
            type="NP",
        )
        self.assertEqual(phrase.start, 30)
        self.assertEqual(phrase.end, 100)
        self.assertEqual(phrase.tokens[0].sentence, 0)

    def test_a_property_is_initialised(self):
        """
        ...then verify that the type_ argument is correctly handled
        """
        property_ = Property(type="type", value="value")
        self.assertEqual(property_.type_, "type")
        self.assertEqual(property_.value, "value")

    def test_a_paragraph_is_initilised(self):
        """
        ...then verify that also the position is initialised
        """
        paragraph = Paragraph(**{"sentences": [0, 1], "start": 0, "end": 176})
        self.assertEqual(paragraph.start, 0)
        self.assertEqual(paragraph.end, 176)
        self.assertEqual(paragraph.sentences, [0, 1])

    def test_a_sentence_is_initilised(self):
        """
        ...then verify that also the position is initialised
        """
        sentence = Sentence(**{"phrases": [], "start": 0, "end": 66})
        self.assertEqual(sentence.start, 0)
        self.assertEqual(sentence.end, 66)
        self.assertEqual(sentence.phrases, [])

    def test_a_language_object_is_initilised_by_name(self):
        """
        ...then verify that the proper language description is resolved
        """
        language = Language(name="es")
        self.assertEqual(language.name, "es")

    def test_language_get_language_by_description(self):
        """
        ...then verify that the proper language name is resolved
        """
        language = Language(description="English")
        self.assertEqual(language.description, "English")

    def test_a_standard_is_correctly_initialised(self):
        """
        ...then properties should return the expected values
        """
        standard = Standard(
            **{
                "description": "Standard",
                "languages": [
                    {"description": "English", "name": "en"},
                    {"description": "German", "name": "de"},
                ],
            }
        )
        self.assertEqual(standard.description, "Standard")
        self.assertEqual(
            standard.languages[0].name, "en"
        )

    def test_a_token_is_initialised_with_a_syncon(self):
        """
        ...then verify that all other subclasses are correctly setup
        """
        token = Token(
            **{
                "syncon": 62653,
                "start": 74,
                "end": 83,
                "type": "NOU",
                "lemma": "long time",
                "pos": "PUNCT",
                "dependency": {"id": 11, "head": 7, "label": "nmod"},
                "morphology": "Number=Sing",
                "paragraph": 0,
                "sentence": 0,
                "phrase": 4,
                "atoms": [
                    {"start": 74, "end": 78, "type_": "ADJ", "lemma": "long"},
                    {"start": 79, "end": 83, "type_": "NOU", "lemma": "time"},
                ],
            }
        )

        self.assertEqual(token.start, 74)
        self.assertEqual(token.end, 83)
        self.assertEqual(token.syncon, 62653)
        self.assertEqual(token.lemma, "long time")
        self.assertEqual(token.dependency.head, 7)
        self.assertEqual(token.dependency.label, "nmod")
        self.assertEqual(token.morphology, "Number=Sing")
        self.assertEqual(token.paragraph, 0)
        self.assertEqual(token.sentence, 0)
        self.assertEqual(token.phrase, 4)
        self.assertEqual(token.atoms[1].start, 79)
        self.assertEqual(token.atoms[1].end, 83)
        self.assertEqual(token.atoms[1].type_, "NOU")
        self.assertEqual(token.syncon, 62653)
        self.assertEqual(token.vsyn, None)

    def test_token_with_a_virtual_syncon_but_without_morphology(self):
        """
        ...then verify that a Virtual syncon object is created
        """
        token = Token(
            **{
                "syncon": -1,
                "vsyn": {"id": -436106, "parent": 73303},
                "start": 74,
                "end": 83,
                "type": "NOU",
                "lemma": "long time",
                "pos": "NOUN",
                "dependency": {"id": 11, "head": 7, "label": "nmod"},
                "paragraph": 0,
                "sentence": 0,
                "phrase": 4,
                "atoms": [
                    {"start": 74, "end": 78, "type_": "ADJ", "lemma": "long"},
                    {"start": 79, "end": 83, "type_": "NOU", "lemma": "time"},
                ],
            }
        )

        self.assertEqual(token.start, 74)
        self.assertEqual(token.end, 83)
        self.assertEqual(token.lemma, "long time")
        self.assertEqual(token.dependency.head, 7)
        self.assertEqual(token.dependency.label, "nmod")
        self.assertIsNone(token.morphology)
        self.assertEqual(token.paragraph, 0)
        self.assertEqual(token.sentence, 0)
        self.assertEqual(token.phrase, 4)
        self.assertEqual(token.atoms[1].start, 79)
        self.assertEqual(token.atoms[1].end, 83)
        self.assertEqual(token.atoms[1].type_, "NOU")
        self.assertEqual(token.syncon, -1)
        self.assertEqual(token.vsyn.id_, -436106)
        self.assertEqual(token.vsyn.parent, 73303)

    def test_a_token_is_initialised_with_invalid_values(self):
        """
        ...then verify that an exception is raised
        """
        self.assertRaises(
            ETypeError,
            Token,
            start=1,
            end=21,
            syncon=3234555,
            pos="",
            lemma="lemma",
            dependency=None,
            morphology="morphology",
            paragraph=0,
            sentence=0,
            phrase=4,
            atoms=[],
        )

    def test_a_topic_object_is_correctly_initialised(self):
        """
        ...then verify all properties return the expected value
        """
        topic = Topic(id_=12455, label="label", score=2.3, winner=False)
        self.assertEqual(topic.id_, 12455)
        self.assertEqual(topic.label, "label")
        self.assertEqual(topic.score, 2.3)
        self.assertEqual(topic.winner, False)

    def test_a_vsyncon_is_initialised(self):
        """
        ...then the id_ argument must be specified
        """
        self.assertRaises(MissingArgumentError, VSyncon, parent=0)

    def test_a_contexts_object(self):
        """
        ...then verify that type_ argument is correctly handled
        """
        ctx = Context(**{
                "name": "standard",                    
                "description": "Standard context",
                "languages": [
                    {
                        "analyses": [
                            "disambiguation",
                            "relevants",
                            "entities",
                            "sentiment",
                            "relations"
                        ],
                        "code": "en",
                        "name": "English"
                    },
                    {
                        "analyses": [
                            "disambiguation",
                            "relevants",
                            "entities",
                            "relations"
                        ],
                        "code": "es",
                        "name": "Spanish"
                    },
                    {
                        "analyses": [
                            "disambiguation",
                            "relevants",
                            "entities",
                            "relations"
                        ],
                        "code": "fr",
                        "name": "French"
                    },
                    {
                        "analyses": [
                            "disambiguation",
                            "relevants",
                            "entities",
                            "relations"
                        ],
                        "code": "de",
                        "name": "German"
                    },
                    {
                        "analyses": [
                            "disambiguation",
                            "relevants",
                            "entities",
                            "relations"
                        ],
                        "code": "it",
                        "name": "Italian"
                    }
                ]
            }
        )
        self.assertEqual(ctx.name, "standard")
        self.assertEqual(ctx.description, "Standard context")

    def test_a_taxonomies_object(self):
        """
        ...then verify that type_ argument is correctly handled
        """
        txn = TaxonomyList(**{
                "contract": "https://github.com/therealexpertai/nlapi-openapi-specification/blob/master/geotax.yaml",
                "description": "The geotax document classification resource recognizes geographic places cited in the text and returns corresponding countries' names. In addition, when requested with a specific query-string parameter, it returns extra-data containing equivalent GeoJSON objects. See the specific OpenAPI document (https://github.com/therealexpertai/nlapi-openapi-specification/blob/master/geotax.yaml) for information about the way to obtain and interpret GeoJSON data.",
                "languages": [
                    {
                        "code": "en",
                        "name": "English"
                    },
                    {
                        "code": "es",
                        "name": "Spanish"
                    },
                    {
                        "code": "fr",
                        "name": "French"
                    },
                    {
                        "code": "de",
                        "name": "German"
                    },
                    {
                        "code": "it",
                        "name": "Italian"
                    }
                ],
                "name": "geotax"
            }
        )

        self.assertEqual(txn.name, "geotax")
        self.assertEqual(txn.languages[0].name, "English")
        self.assertEqual(txn.languages[1].code, "es")

    def test_a_taxonomy_object(self):
        """
        ...then verify that type_ argument is correctly handled
        """
        txn = Taxonomy(**{
                "namespace": "iptc_en_1.0",
                "taxonomy": [{
                        "categories": [{
                                "categories": [{
                                        "categories": [{
                                                "id": "20000003",
                                                "label": "Animation"
                                            }, {
                                                "id": "20000004",
                                                "label": "Cartoon"
                                            }, {
                                                "categories": [{
                                                        "id": "20000006",
                                                        "label": "Film festival"
                                                    }
                                                ],
                                                "id": "20000005",
                                                "label": "Cinema"
                                            }, {
                                                "categories": [{
                                                        "id": "20000008",
                                                        "label": "Ballet"
                                                    }, {
                                                        "id": "20000009",
                                                        "label": "Modern dance"
                                                    }, {
                                                        "id": "20000010",
                                                        "label": "Traditional dance"
                                                    }
                                                ],
                                                "id": "20000007",
                                                "label": "Dance"
                                            }
                                        ],
                                        "id": "01000000",
                                        "label": "Arts, culture and entertainment"
                                    }
                                ],
                                "id": "V16000000",
                                "label": "Conflicts, war and peace"
                            }
                        ],
                        "id": "MEDIATOPIC_TAX",
                        "label": "MEDIATOPIC_TAX"
                    }
                ]
            }
        )

        self.assertEqual(txn.namespace, "iptc_en_1.0")
        self.assertEqual(txn.categories[0].id, "MEDIATOPIC_TAX")
        self.assertEqual(txn.categories[0].categories[0].categories[0].categories[1].label, "Cartoon")
