from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm

class singupForm (UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput, strip=False)
    password2=forms.CharField(label="Repita contraseña", widget=forms.PasswordInput, strip=False)

    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]
        help_texts = {k:"" for k in fields}