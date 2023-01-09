from django import forms
from Blog.models import *
from ckeditor_uploader.fields import RichTextUploadingField

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo','director','fecha_publicacion','pais_origen','imagen', 'sinopsis']
widgets = {
            
            'fecha_publicacion': DateTimeInput(attrs={'class': 'form-control'}),
            
        }