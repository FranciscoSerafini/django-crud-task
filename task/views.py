from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #clase que devuelve un formulario


# Create your views here.
def hellowordl(request):
    return render(request, 'signup.html', {
        'forms': UserCreationForm
    })
