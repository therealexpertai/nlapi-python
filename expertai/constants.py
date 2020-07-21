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

BASE_API_URL = "https://nlapi.expert.ai/v1"

OAUTH2_TOKEN_URL = "https://developer.expert.ai/oauth2/token"

USERNAME_ENV_VARIABLE = "EAI_USERNAME"
PASSWORD_ENV_VARIABLE = "EAI_PASSWORD"
TOKEN_ENV_VARIABLE = "AUTH_TOKEN"

TK_TIMESTAMP_FILENAME = ".timestamp"


# No leading slash
FULL_ANALYSIS_PATH = "analyze/standard/{language}"
SPECIFIC_RESOURCE_ANALYSIS_PATH = "analyze/standard/{language}/{resource}"
IPTC_MEDIA_TOPICS_CLASSIFICATION_PATH = "categorize/iptc/{language}"

CONTEXTS_PATH = "contexts"
CONTEXTS_STANDARD_PATH = "contexts/standard"
TAXONOMIES_LIST_PATH = "taxonomies"
IPTC_TAXONOMIES_PATH = "taxonomies/iptc"


CONTENT_TYPE_HEADER = {"Content-Type": "application/json"}
AUTH_HEADER_KEY = "Authorization"
AUTH_HEADER_VALUE = "Bearer {}"

URLS_AND_METHODS = (
    (FULL_ANALYSIS_PATH, "POST"),
    (SPECIFIC_RESOURCE_ANALYSIS_PATH, "POST"),
    (IPTC_MEDIA_TOPICS_CLASSIFICATION_PATH, "POST"),
    (CONTEXTS_PATH, "GET"),
    (CONTEXTS_STANDARD_PATH, "GET"),
    (TAXONOMIES_LIST_PATH, "GET"),
    (IPTC_TAXONOMIES_PATH, "GET")
)

HTTP_OK = 200
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_INTERNAL_SERVER_ERROR = 500

HTTP_ERRORS = [
    HTTP_UNAUTHORIZED,
    HTTP_FORBIDDEN,
    HTTP_NOT_FOUND,
    HTTP_INTERNAL_SERVER_ERROR,
]


PARAMETER_NAMES = ['language', 'resource']

LANGUAGE_ISO_639_1_CODES = ["de", "en", "es", "fr", "it"]

RESOURCES_NAMES = [
    "disambiguation",
    "relevants",
    "entities"
]
