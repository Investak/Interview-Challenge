from __future__ import unicode_literals

from django.db import models
from simple_history.models import HistoricalRecords

ASSET_CLASSES = (
	('stock', 'Stock'), ('index', 'Index'), (None, '')
)
class  Investment(models.Model):
	symbol = models.CharField(max_length=5)
	name = models.CharField(max_length=50)
	market = models.CharField(max_length=50, blank=True)
	asset_class = models.CharField(max_length=10, blank=True, choices=ASSET_CLASSES)

	def __str__(self):
		return self.name

class Portfolio(models.Model):
	name = models.CharField(max_length=100)
	investments = models.ManyToManyField(Investment, through="Allocation")
	history = HistoricalRecords()

	def __str__(self):
		return self.name

class Allocation(models.Model):
	investment = models.ForeignKey(Investment)
	portfolio = models.ForeignKey(Portfolio)
	weight = models.DecimalField(max_digits=5, decimal_places=2)
	history = HistoricalRecords()

	def __str__(self):
		return "%s with %s%% in %s" % (self.portfolio.name, self.weight, self.investment.name)

class HistoricPrice(models.Model):
	date = models.DateField()
	open = models.FloatField()
	high = models.FloatField()
	low = models.FloatField()
	close = models.FloatField()
	adjusted_close = models.FloatField()
	volume = models.PositiveIntegerField()
	investment = models.ForeignKey(Investment)

	def __str__(self):
		return "%s closed:%s" % (self.date, self.close)