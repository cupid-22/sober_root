from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User
from users.serializer import UserSobrietySerializer, AppUserLoginSerializer


class SobrietyDateViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    model = User
    queryset = User.objects.exclude(social_type=User.SocialLoginOption.ADMIN)
    serializer_class = UserSobrietySerializer
    permission_classes = [IsAuthenticated]


class UserLoginViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    model = User
    queryset = User.objects.exclude(social_type=User.SocialLoginOption.ADMIN)
    serializer_class = AppUserLoginSerializer
    permission_classes = []
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        request_data = request.data
        social_type = request_data.get('social_type')
        social_id = request_data.get('social_id')
        customised_query = self.get_queryset().filter(social_id=social_id, social_type=social_type)
        if customised_query.exists():
            serialized = self.get_serializer(instance=customised_query.first())
            headers = self.get_success_headers(serialized.data)
            return Response(serialized.data, status=status.HTTP_201_CREATED, headers=headers)
        return super().create(request, *args, **kwargs)
