from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from apps.companies.models import Company, CompanyRole


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    company_role = models.ForeignKey(CompanyRole, on_delete=models.PROTECT, default=3)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
