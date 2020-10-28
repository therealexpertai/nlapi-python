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

import os
from unittest import TestCase
from unittest.mock import MagicMock, patch

import requests

from nlapi.v1 import constants


class BaseTestCase(TestCase):
    """"""


class ExpertAiTestCase(BaseTestCase):
    def setUp(self):
        requests_post_patched = patch.object(requests, "post")
        self.patched_post = requests_post_patched.start()

        requests_get_patched = patch.object(requests, "get")
        self.patched_get = requests_get_patched.start()

        self.endpoint_path = "language/resource"

        response = MagicMock(text="")
        self.patched_post.return_value = response

        environment_variables_patch = patch.dict(
            os.environ,
            {
                constants.USERNAME_ENV_VARIABLE: "user@eai",
                constants.PASSWORD_ENV_VARIABLE: "pw",
            },
        )
        environment_variables_patch.start()

        self.addCleanup(requests_get_patched.stop)
        self.addCleanup(requests_post_patched.stop)
        self.addCleanup(environment_variables_patch.stop)
        super().setUp()
