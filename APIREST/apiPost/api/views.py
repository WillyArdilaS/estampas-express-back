from rest_framework.viewsets import ModelViewSet
from apiPost.models import register,login
from apiPost.api.serializers import registerSerializer,loginSerializer

class registerApiViewSet(ModelViewSet):
    serializer_class = registerSerializer
    queryset = register.objects.all()

class loginApiViewSet(ModelViewSet):
    serializer_class = loginSerializer
    queryset = login.objects.all()
