from django.db.models.fields import files
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Mascota
from .forms import ContratarPlanForm, MascotaForm, CustomUserCreationForm, ClienteForm
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import forms
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request):
    return render(request, 'mascotas/index.html')

def servicios(request):
    return render(request, 'mascotas/servicios.html')

def contratarPlan(request):
    data = {
        'forms': ContratarPlanForm()
    }

    if request.method == 'POST':
        formulario = ContratarPlanForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Plan Contratado"
        else:
            data["forms"] = formulario
    return render(request, 'mascotas/contratarPlan.html', data)

#VISTAS CLIENTE
def agregar_Cliente(request):
    data = {
        'form': ClienteForm()
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            messages.success(request, "Cliente Agregado")
            
        else:
            data["form"] = formulario

    return render(request, 'mascotas/Cliente/agregar.html', data)

def listar_Cliente(request):
    clientes = Cliente.objects.all()

    data = {
        'clientes': clientes
    }
    return render(request, 'mascotas/Cliente/listar.html', data)

def modificar_Cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    data = {
        'form': ClienteForm(instance=cliente)
    }

    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance=cliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to=("listar_cliente"))
        data["form"] = formulario


    return render(request, 'mascotas/Cliente/modificar.html', data)

def eliminar_Cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_cliente")


#VISTAS MASCOTAS
def agregar_Mascota(request):
    data = {
        'form': MascotaForm()
    }
    if request.method == 'POST':
        formulario = MascotaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mascota Agregada")
            
        else:
            data["form"] = formulario

    return render(request, 'mascotas/Mascota/agregar.html', data)

def listar_Mascota(request):
    mascotas = Mascota.objects.all()
    data = {
        'mascotas': mascotas
    }
    return render(request, 'mascotas/Mascota/listar.html', data)


def modificar_Mascota(request, id):

    mascota = get_object_or_404(Mascota, id=id)

    data = {
        'form': MascotaForm(instance=mascota)
    }

    if request.method=='POST':
        formulario = MascotaForm(data=request.POST, instance=mascota, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to=("listar_mascota"))
        data["form"] = formulario


    return render(request, 'mascotas/Mascota/modificar.html', data)

def eliminar_Mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    mascota.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_mascota")


def registro(request):
    data = {
        'form': CustomUserCreationForm()

    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado Correctamente")
            return redirect(to="index")
        data["form"] = formulario


    return render(request, 'registration/registro.html', data)


def misMascotas(request):
    mascotas = Mascota.objects.all()
    data = {
        'mascotas': mascotas
    }
    return render(request, 'mascotas/misMascotas.html', data)



def miPerfil(request):
    return render(request, 'mascotas/miPerfil.html')