from rest_framework import serializers

from literature.models import Literature, LiteratureSubSection


class LiteratureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Literature
        fields = [
            'title',
            'sub_title',
        ]


class LiteratureSubSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiteratureSubSection
        fields = [
            'title',
            'sub_title',
            'is_sub_title_active',
            'main_content',
        ]
