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

import logging

logger = logging.getLogger(__name__)


class ExpertAiBaseException(Exception):
    def __init__(self, message, **kwargs):
        super().__init__(message, **kwargs)
        if kwargs.get("exception"):
            message += "{}".format(kwargs.get("exception"))
        logger.error(message)


class CredentialsError(ExpertAiBaseException):
    """"""


class ExpertAiRequestError(ExpertAiBaseException):
    """"""


class MissingParametersError(ExpertAiBaseException):
    """"""


class MissingArgumentError(ExpertAiBaseException):
    """"""


class ParameterError(ExpertAiBaseException):
    """"""


class ObjectMapperError(ExpertAiBaseException):
    """"""


class ETypeError(ExpertAiBaseException):
    def __init__(self, expected, current):
        current_type_name = getattr(
            current, "__name__", current.__class__.__name__
        )
        expected_type_name = getattr(
            expected, "__name__", expected.__class__.__name__
        )
        message = "Found {current_type}, expecting {expected_type}".format(
            current_type=current_type_name if current else "NoneType",
            expected_type=expected_type_name if expected else "NoneType",
        )
        super().__init__(message)


class EValueError(ExpertAiBaseException):
    def __init__(self, value, argument):
        message = "Wrong value {current_value}, for {ref_argument}".format(
            current_value=value, ref_argument=argument,
        )
        super().__init__(message)
