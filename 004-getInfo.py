#!/usr/bin/env python

import os
from bs4 import BeautifulSoup
import sys
import re
import json
import glob
from subprocess import call

import time

DSPACE_BASE="10.1.32.27/dspace/handle/123456789/"

for myfile in glob.iglob(DSPACE_BASE + "*"):
  file_split = myfile.split("/")
  filenam = file_split[-1:][0]
  my_dir = 'DATA/' + '/'.join(file_split[-2:])
  if os.path.exists(my_dir + '/' + filenam +'.json'):
    continue
  if not os.path.exists(os.path.dirname(my_dir)):
    os.makedirs(os.path.dirname(my_dir))
  json_file = my_dir + '/' + filenam + '.json'
  print "processing " + json_file
  soup = BeautifulSoup(open(myfile), 'lxml')
  table = soup.find('table', {'class' : 'itemDisplayTable'});
  meta_s = table.find_all('tr')
  data = {}
  for meta in meta_s:
    label = meta.find('td', {'class' : 'metadataFieldLabel'}).text.encode('utf-8')
    value = meta.find('td', {'class' : 'metadataFieldValue'}).text.encode('utf-8')
    data[re.sub('[^A-Za-z0-9]+', '', label)] = value
  
  data['urlhref'] = []
  for td in soup.find_all('td', {'class' : 'standard'}):
    if (td.find('a') is not None):
      url = td.find('a').get('href').encode('utf-8')
      if url in data['urlhref']:
        continue
      data['urlhref'].append(url)
      pdf = my_dir + url.split("/" + filenam,1)[1] 
      os.system("/bin/bash -c 'curl --progress-bar http://10.1.32.27" + url + " --create-dirs -o " + pdf + "'")
      os.system("/bin/bash -c 'touch " + json_file + "'")
  with open(json_file, 'w') as fp:
    json.dump(data, fp)
  time.sleep(1)
