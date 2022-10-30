from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'social_id',
            'social_type',
            'sobriety_date',
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
        social_id = validated_data.get('social_id')
        social_type = validated_data.get('social_type')

        user_details = User.objects.filter(social_id=social_id, social_type=social_type)
        if user_details.exists():
            return user_details
        return User.objects.create_user(social_id=social_id, social_type=social_type)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['token'] = str(Token.objects.get_or_create(user=instance)[0])
        return representation
