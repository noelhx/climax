#!/usr/bin/python

import requests
from collections import Counter


req = requests.get('http://www.wrh.noaa.gov/pqr/climate/PDXtemp.txt')
#print req.content

print "year, days over 65, days over 70"

for line in req.content.splitlines():
  year = str(line[:4])
  if not year.isdigit(): continue
  year = int(year)
  if year < 1942: continue

  month = int(line[4:6])
  if month != 10: continue

  maxmin = line[6:8]
  if maxmin == 'TN': continue

  row = line[10:].split()

  #print "%s-%s xx %s" % (year, month, len(row))

  print "%s, %s, %s" % (year, sum(int(x) >= 65 for x in row), sum(int(x) >= 70 for x in row))

