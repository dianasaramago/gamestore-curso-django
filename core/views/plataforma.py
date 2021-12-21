from django.db.models.base import Model
from rest_framework.viewsets import ModelViewSet

from core.models import Plataforma
from core.serializers import PlataformaSerializer


class PlataformaViewSet(ModelViewSet):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSerializer
