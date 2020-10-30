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

from expertai.nlapi.v1.errors import EValueError

ENTITY_TYPE_VALUES = {
    "ADR": "Street address",
    "ANM": "Animals",
    "BLD": "Building",
    "COM": "Businesses / companies",
    "DAT": "Date",
    "DEV": "Device",
    "DOC": "RequestDocument",
    "EVN": "Event",
    "FDD": "Food/beverage",
    "GEA": "Physical geographic features",
    "GEO": "Administrative geographic areas",
    "GEX": "Extended geography",
    "HOU": "Hours",
    "LEN": "Legal entities",
    "MAI": "Email address",
    "MEA": "Measure",
    "MMD": "Mass media",
    "MON": "Money",
    "NPH": "Humans",
    "ORG": "Organizations / societies / institutions",
    "PCT": "Percentage",
    "PHO": "Phone number",
    "PPH": "Physical phenomena",
    "PRD": "Product",
    "VCL": "Vehicle",
    "WEB": "Web address",
    "WRK": "Work of human intelligence",
    "NPR": "Proper noun",
}


class EntityType:
    def __init__(self, key):
        if key not in ENTITY_TYPE_VALUES:
            raise EValueError(key, "Entity.key")

        self._key = key

    @property
    def key(self):
        return self._key

    @property
    def description(self):
        return ENTITY_TYPE_VALUES.get(self._key)
