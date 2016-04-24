from __future__ import unicode_literals

from django.db import models

# Create your models here.
	
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length = 120, blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	
	def __unicode__(self):
		return self.email

class Company(models.Model):
    symbol = models.CharField( max_length=100)
    name = models.CharField(max_length=150)
    market_name = models.CharField( max_length=100, blank=True, null=True)
    asset_class = models.CharField(max_length=100, blank=True, null=True)
    weight = models.IntegerField()

    def __unicode__(self):
		return self.name
    
#This part is also not reusable, need to use yahho finance API to get data and then transfer to database.

class Yahoo(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Amazon(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Facebook(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Twitter(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Apple(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Priceline(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Alphabet(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Regeneron(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Tesla(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Biogen(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Baidu(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class illumina(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Celgene(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Vodafone(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Intel(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Paypal(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Texas(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close

class Ea(models.Model):
	date = models.DateField(blank = True, null = True)
	opent = models.FloatField(blank = True, null = True, default = 0.0)
	high = models.FloatField(blank = True, null = True, default = 0.0)
	low = models.FloatField(blank = True, null = True, default = 0.0)
	close = models.FloatField(blank = True, null = True, default = 0.0)
	volume = models.IntegerField(blank = True, null = True)
	adjclose = models.FloatField(blank = True, null = True, default = 0.0)

	def __unicode__(self):
		return self.close