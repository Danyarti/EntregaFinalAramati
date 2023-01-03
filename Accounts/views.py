from django.shortcuts import render
from Accounts.forms import userForm
from Accounts.models import user


# Create your views here.
def singup (request):
    if request.method=="POST":
        form=userForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            user_name=info["user_name"]
            email=info["email"]
            password=info["password"]

            user_Form=user(user_name=user_name, email=email, password=password)
            user_Form.save()
            return render (request, "signupSuseccessful.html", {"message": "El usuario ha sido registrado correctamente" })

    else: 
        formulario=singup
        
    return render (request, "login.html")
