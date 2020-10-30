# Copyright (c) 2020 original authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an \"AS IS\" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest.mock import patch

from expertai.nlapi.v1.errors import ParameterError
from expertai.nlapi.v1.validate import ExpertAiValidation
from tests import BaseTestCase


class ValidationTests(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.validation_klass = ExpertAiValidation()

    def test_the_language_code_is_not_among_those_permitted(self):
        """
        ...then the value should not be considered correct
        """
        self.assertFalse(
            self.validation_klass.language_value_is_correct(language="sv")
        )

    def test_the_resource_is_not_among_those_permitted(self):
        """
        ...then the value should not be considered correct
        """
        self.assertFalse(
            self.validation_klass.resource_value_is_correct(
                resource="document"
            )
        )

    @patch("expertai.nlapi.v1.validate.ExpertAiValidation.language_value_is_correct")
    def test_the_parameter_to_be_validated_is_the_language(
        self, patched_method
    ):
        """
        ...then verify language_value_is_correct() is called
        """
        self.validation_klass.check_value(param_name="language", value="it")
        patched_method.assert_called_once_with(language="it")

    @patch("expertai.nlapi.v1.validate.ExpertAiValidation.resource_value_is_correct")
    def test_the_parameter_to_be_validated_is_the_resource(
        self, patched_method
    ):
        """
        ...then verify resource_value_is_correct() is called
        """
        self.validation_klass.check_value(
            param_name="resource", value="disambiguation"
        )
        patched_method.assert_called_once_with(resource="disambiguation")

    def test_parameter_name_is_wrong(self):
        """
        ...then the validation should fail immediately
        """
        self.assertRaises(
            ParameterError, self.validation_klass.check_name, param_name="lang"
        )

    def test_when_parameter_name_is_correct_but_the_value_is_wrong(self):
        """
        ...then the validation should still fail

        This test implicitly verifies that the two check_name and check_value
        methods are sequentially invoked
        """
        self.assertRaises(
            ParameterError,
            self.validation_klass.check_value,
            param_name="language",
            value="sv",
        )
