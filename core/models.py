from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, codigo, password=None, **extra_fields):
        if not codigo:
            raise ValueError('El nombre de usuario es necesario')
        user = self.model(codigo=codigo, **extra_fields)
        user.set_password(password)  # Codifica la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, codigo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(codigo, password, **extra_fields)
    
# Create your models here.
class Usuario(AbstractBaseUser, PermissionsMixin):
    codigo = models.CharField(primary_key=True, max_length=9)
    password = models.CharField(max_length=255)
    nombre = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(null=True)
    edad = models.IntegerField(null=True)
    sexo = models.CharField(max_length=1, null=True)
    tipo = models.CharField(max_length=1, null=True)
    email = models.EmailField(blank=True,null=True)
    seleccion = models.CharField(blank=True, max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(blank=True, null=True, max_length=50)
    programa = models.CharField(blank=True, null=True,max_length=60)
    semestre = models.IntegerField(blank=True, null=True)
    objects = UsuarioManager()

    USERNAME_FIELD = 'codigo'
    REQUIRED_FIELDS = ['nombre', 'email']
#'fecha_nacimiento','edad','sexo','tipo','seleccion'
    class Meta:
        db_table = 'Usuario'
        db_table_comment = 'Contiene la informaci�n  de los usuarios registrados '

    def __str__(self):
        return self.nombre

class Deporte(models.Model):
    idDeporte = models.CharField(primary_key=True,max_length=2)
    nombre_dep = models.CharField()

    def __str__(self):
        return self.nombre_dep

class Campeonato(models.Model):
    idCampeonato = models.CharField(primary_key=True,max_length=5)
    idDeporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=1)
    fecha_inicio = models.DateField()

    def __str__(self):
        return self.nombre

class Eventos(models.Model):
    #idEvento = models.CharField(primary_key=True,max_length=5)
    nombre_ev = models.CharField(max_length=50)
    fecha = models.DateField()
    lugar = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100,  blank=True)

class Equipos(models.Model):
    idEquipo = models.CharField(primary_key=True, max_length=5)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    nombre_eq = models.CharField(max_length=50)
    num_integrantes = models.IntegerField()

class Desafios(models.Model):
    idDesafio = models.CharField(primary_key=True,max_length=6)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    equipo1 = models.CharField(max_length=50)
    equipo2 = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=100)
    ganador = models.CharField()

class Rendimiento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    campo1 = models.IntegerField(null=True)
    campo2 = models.IntegerField(null=True)
    campo3 = models.IntegerField(null=True)
    campo4 = models.IntegerField(null=True)
    campo5 = models.IntegerField(null=True)
    grasa_corporal = models.IntegerField(null=True)
    masa_muscular = models.IntegerField(null=True)
    rendimiento = models.IntegerField(null=True)

