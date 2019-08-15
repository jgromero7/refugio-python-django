# from django.shortcuts import render
import json
from rest_framework.views import APIView

from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.usuario.form import RegistroUserioForm
from apps.usuario.serializers import UserSerializer

# Create your views here.
class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/registro.html'
    form_class = RegistroUserioForm
    success_url = reverse_lazy('mascota:mascota_listar')

class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')