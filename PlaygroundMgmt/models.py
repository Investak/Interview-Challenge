from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Types of assets 
class AssetType(models.Model):
  name = models.CharField(max_length = 200)

  def __str__(self):
    return self.name

# Types of Markets
class Market(models.Model):
  name = models.CharField(max_length = 200)
  
  def __str__(self):
    return self.name

# Basic instrument model
class Instrument(models.Model):
  ticker = models.CharField(max_length = 200)
  name = models.CharField(max_length = 200)
  market = models.ForeignKey(Market)
  asset_type = models.ForeignKey(AssetType)

  def __str__(self):
    return self.name  

# Portfolio, linked to a User
class Portfolio(models.Model):
  user = models.ForeignKey(User)
  name = models.CharField(max_length = 200)
  instruments = models.ManyToManyField(Instrument, through = 'Investment')

  def __str__(self):
    return self.name

  class Meta:
  	ordering = ['id']

# Investments are the set of instruments an investor
# places in his portfolio
class Investment(models.Model):
  portfolio = models.ForeignKey(Portfolio, on_delete = models.CASCADE)
  instrument = models.ForeignKey(Instrument, on_delete = models.CASCADE)
  size = models.DecimalField(max_digits = 3, decimal_places = 2)

  def __str__(self):
    return self.portfolio.user.username + ' [id:' + str(self.portfolio.user.id) + ']' + \
      ' > ' + self.portfolio.name + ' [id:' + str(self.portfolio.id) + ']' + ' > ' + \
      self.instrument.name + ' [id:' + str(self.instrument.id) + ']'