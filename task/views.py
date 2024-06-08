from django.shortcuts import render, redirect
# para saber si el login existe
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
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
                # Asegúrate de que 'tasks' esté definido en tus urls
                return redirect('Tasks')
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


def signout(request):
    logout(request)
    return redirect('Home')


def signin(request):
  if request.method == 'GET':
    return render(request, 'signin.html', {
        'form': AuthenticationForm
    })
  else:
      usuario=authenticate(request, usurname=request.POST['username'], password=request.POST['password'])
      if usuario is None:
          return render(request, 'signin.html', {
          'form': AuthenticationForm,
          'error':'Usuario o contraseña son incorrectas'
      })
          
      
