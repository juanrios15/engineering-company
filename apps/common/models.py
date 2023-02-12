from django.db import models

from .middlewares import GlobalRequestMiddleware
from apps.companies.models import Company
from apps.users.models import User


class BaseModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="created_by", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="updated_by", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.audit()
        super(BaseModel, self).save(*args, **kwargs)

    def audit(self):
        request = GlobalRequestMiddleware.get_request()

        if request and request.user:
            user = request.user
            if self.pk:
                self.updated_by = user
            else:
                self.created_by = user
                self.company = user.company
