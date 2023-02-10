from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny

from .serializers import CompanySerializer, CurrencySerializer
from .models import Company, Currency


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]
