from django.urls import path
from apps.adopcion.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate, \
    SolicitudDelete

urlpatterns = [
    path('', index),
    path('solicitud/listar/', SolicitudList.as_view(), name='solicitud_listar'),
    path('solicitud/nueva/', SolicitudCreate.as_view(), name='solicitud_crear'),
    path('solicitud/editar/<int:pk>', SolicitudUpdate.as_view(), name='solicitud_editar'),
    path('solicitud/eliminar/<int:pk>', SolicitudDelete.as_view(), name='solicitud_eliminar'),
]
