from django.db import models

# Create your models here.
class Camiseta(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(default='SOME STRING')
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='img', null=True)
    
    def __str__(self):
        return self.nombre