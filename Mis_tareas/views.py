from django.shortcuts import render, redirect
from .models import Tareas

# Create your views here.
def Lista_tareas(request):
    return render(request,'Listar_tareas.html')

def crear_tareas(request):
    mi_tarea=Tareas(Titulo=request.POST['txtTitulo'],Descripcion=request.POST['txtDescripcion'])
    mi_tarea.save()
    return redirect('/Lista_tareas/')