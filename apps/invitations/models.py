from django.db import models

from apps.common.models import BaseModel


class Invitation(BaseModel):
    invited_email = models.EmailField(max_length=254)

    def __str__(self):
        return str(self.invited_email)
