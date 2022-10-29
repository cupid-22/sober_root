from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from literature.models import Literature
from literature.serializer import LiteratureSerializer


class LiteratureViewSet(viewsets.ModelViewSet):
    model = Literature
    queryset = Literature.objects.all()
    serializer_class = LiteratureSerializer
    # permission_classes = [IsAuthenticated]
