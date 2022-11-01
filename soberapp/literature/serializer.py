from rest_framework import serializers

from literature.models import Literature, LiteratureSubSection


class LiteratureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Literature
        fields = [
            'id',
            'title',
            'subtitle',
        ]


class LiteratureSubSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiteratureSubSection
        fields = [
            'id',
            'title',
            'subtitle',
            'start_page',
            'end_page',
        ]


class LiteratureSubSectionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiteratureSubSection
        fields = [
            'id',
            'title',
            'subtitle',
            'start_page',
            'end_page',
        ]


class LiteratureWithSubsectionSerializer(serializers.ModelSerializer):
    subsection = LiteratureSubSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Literature
        fields = [
            'id',
            'title',
            'subtitle',
            'is_subtitle_display_active',
            'is_sequence_display_active',
            'subsection',
        ]
