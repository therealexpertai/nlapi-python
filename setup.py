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

from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="expertai-nlapi",
    version="2.2.0",
    author="Expert System S.p.A.",
    author_email="api.support@expert.ai",
    description="Python client for expert.ai Natural Language API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/therealexpertai/nlapi-python",
    #packages=find_namespace_packages(include=['expertai.nlapi']),
    packages=find_namespace_packages(include=['expertai.nlapi.*']),
    install_requires=["requests"],
    classifiers=[
		'Development Status :: 5 - Production/Stable',        
        #"Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
		'Topic :: Text Processing :: Linguistic',
		'Intended Audience :: Developers',		
		'Intended Audience :: Science/Research',				
		'Intended Audience :: Education',        
    ],
    python_requires=">=3.7",
)
