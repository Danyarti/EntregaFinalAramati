from django import forms

class userForm(forms.Form):
    username=forms.CharField(max_length=50)
    emailname=forms.EmailField(required=False, max_length=254)
    password=forms.CharField(label="Password", widget=forms.PasswordInput, strip=False)