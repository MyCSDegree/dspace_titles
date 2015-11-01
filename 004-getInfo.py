import os
from bs4 import BeautifulSoup
import sys
import re
import json

json_file = 'JSON/' + sys.argv[1] + '.json'

if os.path.exists(os.path.dirname(json_file)):
  quit()

print "processing " + sys.argv[1] + '.json'
soup = BeautifulSoup(open(sys.argv[1]), 'lxml')

table = soup.find('table', {'class' : 'itemDisplayTable'});

meta_s = table.find_all('tr')

data = {}

for meta in meta_s:
  label = meta.find('td', {'class' : 'metadataFieldLabel'}).text.encode('utf-8')
  value = meta.find('td', {'class' : 'metadataFieldValue'}).text.encode('utf-8')
  data[re.sub('[^A-Za-z0-9]+', '', label)] = value

data['urlhref'] = soup.find('td', {'class' : 'standard'}).find('a').get('href').encode('utf-8')


if not os.path.exists(os.path.dirname(json_file)):
  os.makedirs(os.path.dirname(json_file))

with open(json_file, 'w') as fp:
  json.dump(data, fp)
