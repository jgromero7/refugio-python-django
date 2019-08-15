from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.mascota.views import index, listado,  mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    # Vistas Basada en Funciones
    path('', index, name='index'),
    # path('nuevo/', mascota_view, name='mascota_crear'),
    # path('listar/', mascota_list, name='mascota_listar'),
    # path('editar/<int:id_mascota>', mascota_edit, name='mascota_editar'),
    # path('eliminar/<int:id_mascota>', mascota_delete, name='mascota_eliminar'),
    # Vistas Basada en clases
    path('listar/', login_required(MascotaList.as_view()), name='mascota_listar'),
    path('nuevo/', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    path('editar/<int:pk>', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    path('eliminar/<int:pk>', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
    path('listado/', listado, name='listado'),
]
