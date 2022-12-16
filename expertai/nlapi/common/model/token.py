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

from expertai.nlapi.common.errors import ETypeError, EValueError
from expertai.nlapi.common.model.atom import Atom
from expertai.nlapi.common.model.dependency import Dependency
from expertai.nlapi.common.model.position import Position
from expertai.nlapi.common.model.vsyncon import VSyncon


class Token(Position):
    def __init__(
        self,
        start,
        end,
        syncon,
        pos,
        lemma,
        paragraph,
        sentence,
        phrase,
        dependency=None,
        atoms=[],
        morphology=None,
        vsyn=None,
        type=None,
        type_=None,
        **kwargs
    ):
        """Initialise the Property object

        To minimise the `abuse` of the Python `type` keyword, the
        initialisation method also accepts `type_`. The former argument
        is used when the initialisation is nested inside other
        data-model classes. In these cases the __init__ receives a
        dictionary containing `type` not `type_`, because that how the
        response the server sends is defined. Otherwise when the object
        can be directly initialised using the second alternative.

        Again, to mitigate this name clash with the reserved keyword
        the property was suffixed with the underscore.
        """
        super().__init__(start=start, end=end)
        self._syncon = syncon
        # by default if only one value is passed, it is considered
        # to be the key
        self._pos = pos
        self._lemma = lemma
        self._atoms = []
        self._vsyn = None

        self._dependency = None
        if dependency:
            self._dependency = Dependency(**dependency)

        self._morphology = morphology
        self._paragraph = paragraph
        self._sentence = sentence
        self._phrase = phrase
        self._type = type or type_

        if not isinstance(atoms, list):
            raise ETypeError(list, atoms)

        for atom in atoms:
            if not isinstance(atom, dict):
                raise ETypeError(dict, atom)
            if not atom:
                raise EValueError(atom, "Token.atom")

            self._atoms.append(Atom(**atom))

        if vsyn:
            if not isinstance(vsyn, dict):
                raise ETypeError(dict, vsyn)

            self._vsyn = VSyncon(**vsyn)

    @property
    def syncon(self):
        return self._syncon

    @property
    def pos(self):
        return self._pos

    @property
    def lemma(self):
        return self._lemma

    @property
    def dependency(self):
        return self._dependency

    @property
    def morphology(self):
        return self._morphology

    @property
    def paragraph(self):
        return self._paragraph

    @property
    def sentence(self):
        return self._sentence

    @property
    def phrase(self):
        return self._phrase

    @property
    def atoms(self):
        return self._atoms

    @property
    def vsyn(self):
        return self._vsyn

    @property
    def type_(self):
        return self._type

    def __str__(self):
        return "{},{},{}".format(self.start, self.end, self.lemma)
