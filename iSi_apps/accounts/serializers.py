from rest_framework import serializers
from iSi_apps.accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        exclude = ('last_login', 'is_superuser', 'is_staff', 'groups', 'user_permissions')

        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True, 'write_only': True},

        }

    def create(self, validated_data):
        instance = super(CustomUserSerializer, self).create(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
