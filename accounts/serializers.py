from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, Serializer


class UserCreateSerializer(ModelSerializer):
    """ A serializer class for creating User model """

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'is_active', 'is_superuser')


class UserSerializer(ModelSerializer):
    """ A serializer class for the User model """

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'is_active', 'is_superuser')
