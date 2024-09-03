from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'categoria'

class Post(models.Model):

    autor = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='post')
    fecha_alta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.titulo} - {self.categoria}'
    
    class Meta:
        db_table = 'post'


