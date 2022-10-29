from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'social_id',
            'social_type'
        ]


class AppUserLoginSerializer(serializers.ModelSerializer):
    social_type_name = serializers.CharField(source='get_social_type_display', read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'social_id',
            'social_type',
            'social_type_name',
        ]

    def create(self, validated_data):
        user_details = self.instance.filter(social_id=validated_data.social_id)
        if user_details.exists():
            return user_details
        return self.instance.create_user(validated_data)

    def to_representation(self, instance):
        # token = Token.objects.create(user=self)
        representation = super().to_representation(instance)
        representation['token'] = "some_random_shit"
        return representation
