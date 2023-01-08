from django.db import models


# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField (max_length=100)
    fecha_publicacion = models.DateField(auto_now=False, auto_now_add=False)
    pais_origen = models.CharField (max_length=100)
    imagen = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    ##sinopsis = models.CharField( max_length=500) >CKeditor

    def __str__(self) -> str:
        return self.titulo + " " + self.director

