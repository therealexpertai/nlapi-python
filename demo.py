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
import os
from getpass import getpass
from pprint import pprint

from lib import constants
from lib.errors import ExpertBaseException
from lib.expert import ExpertClient


def show(end_point_method, **kwargs):
   try:
      response = end_point_method(**kwargs)
   except ExpertBaseException as e:
      logging.error(e)
      return
   else:
      if response.successful:
         pprint(response.json)
      else:
         import pdb;pdb.set_trace()
         print("Error")
         return {}

def demo_setup():
   username = os.getenv(constants.USERNAME_ENV_VARIABLE)
   if not username:
      username = input("Enter your Expert-AI username: \t")
      os.environ[constants.USERNAME_ENV_VARIABLE] = username
   
   password = os.getenv(constants.PASSWORD_ENV_VARIABLE)
   if not password:
      password = getpass(prompt="Enter your Expert-AI password: \t")
      os.environ[constants.PASSWORD_ENV_VARIABLE] = password
      

def demo():
   demo_setup()
   client = ExpertClient()
   text = "Facebook is looking at buying U.S. startup for $6 million"
   language = "en"

   print("======= CONTEXTS  =======")
   show(client.contexts)

   print('', end='\n\n')
   print("======= FULL_ANALYSIS  =======")
   show(
      client.full_analysis,
      body={"document": {"text": text}},
      params={'language': language}
   )

   print('', end='\n\n')
   print("======= SPECIFIC_RESOURCE_ANALYSIS  =======")
   show(
      client.specific_resource_analysis,
      body={"document": {"text": text}},
      params={'language': language, 'resource': 'entities'}
   )

   print('', end='\n\n')
   print("======= AVAILABLE TAXONOMIES  =======")
   show(client.iptc_taxonomies_list)
   
   print('', end='\n\n')
   print("======= IPTC_MEDIA_TOPICS_CLASSIFICATION  =======")
   show(
      client.iptc_media_topics_classification,
      body={"document": {"text": text}},
      params={'language': language}
   )




if __name__ == "__main__":
   demo()
