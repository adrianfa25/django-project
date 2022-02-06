from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#queremos hacer que el formulario se base en un modelo. EN el de user-
#si queremos ver todos los campos que hay, tenemos que entrar a la base de datos y abrir auth_user

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

