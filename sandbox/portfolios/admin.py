from django.contrib import admin

from .models import Investment, Portfolio, Allocation, HistoricPrice

class AllocationInline(admin.TabularInline):
	model = Allocation
	extra = 1

class InvestmentAdmin(admin.ModelAdmin):
	inlines = (AllocationInline, )

class PortfolioAdmin(admin.ModelAdmin):
	inlines = (AllocationInline,)

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Investment, InvestmentAdmin)
admin.site.register(HistoricPrice)