from rest_framework.viewsets import ModelViewSet

from core.models import Jogo
from core.serializers import JogoSerializer, JogoDetailSerializer


class JogoViewSet(ModelViewSet):
    queryset = Jogo.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return JogoDetailSerializer
        if self.action == "retrieve":
            return JogoDetailSerializer
        return JogoSerializer