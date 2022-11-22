from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.mixins import NestedViewSetMixin

from common.utils import MultiSerializerViewSetMixin
from literature.models import Literature, LiteratureSubSection
from literature.serializer import (
    LiteratureSerializer,
    LiteratureSubSectionSerializer,
    LiteratureSubSectionDetailSerializer,
)


class LiteratureViewSet(NestedViewSetMixin, mixins.RetrieveModelMixin,
                        mixins.ListModelMixin, viewsets.GenericViewSet):
    model = Literature
    queryset = Literature.objects.all()
    serializer_class = LiteratureSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'subtitle']


class LiteratureSubSectionDetailViewSet(NestedViewSetMixin, MultiSerializerViewSetMixin,
                                        mixins.RetrieveModelMixin, mixins.ListModelMixin,
                                        viewsets.GenericViewSet):
    model = LiteratureSubSection
    serializer_action_classes = {
        'list': LiteratureSubSectionSerializer,
        'retrieve': LiteratureSubSectionDetailSerializer,
    }
    queryset = LiteratureSubSection.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'subtitle']
