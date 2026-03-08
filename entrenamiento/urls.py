from django.urls import path 
from entrenamiento.views import*


urlpatterns =  [
   path("", home, name="home")

]