from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny

from .serializers import CompanySerializer, CompanyReadSerializer, CurrencySerializer, JoinRequestSerializer
from .models import Company, Currency, JoinRequest


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyReadSerializer
    permission_classes = [AllowAny]


class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]


class JoinRequestView(generics.CreateAPIView):
    queryset = JoinRequest.objects.all()
    serializer_class = JoinRequestSerializer
    permission_classes = [AllowAny]


class ListJoinRequestView(generics.ListAPIView):
    queryset = JoinRequest.objects.all()
    serializer_class = JoinRequestSerializer

    def get_queryset(self):
        user = self.request.user
        return JoinRequest.objects.filter(company=user.company)
