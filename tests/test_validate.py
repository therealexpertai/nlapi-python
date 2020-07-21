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

from expertai.validate import ExpertAiValidation
from expertai.errors import ParameterError
from tests import BaseTestCase


class ValidationTests(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.validation_klass = ExpertAiValidation()
    
    def test_invalid_language_choice(self):
        self.assertFalse(
            self.validation_klass.language_value_is_correct(language='sv')
        )

    def test_invalid_resource(self):
        self.assertFalse(
            self.validation_klass.resource_value_is_correct(resource='document')
        )

    @patch('expertai.validate.ExpertAiValidation.language_value_is_correct')
    def test_the_language_method_is_called(self, patched_method):
        self.validation_klass.check_value(param_name='language', value='it')
        patched_method.assert_called_once_with(
            language='it'
        )

    @patch('expertai.validate.ExpertAiValidation.resource_value_is_correct')
    def test_the_resource_method_is_called(self, patched_method):
        self.validation_klass.check_value(
            param_name='resource', value='disambiguation'
        )
        patched_method.assert_called_once_with(
            resource='disambiguation'
        )

    def test_check_wrong_value(self):
        self.assertRaises(
            ParameterError,
            self.validation_klass.check_name,
            param_name="lang"
        )

    def test_check_wrong_value(self):
        self.assertRaises(
            ParameterError,
            self.validation_klass.check_value,
            param_name="language",
            value='sv'
        )

       
        
        
	

