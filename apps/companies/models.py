import os

from django.db import models


class CompanyRole(models.Model):
    ADMIN = 1
    EDITOR = 2
    BASIC = 3
    role = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Company Roles"

    def __str__(self):
        return str(self.role)


class Currency(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = "Currencies"

    def __str__(self):
        return str(self.name)


def content_file_name(instance, filename):
    return os.path.join("logos", filename)


class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = models.FileField(upload_to=content_file_name, null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return str(self.name)


class JoinRequest(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
