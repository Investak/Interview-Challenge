#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "akj.settings")

    from django.core.wsgi import get_wsgi_application

    application = get_wsgi_application()


import csv
from random import randint

import django
from django.core.files import File

from portfolio.models import *

dataFile = open('company.csv')
dataFileReader = csv.reader(dataFile)
data = list(dataFileReader)

l = len(data)

print('-' * 25, 'Products', '-' * 25)
print()

for i in range(7527, l):
    symbol = data[i][0]
    name = data[i][1]
    market_name = data[i][2]
    asset_class = data[i][3]
    weight = randint(1, 10)

    print(i, '\t', symbol, '\t', name)


    companyObj = Company()
    companyObj.symbol = symbol
    companyObj.name = name
    companyObj.market_name = market_name
    companyObj.asset_class = asset_class
    companyObj.weight = weight

    companyObj.save()
