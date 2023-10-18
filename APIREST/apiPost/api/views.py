from rest_framework.viewsets import ModelViewSet
from apiPost.models import usuario
from apiPost.api.serializers import registerSerializer,loginSerializer

class registerApiViewSet(ModelViewSet):
    serializer_class = registerSerializer
    queryset = usuario.objects.all()

class loginApiViewSet(ModelViewSet):
    serializer_class = loginSerializer
    queryset = usuario.objects.all()
