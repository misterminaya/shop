from django.shortcuts import render

from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.contrib.auth.models import User

from .forms import RegisterForm

def index(request):
    return render(request, 'index.html', {
        #context
        'message': 'Listado de productos',
        'title':'Productos',
        'products': [
            {'title': 'Playera', 'price':5, 'stock': True},
            {'title': 'Camisa', 'price':7, 'stock': True},
            {'title': 'Mochila', 'price':20, 'stock': False}
        ]
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') #diccionario
        password = request.POST.get('password') #None

        user = authenticate(username=username, password=password) #None
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'usuario o contraseña no válidos')

    return render(request, 'users/login.html',{

    })


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # username = form.cleaned_data.get('username') #Dic
        # email = form.cleaned_data.get('email') #Dic
        # password = form.cleaned_data.get('password') #Dic

        # user = User.objects.create_user(username, email, password)

        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')

    return render(request, 'users/register.html',{
        'form': form
    })
