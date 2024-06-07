from django.shortcuts import render
# clase que devuelve un formulario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # clase para registrar user
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html', {

    })


def signup(request):
    # se registra el usuario
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'forms': UserCreationForm
        })
    else:  # si las contraseñas no coinciden
        if request.POST['password1'] == request.POST['password2']:
           try:
               # register user
               usuario = User.objects.create_user(
                   username=request.POST['username'], password=request.POST['password1'])
               # hay que pasarle ususario y contraseña
               usuario.save()
               return HttpResponse('Usuario creado')
           except:
               return render(request, 'signup.html', {
                   'forms': UserCreationForm,
                   'error': 'El ususario ya extiste'
               })
        return render(request, 'signup.html', {
        'forms': UserCreationForm,
        'error':'Las contraseñas no coinciden'
        })

   
