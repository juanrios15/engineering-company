from django.urls import path

from .views import UserCreateView

app_name = "users"

urlpatterns = [
    path('create_user/', UserCreateView.as_view()),
]