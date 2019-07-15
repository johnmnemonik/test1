from django.contrib import admin

from sale.models import Selling

class AdminSelling(admin.ModelAdmin):
	list_display = ('description', 'netto', 'delivery_country', 'vat_rate', 'vat_sum')


admin.site.register(Selling, AdminSelling)
