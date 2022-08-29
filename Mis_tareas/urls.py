from django.urls import path

from Mis_tareas.views import Lista_tareas, crear_tareas

urlpatterns = [
    path('',Lista_tareas),
    path('new/',crear_tareas)
]