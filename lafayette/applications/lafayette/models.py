from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


Userr = get_user_model()

# Create your models here.
class Operacion(models.Model):
    tipo = models.CharField('Operación a realizar', max_length=20)
    def __str__(self):
        return self.tipo 

class Producto(models.Model):
    producto = models.CharField('Producto a ofertar', max_length=50)
    def __str__(self):
        return self.producto 

class Amigo(models.Model):
    opc = (
        ('Ofrece','Ofrece'),
        ('Desea','Desea'),
    )

    opc2 = (
        ('1','Publica'),
        ('2','Privada'),
    )
    user = models.ForeignKey(Userr, null=True,blank=True, on_delete=models.CASCADE)
    cliente = models.CharField('Nombre del Cliente', max_length=60)
    operacion = models.ForeignKey(Operacion, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    municipio = models.CharField('Municipio', max_length=50)
    estado = models.CharField('Estado', max_length=50)
    email = models.EmailField()
    telefono = models.CharField('Telefono', max_length=10)
    opcion = models.CharField('Operacion a realizar', max_length=20,choices=opc)
    titulo = models.CharField('Título', max_length=300)
    nota = models.CharField('Descripción del inmueble', max_length=300)
    publicar = models.CharField('Esta nota sera ?', max_length=20,choices=opc2)
    img=models.ImageField('Seleccionar una imagen',upload_to = 'static/media')
    precio = models.FloatField('Precio ',max_length=50)
    finalizada = models.BooleanField(default=False) 
    
    def __str__(self):
        return self.cliente 

class Contacto(models.Model):
    opc = (
        ('Vender','Vender'),
        ('Rentar','Rentar'),
    )

    nombre = models.CharField('Nombre del Cliente', max_length=60)
    telefono = models.CharField('Número de teléfono', max_length=10)
    opcion = models.CharField('Vender o Rentar', max_length=20,choices=opc)
    datos = models.CharField('Datos de la propiedad', max_length=600)

    def __str__(self):
        return self.nombre 
