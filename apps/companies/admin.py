from django.contrib import admin
from .models import Company, Currency, CompanyRole


admin.site.register(Company)
admin.site.register(Currency)
admin.site.register(CompanyRole)
