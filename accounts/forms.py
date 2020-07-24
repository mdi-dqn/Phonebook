from django import forms
from django.contrib.auth.models import User

class loginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput())

class registerUser(forms.ModelForm):
    phone = forms.CharField(widget=forms.NumberInput())
    age = forms.IntegerField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'password' : forms.PasswordInput()
        }