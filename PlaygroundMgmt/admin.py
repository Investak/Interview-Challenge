from django.contrib import admin

from .models import *

admin.site.register(Instrument)
admin.site.register(Market)
admin.site.register(AssetType)
admin.site.register(Portfolio)
admin.site.register(Investment)
