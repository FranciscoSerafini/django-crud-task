from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login
from django.db import IntegrityError

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'forms': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Intentar registrar el usuario
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('Tasks')  # Asegúrate de que 'tasks' esté definido en tus urls
            except IntegrityError:
                return render(request, 'signup.html', {
                    'forms': UserCreationForm(),
                    'error': 'El usuario ya existe'
                })
            except Exception as e:
                return render(request, 'signup.html', {
                    'forms': UserCreationForm(),
                    'error': f'Error desconocido: {str(e)}'
                })
        return render(request, 'signup.html', {
            'forms': UserCreationForm(),
            'error': 'Las contraseñas no coinciden'
        })

def task(request):
    return render(request, 'tasks.html')

