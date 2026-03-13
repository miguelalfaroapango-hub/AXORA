from django.urls import path
from entrenamiento.views import index, clases, contacto, promocion

urlpatterns = [
    path('', index, name='index'),
    path('clases/', clases, name='clases'),
    path('contacto/', contacto, name='contacto'),
    path('promocion/', promocion, name='promocion'),
]
