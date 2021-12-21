from rest_framework.viewsets import ModelViewSet

from core.models import Desenvolvedora
from core.serializers import DesenvolvedoraSerializer

class DesenvolvedoraViewSet(ModelViewSet):
    queryset = Desenvolvedora.objects.all()
    serializer_class = DesenvolvedoraSerializer