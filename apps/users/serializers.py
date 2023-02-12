from rest_framework import serializers

from .models import User
from apps.companies.models import CompanyRole


class UserBasicCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super(UserBasicCreateSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.is_active = False
        user.company_role = CompanyRole.objects.get(id=CompanyRole.ADMIN)
        user.save()
        # Email must be sent to activate user. 
        return user


class UserInvitedCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super(UserBasicCreateSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.company_role = CompanyRole.objects.get(id=CompanyRole.BASIC)
        user.save()
        return user
