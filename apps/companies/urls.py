from django.urls import path, include
from rest_framework import routers

from .views import CurrencyViewSet, CompanyCreateView, CompanyViewSet, JoinRequestView, ListJoinRequestView

app_name = "companies"

router = routers.DefaultRouter()

router.register(r"currencies", CurrencyViewSet, basename="currencies")
router.register(r"companies", CompanyViewSet, basename="companies")

urlpatterns = [
    path("", include(router.urls)),
    path('create_company/', CompanyCreateView.as_view()),
    path('join_request/', JoinRequestView.as_view()),
    path('list_requests/', ListJoinRequestView.as_view()),
]