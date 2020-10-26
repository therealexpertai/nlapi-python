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

TOKEN_TYPE_VALUES = {
    "ADJ": "Adjective",
    "ADV": "Adverb",
    "ART": "Article",
    "AUX": "Auxiliary verb",
    "CON": "Conjunction",
    "NOU": "Noun",
    "NOU_ADR": "Street address",
    "NOU_DAT": "Date",
    "NOU_HOU": "Hour",
    "NOU_MAI": "Email address",
    "NOU_MEA": "Measure",
    "NOU_MON": "Money",
    "NOU_PCT": "Percentage",
    "NOU_PHO": "Phone number",
    "NOU_WEB": "Web address",
    "NPR": "Proper noun",
    "NPR_ANM": "Proper noun of an animal",
    "NPR_BLD": "Proper noun of a building",
    "NPR_COM": "Proper noun of a business/company",
    "NPR_DEV": "Proper noun of a device",
    "NPR_DOC": "Proper noun of a document",
    "NPR_EVN": "Proper noun of an event",
    "NPR_FDD": "Proper noun of a food/beverage",
    "NPR_GEA": "Proper noun of a physical geographic feature",
    "NPR_GEO": "Proper noun of an administrative geographic area",
    "NPR_GEX": "Proper noun of an extra-terrestrial or imaginary place",
    "NPR_LEN": "Proper noun of a legal/fiscal entity",
    "NPR_MMD": "Proper noun of a mass media",
    "NPR_NPH": "Proper noun of a human being",
    "NPR_ORG": "Proper noun of an organization/society/institution",
    "NPR_PPH": "Proper noun of a physical phenomena",
    "NPR_PRD": "Proper noun of a product",
    "NPR_VCL": "Proper noun of a vehicle",
    "NPR_WRK": "Proper noun of a work of human intelligence",
    "PNT": "Punctuation mark",
    "PRE": "Preposition",
    "PRO": "Pronoun",
    "PRT": "Particle",
    "VER": "Verb",
    "ANY": "Any entity type",
}


class TokenType:
    def __init__(self, key="", description=""):
        self._key = key
        self._description = description

    @property
    def key_from_description(self):
        return dict((v, k) for k, v in TOKEN_TYPE_VALUES.items()).get(
            self._description
        )

    @property
    def key(self):
        return self._key

    @property
    def description(self):
        return TOKEN_TYPE_VALUES.get(self._key)
