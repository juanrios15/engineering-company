from django.urls import path

from .views import UserBasicCreateView, UserInvitedCreateView, ActivateUserView

app_name = "users"

urlpatterns = [
    path('create_user/', UserBasicCreateView.as_view()),
    path('create_invited_user/', UserInvitedCreateView.as_view()),
    path('activate_user/', ActivateUserView.as_view()),
]