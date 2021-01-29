from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):

    GENDER_CHOICES =(
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otros'),
    )

    NIVEL =(
        ('JR','JR'),
        ('PLATA','PLATA'),
        ('ORO','ORO'),
        ('PREMIER','PREMIER'),
    )
    username = models.CharField(max_length=10, unique = True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    municipio = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True)
    nivel = models.CharField(max_length=7, choices=NIVEL,blank=True)
    ventas = models.FloatField(default=0,blank=True)
    is_staff = models.BooleanField(default=False)
   # is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    object = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres +' '+ self.apellidos
