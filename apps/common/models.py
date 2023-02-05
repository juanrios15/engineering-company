from django.db import models

from .middlewares import GlobalRequestMiddleware
from apps.companies.models import Company
from apps.users.models import User


class BaseManager(models.Manager):
    def get_queryset(self):
        return super(BaseManager, self).get_queryset().filter(active=True)


class BaseModel(models.Model):
    objects = BaseManager()
    original_objects = models.Manager()

    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.audit()
        super(BaseModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.activo = False
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


class BaseMeta:
    ordering = ["-id"]