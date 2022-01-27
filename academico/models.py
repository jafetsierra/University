from django.db import models

# Create your models here.
class Docente(models.Model):
    sexos = (
        ('F', 'femenino'),
        ('M', 'masculino')
    )
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    nombres          = models.CharField(max_length=50)
    sexo             = models.CharField(max_length=1,choices=sexos)
    
    def nombre_completo(self):
        return "{} {} {}".format(self.nombres, self.apellido_paterno, self.apellido_materno)
    
    def __str__(self):
        return self.nombre_completo()
    class Meta:
        verbose_name        = 'Docente'
        verbose_name_plural = 'Docentes'
        db_table            = 'docente'
        
class Curso(models.Model):
    name     = models.CharField(max_length=50)
    credits  = models.PositiveSmallIntegerField()
    capacity = models.IntegerField()
    docente  = models.ForeignKey(Docente, blank=True, null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.name, self.credits)

class Estudiante(models.Model):
    name     = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age      = models.PositiveSmallIntegerField()
    curso    = models.ManyToManyField(Curso)
    
    def __str__(self):
        text = "{0} {1}"
        return text.format(self.name, self.lastname)