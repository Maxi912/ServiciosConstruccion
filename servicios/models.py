from django.db import models
from django.contrib.auth.models import User

class Servicio(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.titulo