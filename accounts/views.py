from rest_framework import permissions
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework_jwt.serializers import User

from accounts.serializers import UserSerializer, UserCreateSerializer


class UserList(ListAPIView):
    """ View to list all users"""
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


@authentication_classes([])
@permission_classes([])
class UserCreate(CreateAPIView):
    """ View to create a new user. Only accepts POST requests """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        # TODO: should be changed to activating by email activation link
        instance.is_active = True
        instance.save()


class UserRetrieveUpdate(RetrieveUpdateAPIView):
    """ Retrieve a user or update user information.
    Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
