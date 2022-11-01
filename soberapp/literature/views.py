from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated

from common.utils import MultiSerializerViewSetMixin
from literature.models import Literature, LiteratureSubSection
from literature.serializer import (
    LiteratureSerializer,
    LiteratureWithSubsectionSerializer,
    LiteratureSubSectionContentSerializer
)


class LiteratureViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    model = Literature
    queryset = Literature.objects.all()
    serializer_class = LiteratureSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'subtitle']


class LiteratureSubSectionViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    model = Literature
    queryset = Literature.objects.all()
    serializer_class = LiteratureWithSubsectionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'subtitle']


class LiteratureSubSectionDetailViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    model = LiteratureSubSection
    queryset = LiteratureSubSection.objects.all()
    serializer_class = LiteratureSubSectionContentSerializer
    permission_classes = [IsAuthenticated]
