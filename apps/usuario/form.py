from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroUserioForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username' : 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electronico',
        }