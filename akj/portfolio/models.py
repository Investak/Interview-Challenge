from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text

from django.utils.encoding import python_2_unicode_compatible

from phonenumber_field.modelfields import PhoneNumberField

@python_2_unicode_compatible
class Company(models.Model):
    symbol = models.CharField('Symbol', max_length=125)
    name = models.CharField('Name', max_length=250)
    market_name = models.CharField('Market Name', max_length=40, blank=True, null=True)
    asset_class = models.CharField('Asset class', max_length=40, blank=True, null=True)
    weight = models.PositiveSmallIntegerField('Weight')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.symbol

@python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
    profile_pic = models.ImageField('Profile Pic', upload_to="profile_pic", blank=True, null=True)
    dob = models.DateField('Date Of Birth', blank=True, null=True)
    phone_num = PhoneNumberField("Contact Number", blank=True, null=True)
    address = models.TextField('Address', blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return force_text(self.user.email)


@python_2_unicode_compatible
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=150, blank=True, null=True)
    companies = models.ManyToManyField('Company')

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

    def __str__(self):
        return self.name
