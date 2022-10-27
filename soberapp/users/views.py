from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
