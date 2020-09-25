from rest_framework import viewsets
from imagens.models import Imagem
from imagens.serializers import ImagemSerializer

class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer