from django.core.exceptions import ValidationError
from django.conf import settings

from rest_framework import serializers

from . import models
from .utils import get_tokens


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=10, label='confirm password', write_only=True, required=True)
    token = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(max_length=10, label='password', write_only=True, required=True)

    class Meta:
        model = models.User
        fields = [
                  'id',
                  'username',
                  'password',
                  'password2',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'national_code',
                  'token',
                 ]


    def validate(self, data):
        """
        Check that start is before finish.
        """
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise ValidationError('password must match')
        return data


    def create(self, validated_data):
        user = models.User.objects.create(
                                username=validated_data['username'],
                                password=validated_data['password'],
                                first_name=validated_data['first_name'],
                                last_name=validated_data['last_name'],
                                phone_number=validated_data['phone_number'],
                                national_code=validated_data['national_code'],
                                          )
        return user


    def get_token(self, obj):
        user = models.User.objects.get(id=obj.id)
        token = get_tokens(user)
        refresh = token['refresh']
        access = token['access']
        settings.REDIS_JWT_TOKEN.set(name=refresh, value=refresh, ex=settings.REDIS_REFRESH_TIME)
        return {
            "refresh": refresh,
            "access": access
        }


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'password']
