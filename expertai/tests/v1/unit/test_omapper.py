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

from unittest.mock import patch

from nlapi.v1.errors import ObjectMapperError
from nlapi.v1.object_mapper import ObjectMapper
from tests import BaseTestCase


class ObjectMapperTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.omapper = ObjectMapper()

    def test_the_snake_case_method_is_called_on_a_camelcase_string(self):
        """
        ...then it should split words with _ and the string should
        be all lower case
        """
        self.assertEqual(self.omapper.to_snake_case("mainLemma"), "main_lemma")
        self.assertEqual(self.omapper.to_snake_case("aBcDe"), "a_bc_de")
        self.assertEqual(
            self.omapper.to_snake_case("main_lemma"), "main_lemma"
        )

    def test_convert_json_keys_is_called(self):
        """
        ...then all keys should be converted to snake case if they need to
        """
        djson = self.omapper.convert_json_keys(
            {"mainLemma": [], "mainSentences": [], "mainPhrases": []}
        )
        expected_json = {
            "main_lemma": [],
            "main_sentences": [],
            "main_phrases": [],
        }
        self.assertEqual(djson, expected_json)

    @patch("nlapi.v1.object_mapper.DataModel")
    def test_response_json_is_read(self, mocked_class):
        """
        ...then verify that DataModel class is called
        """
        self.omapper.read_json(
            {
                "data": {
                    "mainSentences": [
                        {
                            "value": "The machine",
                            "score": 13.3,
                            "start": 740,
                            "end": 936,
                        },
                        {
                            "value": "The machine",
                            "score": 13.3,
                            "start": 70,
                            "end": 93,
                        },
                    ]
                }
            }
        )
        self.assertEqual(mocked_class.call_count, 1)

    def test_there_invalid_data_model_references(self):
        """
        ...then check that the proper exception is raised

        These are kind of edge cases that should not happen
        """
        self.assertRaises(
            ObjectMapperError,
            self.omapper.precheck_references,
            {"tokens": [], "phrases": [{"tokens": [1]}]},
            "phrases",
            "tokens",
        )
        self.assertRaises(
            ObjectMapperError,
            self.omapper.precheck_references,
            {"phrases": [{"tokens": [1]}]},
            "phrases",
            "tokens",
        )

    @patch("nlapi.v1.object_mapper.ObjectMapper.precheck_references")
    def test_references_are_resolved_into_objects(
        self, patched_precheck_references
    ):
        """
        ...then verify that the precheck_references method is called
        """
        self.omapper.resolve_references(
            {"main_sentences": []}, "phrases", "tokens"
        )
        self.assertEqual(patched_precheck_references.call_count, 1)

    def test_the_response_does_not_contain_refs_and_elem_array(self):
        """
        ...then an error should be raised
        """
        self.assertEqual(
            self.omapper.resolve_references(
                {"main_sentences": []}, "phrases", "tokens"
            ),
            {"main_sentences": []},
        )

    def test_the_response_contains_only_an_empty_ref_array(self):
        """
        ...then it should raise and error because the elements array
        does not exists
        """
        self.assertEqual(
            self.omapper.resolve_references(
                {"sentences": [], "phrases": []}, "sentences", "phrases"
            ),
            {"sentences": [], "phrases": []},
        )

    def test_token_references_are_resolved_to_phrases(self):
        """
        ...then verify that the values are one expected
        """
        tokens_list = [
            {
                "syncon": 62653,
                "start": 74,
                "end": 83,
                "type": "NOU",
                "pos": "NOUN",
            },
            {
                "syncon": 33653,
                "start": 33,
                "end": 44,
                "type": "DET",
                "pos": "DETERMINER",
            },
        ]
        sample_response = {
            "tokens": tokens_list,
            "phrases": [{"tokens": [1]}, {"tokens": [0, 1]}],
        }
        self.assertEqual(
            self.omapper.resolve_references(
                sample_response, "phrases", "tokens"
            ),
            {
                "tokens": tokens_list,
                "phrases": [
                    {"tokens": [tokens_list[1]]},
                    {"tokens": tokens_list},
                ],
            },
        )

    def test_sentences_references_are_resolved_to_phrases(self):
        """
        ...then verify that the values are one expected
        """
        phrases_list = [
            {"tokens": [3, 4, 9], "type": "PP", "start": 54, "end": 65},
            {"tokens": [3, 4, 9], "type": "PP", "start": 54, "end": 65},
        ]

        sample_response = {
            "phrases": phrases_list,
            "sentences": [{"phrases": [1], "start": 0, "end": 66}],
        }
        self.assertEqual(
            self.omapper.resolve_references(
                sample_response, "sentences", "phrases"
            ),
            {
                "phrases": phrases_list,
                "sentences": [
                    {"phrases": [phrases_list[1]], "start": 0, "end": 66}
                ],
            },
        )

    def test_the_response_contains_a_key_that_does_not_map_to_any_data_model(
        self,
    ):
        """
        ...then an error should be raised before the DataModel class
        is initialised because the json is directly mapped to the arguments of
        the __init__ method
        """
        self.assertRaises(
            ObjectMapperError,
            self.omapper.read_json,
            {"data": {"mainToken": []}},
        )
