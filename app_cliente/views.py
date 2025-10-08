# app_cliente/views.py

from django.shortcuts import render
# IMPORTA TU MODELO CLIENTE de la app actual (app_cliente.models)
from .models import Cliente 

def index(request):
    # 1. Obtiene TODOS los objetos de tu modelo Cliente
    datos_cliente = Cliente.objects.all()
    
    contexto = {
        # Cambiamos el nombre de la variable para ser más claros, si quieres
        'clientes': datos_cliente  
    }
    
    # Renderiza la plantilla, pasando el contexto
    return render(request, 'index.html', contexto)