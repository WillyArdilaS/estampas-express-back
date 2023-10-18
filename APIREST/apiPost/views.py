from django.shortcuts import render
import json
from django.core import serializers
from apiPost.api.serializers import loginSerializer
from apiPost.models import usuario
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import collections 
# Create your views here.

def login(request):
    if request.method == 'GET':
        users = usuario.objects.all()
        peti = collections.OrderedDict(request.GET)
        #print(peti)
        #test_data = {
        #"usuario": "peperez",
        #"contrasenia": "asd1233",
        #"rol": "cliente"
        #}

        if (usuario.objects.filter(usuario = request.GET['usuario'], contrasenia = request.GET['contrasenia'])):
            return HttpResponse('Has sido loggeado')
        elif(usuario.objects.filter(usuario = request.GET['usuario'])):
            return HttpResponse('Contraseña incorrecta')
        else:
            return HttpResponse('Usuario no existente')
        

    return HttpResponse('a')