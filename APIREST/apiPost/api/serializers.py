from rest_framework.serializers import ModelSerializer
from apiPost.models import register,login

class registerSerializer(ModelSerializer):
    class Meta:
        model = register
        fields = ['id', 'nombre', 'apellido','numId','username','password']

class loginSerializer(ModelSerializer):
    class Meta:
        model = login
        fields = ['id','username','password']

