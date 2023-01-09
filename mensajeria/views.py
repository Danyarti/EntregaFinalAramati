from django.shortcuts import render
from django.contrib.auth.models import User
from mensajeria.models import *
from mensajeria.forms import *
from django.contrib.auth.decorators import login_required
from Accounts.views import getAvatar

@login_required
def mensajeFormulario(request):
    usuario=request.user 
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            paraquien = informacion['receiver']
            textoMensaje = informacion['mensaje']
            mensaje1 = Mensaje(enviar=(usuario), recibir = (paraquien), mensaje=textoMensaje, leido = False)
            mensaje1.save()
            formulario = MensajeForm()
            return render(request, 'mensajeFormulario.html', {"form": formulario, "alerta": "El mensaje ha sido enviado exitosamente!", "imagen": getAvatar(request)} )
        else:
            return render(request, 'index.html', {"alerta": "Intentelo Nuevamente, hubo un error", "imagen": getAvatar(request)} )
    else:
        formulario = MensajeForm()
        return render(request, 'mensajeFormulario.html', {"form": formulario, "imagen": getAvatar(request)} )


@login_required
def leerMensaje(request):
    usuario = request.user
    herram = Mensaje.objects.filter(recibir = usuario)
    for mensaje in herram:
        mensaje.leido = True
        mensaje.save()  
    return render(request, "leerMensaje.html", {"mensajes": herram, "imagen": getAvatar(request)})


@login_required
def enviadoMensaje(request):
    usuario = request.user
    herram = Mensaje.objects.filter(enviar = usuario)
    return render(request, "enviadoMensaje.html", {"mensajes": herram, "imagen": getAvatar(request)})


@login_required
def mensajeUsuarios(request):
    return render(request, 'mensajeUsuarios.html',{'users': User.objects.exclude(username=request.user.username), "imagen": getAvatar(request)})