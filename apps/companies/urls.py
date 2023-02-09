from django.urls import path, include
from rest_framework import routers

from .views import CurrencyViewSet, CompanyCreateView

app_name = "companies"

router = routers.DefaultRouter()

router.register(r"currencies", CurrencyViewSet, basename="currencies")

urlpatterns = [
    path("", include(router.urls)),
    path('create_company/', CompanyCreateView.as_view()),
]