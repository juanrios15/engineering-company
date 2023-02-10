from rest_framework import viewsets

from .serializers import InvitationSerializer
from .models import Invitation


class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
