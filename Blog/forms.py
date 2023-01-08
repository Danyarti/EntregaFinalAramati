from django import forms
from Blog.models import *

class BlogForm(forms.ModelForm):
    titulo = forms.CharField(max_length=100)
    director = forms.CharField (max_length=100)
    fecha_publicacion = forms.DateField()
    pais_origen = forms.CharField (max_length=100)
    imagen = forms.ImageField()
    ##sinopsis = forms.CharField( max_length=500) >CKeditor

    class Meta:
        model = Blog
        fields = ['titulo','director','fecha_publicacion','pais_origen','imagen']