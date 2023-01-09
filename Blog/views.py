from django.shortcuts import render
from Blog.forms import *
from Blog.forms import *
from django.contrib.auth.decorators import login_required
from Accounts.models import userAvatar
from Accounts.views import getAvatar

# Create your views here.

@login_required
def index (request):
    return render (request, "index.html", {"imagen":getAvatar(request)})

@login_required
def blogForm (request):
    if request.method=="POST":
        form=BlogForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            titulo = info ["titulo"]
            director = info["director"]
            fecha_publicacion =info ["fecha_publicacion"]
            pais_origen = info ["pais_origen"]
            imagen = info ["imagen"]
            sinopsis = info ["sinopsis"]


            blog_Form=Blog(titulo=titulo, director=director, fecha_publicacion=fecha_publicacion, pais_origen=pais_origen, imagen=imagen, sinopsis=sinopsis)
            blog_Form.save()
            return render (request, "blogSuccessful.html", {"message": "Su reseña se agregó correctamente","imagen":getAvatar(request)})

    else:
        form=BlogForm

    return render (request, "blogForm.html", {"form": form, "imagen":getAvatar(request)})
