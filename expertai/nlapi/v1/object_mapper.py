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

from re import search as re_search

from expertai.nlapi.v1.errors import ObjectMapperError
from expertai.nlapi.v1.model import DataModel


class ObjectMapper:
    def to_snake_case(self, s):
        m = re_search(r"[A-Z]", s)
        while m:
            from_, to_ = m.start(), m.end()
            s = s[:from_] + "_" + s[from_:to_].lower() + s[to_:]
            m = re_search(r"[A-Z]", s)
        return s.strip("_")

    def precheck_references(self, json, refs_name, elems_name):
        """Verify that the ref contained inside the references array
        points to an existing element inside the elements array.
        Somehow this check prevents that an IndexError exception is
        raised when we resolving the reference at the next phase
        """
        references = json.get(refs_name, [])
        elements = json.get(elems_name, [])

        try:
            [
                [elements[el] for el in ref.get(elems_name, [])]
                for ref in references
            ]
        except IndexError as e:
            raise ObjectMapperError(
                "{exc} with refs_name/elems_name: {refs_name}/{elems_name}".format(
                    exc=e, refs_name=refs_name, elems_name=elems_name
                )
            )

    def resolve_references(self, json, refs_name, elems_name):
        """Resolve the references with the constituent elements.

        Each object of the refs_name stored in the json contains an array named
        `elems_name` which stores the index of the concrete objects contained in
        the json[elems_name] array

        This resolution is placed here because my intention was not to store any
        logic inside the data-model classes. And it needed to be performed ahead
        of the DataModel initialisation because that every nested class is
        recursively initialised.
        """
        references = json.get(refs_name, [])
        elements = json.get(elems_name, [])
        new_json = json.copy()
        self.precheck_references(json, refs_name, elems_name)
        if not references:
            return new_json

        for i, ref in enumerate(json[refs_name]):
            if elements:
                new_json[refs_name][i][elems_name] = [
                    elements[i] for i in ref[elems_name]
                ]
            else:
                new_json[refs_name][i][elems_name] = []

        return new_json

    def convert_json_keys(self, json):
        """Convert each key of json to Python's case formatting style."""
        djson = {}
        for k, v in json.items():
            djson[self.to_snake_case(k)] = v
        return djson

    def read_json(self, response_json):
        """Process and digest the json body of the response.

        Before initialising the root modeling class, performs some
        preliminary actions.
        """
        if "taxonomies" in response_json:
            data = response_json.get("taxonomies")
        elif "contexts" in response_json:
            data = response_json.get("contexts")
        else:
            response_data = response_json.get("data")
            cdata = self.convert_json_keys(response_data)
            rdata = self.resolve_references(cdata, "phrases", "tokens")
            data = self.resolve_references(rdata, "sentences", "phrases")

        try:
            dm = DataModel(**data)
        except TypeError as e:
            raise ObjectMapperError(e)
        return dm
