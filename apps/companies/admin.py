from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Company, Currency

admin.site.register(Company, UserAdmin)
admin.site.register(Currency, UserAdmin)