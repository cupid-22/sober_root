from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializer import UserSerializer, AppUserLoginSerializer


class SobrietyDateViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserLoginViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    model = User
    queryset = User.objects.exclude(social_type=User.SocialLoginOption.ADMIN)
    serializer_class = AppUserLoginSerializer
    permission_classes = []
