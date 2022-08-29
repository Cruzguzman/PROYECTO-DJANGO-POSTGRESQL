from django.db import models

# Create your models here.
class Tareas(models.Model):
    Titulo=models.CharField(max_length=100)
    Descripcion=models.TextField(blank=True)