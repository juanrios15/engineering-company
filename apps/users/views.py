from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserBasicCreateSerializer, UserInvitedCreateSerializer


class UserBasicCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserBasicCreateSerializer
    permission_classes = [AllowAny]


class UserInvitedCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserInvitedCreateSerializer
    permission_classes = [AllowAny]


class ActivateUserView(APIView):
    def post(self, request, format=None):
        user = request.user
        user.is_active = True
        user.save()

        return Response(status=status.HTTP_202_ACCEPTED)