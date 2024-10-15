from django.db import models

# Create your models here.

class Alumno(models.Model):
    apaterno=models.CharField(max_length=50,verbose_name="apellido paterno jaja")
    amaterno=models.CharField(max_length=50,verbose_name="apellido materno")
    nombre=models.CharField(max_length=100,verbose_name="Nombree (s)")
    fecha_nacimiento=models.DateField(verbose_name="fecha de nacimiento",null=False,blank=False)
    fecha_ingreso=models.DateField(verbose_name="fecha de ingreso",null=False,blank=False)

    class Frase(models.model):
        Comentario=models.TextField(verbose_name="comentario")
        Alumno_fk=models.ForeignKey(Alumno, on_delete=models.CASCADE)