from rest_framework.serializers import ModelSerializer
from apiPost.models import usuario

class registerSerializer(ModelSerializer):
    class Meta:
        model = usuario
        fields = ['tipoID', 'numeroID', 'nombre', 'apellido','genero', 'rol', 'correo', 'usuario', 'contrasenia']

class loginSerializer(ModelSerializer):
    class Meta:
        model = usuario
        fields = ['id', 'usuario', 'contrasenia', 'rol']

