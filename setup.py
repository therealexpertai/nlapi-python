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

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="expertai-nlapi",
    version="1.2.4",
    author="Expert System S.p.A.",
    author_email="api.support@expert.ai",
    description="Python client for expert.ai Natural Language API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/therealexpertai/nlapi-python",
    packages=["expertai", "expertai.model"],
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
