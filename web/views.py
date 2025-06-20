from django.shortcuts import render

# Create your views here.
""" Vistas para el catalogo de productos """
def index(request):
    return render(request, 'index.html')