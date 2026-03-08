from django.shortcuts import render

def index(request):
    return render(request, "entrenamiento/index.html")

def clases(request):
    return render(request, "entrenamiento/clases.html")

def contacto(request):
    return render(request, "entrenamiento/contacto.html")
