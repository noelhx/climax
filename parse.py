#!/usr/bin/python

import requests
from collections import Counter


req = requests.get('http://www.wrh.noaa.gov/pqr/climate/PDXtemp.txt')
#print req.content

print "year, days over 65, days over 70, days over 75, notes"

warm_years = 0

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

  over65 = sum(int(x) >= 65 for x in row)
  over70 = sum(int(x) >= 70 for x in row)
  over75 = sum(int(x) >= 75 for x in row)
  print "%s, %s, %s, %s," % (year, over65, over70, over75)

  if over65 >= 7 and over75 >= 2: warm_years += 1

print "\n,,,,warm years: %g" % warm_years
print ",,,,(where warm year = a week above 65 and at least two days above 75)"
