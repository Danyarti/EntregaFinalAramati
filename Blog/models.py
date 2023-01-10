from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField (max_length=50)
    fecha_publicacion = models.DateField(auto_now=False, auto_now_add=False)
    pais_origen = models.CharField (max_length=100)
    imagen = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=None, blank=True)
    sinopsis = RichTextUploadingField()
    autor = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.titulo + " " + self.director

