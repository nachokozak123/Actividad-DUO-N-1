from django.db import models

# Create your models here.
class Productos(models.Model):
    Codigo=models.AutoField(primary_key=True)
    Nombre=models.TextField(max_length=20)
    Precio=models.FloatField()
    Cantidad=models.IntegerField()
    Descripcion=models.TextField(max_length=50)
    Fecha=models.DateField()
    Categoria=models.TextField(max_length=50)
    imagen=models.ImageField(upload_to='Productos', null=True)

    def __int__(self):
        return self.Codigob 