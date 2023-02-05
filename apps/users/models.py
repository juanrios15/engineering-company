from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.companies.models import Company


class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
