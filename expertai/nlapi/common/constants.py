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

BASE_API_URL = "https://nlapi.expert.ai/v2"
BASE_EDGE_URL = "https://edgeapi.expert.ai"

OAUTH2_TOKEN_URL = "https://developer.expert.ai/oauth2/token"

USERNAME_ENV_VARIABLE = "EAI_USERNAME"
PASSWORD_ENV_VARIABLE = "EAI_PASSWORD"
TOKEN_ENV_VARIABLE = "AUTH_TOKEN"
AUTH_HEADER_KEY = "Authorization"
AUTH_HEADER_VALUE = "Bearer {}"

TK_TIMESTAMP_FILENAME = ".timestamp"

# No leading slash
FULL_ANALYSIS_PATH = "analyze/{context}/{language}"
ANALYSIS_PATH = "analyze/{context}/{language}/{resource}"
CLASSIFICATION_PATH = "categorize/{taxonomy}/{language}"
EXECUTION_KEY_PATH = "edge/key/{footprint}"
DETECTION_PATH = "detect/{detector}/{language}"

CONTEXTS_PATH = "contexts"
DETECTORS_PATH = "detectors"
TAXONOMIES_PATH = "taxonomies"
TAXONOMY_PATH = "taxonomies/{taxonomy}/{language}"

CONTENT_TYPE_HEADER = {"Content-Type": "application/json"}

URLS_AND_METHODS = (
    (FULL_ANALYSIS_PATH, "POST"),
    (ANALYSIS_PATH, "POST"),
    (CLASSIFICATION_PATH, "POST"),
    (CONTEXTS_PATH, "GET"),
    (TAXONOMIES_PATH, "GET"),
    (TAXONOMY_PATH, "GET"),
    (EXECUTION_KEY_PATH, "GET"),        
    (DETECTION_PATH, "POST"),
    (DETECTORS_PATH, "GET"),
)

HTTP_GET = "GET"
HTTP_SUCCESSFUL = 200
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_INTERNAL_SERVER_ERROR = 500

# Strings used when print out the status of a EaiResponse
HTTP_ERRORS = {
    HTTP_UNAUTHORIZED: "UNAUTHORIZED",
    HTTP_FORBIDDEN: "FORBIDDEN",
    HTTP_NOT_FOUND: "NOT FOUND",
    HTTP_INTERNAL_SERVER_ERROR: "INTERNAL SERVER ERROR",
}

UNKNOWN = "UNKNOWN_STATUS"
SUCCESSFUL = "SUCCESSFUL"
BAD_REQUEST = "BAD REQUEST"

PARAMETER_NAMES = ["language", "resource", "context", "taxonomy", "footprint","detector"]

LANGUAGES = {
    "de": "German",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "it": "Italian",
}

RESOURCES_NAMES = ["disambiguation", "relevants", "entities", "relations", "sentiment"]

RESPONSE_KEYS_TO_IGNORE = ["language", "version", "content"]
