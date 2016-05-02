from django.core.management.base import BaseCommand, CommandError
from PlaygroundMgmt.models import *
import csv

class Command(BaseCommand):
  help = 'Import CSV from instruments. E.g: Coding challenge provided Stock List'

  def add_arguments(self, parser):
      parser.add_argument('file', nargs='+', type=str)

  def renderInstrument(self, row):
    market_name = row[2] # find the market name
    try:
      _market = Market.objects.get(name = market_name)
    except Market.DoesNotExist: # this market will be created
      _market = Market(name = market_name)
      _market.save()

    asset_type = row[3] # find the asset_type in csv
    try:
      _asset = AssetType.objects.get(name = asset_type)
    except AssetType.DoesNotExist: # this asset type will be created
      _asset = AssetType(name = asset_type)
      _asset.save()

    _ticker = row[0] # ticker
    _name = row[1] # stock name

    ins = Instrument(ticker = _ticker, name = _name, market = _market, asset_type = _asset)
    print('adding: ', ins.name)
    ins.save()

  def handle(self, *args, **options):
    filename = options['file'][0]

    self.stdout.write("Looking to import from: " + filename)
    with open(filename, 'rb') as csvfile:
      rows = csv.reader(csvfile, delimiter=',')
      i = 0
      for row in rows:
        if i > 0:
          self.renderInstrument(row)
        i += 1

      print 'processed ' + str(i) + ' instruments'
  


