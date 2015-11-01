

import os
from bs4 import BeautifulSoup

if os.path.exists('records.txt'):
  os.remove('records.txt');

for filename in sorted(os.listdir(os.getcwd() + "/PRE_DATA/")):
  print "processing " + filename
  soup = BeautifulSoup(open("PRE_DATA/" + filename))
  for table in soup.find_all('table', {'class' : 'miscTable'}):
    data = table.find_all('tr')
  separator = "|||"
  for record in data:
    rows = record.find_all('td')
    if (len(rows) == 3):
      if (rows[1].find('a') is not None): #if url exists?
        issue_date = rows[0].find('strong').text.encode('utf-8')
        title      = rows[1].find('a').text.encode('utf-8')
        url        = rows[1].find('a').get('href').encode('utf-8')
        author     = rows[2].text.encode('utf-8')
        to_write   = issue_date + separator + title + separator + author + separator + url
        with open('records.txt', 'a') as the_file:
          the_file.write(to_write + "\n")
