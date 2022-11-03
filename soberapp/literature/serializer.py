from rest_framework import serializers

from literature.models import Literature, LiteratureSubSection


class LiteratureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Literature
        fields = [
            'id',
            'title',
            'subtitle',
            'is_subtitle_active',
            'is_sequence_active',
        ]


class LiteratureSubSectionSerializer(serializers.ModelSerializer):
    is_subtitle_active = serializers.BooleanField(source='literature.is_subtitle_active')
    is_sequence_active = serializers.BooleanField(source='literature.is_sequence_active')

    class Meta:
        model = LiteratureSubSection
        fields = [
            'id',
            'title',
            'subtitle',
            'start_page',
            'end_page',
            'is_subtitle_active',
            'is_sequence_active',
        ]


class LiteratureSubSectionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiteratureSubSection
        fields = [
            'id',
            'title',
            'subtitle',
            'start_page',
            'end_page',
            'main_content',
        ]
