from django.shortcuts import render
from Blog.forms import *
from Blog.forms import *

# Create your views here.

def index (request):
    return render (request, 'index.html')

def blogForm (request):
    if request.method=="POST":
        form=BlogForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            titulo = info ["titulo"]
            director = info["director"]
            fecha_publicacion =info ["fecha_publicacion"]
            pais_origen = info ["pais_origen"]
            imagen = info ["imagen"]


            blog_Form=Blog(titulo=titulo, director=director, fecha_publicacion=fecha_publicacion, pais_origen=pais_origen, imagen=imagen)
            blog_Form.save()
            return render (request, "blogsuccessfull.html", {"message": "Su reseña se agregó correctamente"})

    else:
        form=BlogForm

    return render (request, "blogForm.html", {"form": form})
