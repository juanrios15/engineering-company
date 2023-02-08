from django.db import models


class CompanyRole(models.Model):
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


class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return str(self.name)
