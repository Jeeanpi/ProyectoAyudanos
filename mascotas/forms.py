from django import forms
from django.db import models
from django.forms import fields
from .models import ContratarPlan, Cliente, Mascota
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContratarPlanForm(forms.ModelForm):

    class Meta:
        model = ContratarPlan
        fields = "__all__"

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = "__all__"

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = "__all__"


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
    

