from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages


def index(request):
    return render(request, 'index.html',{

    })

def cart(request):
    return render(request, 'cart.html',{

    })

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('admin:index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'login.html',{

    })

def products(request):
    return render(request, 'products.html',{

    })

def product_detail(request):
    return render(request, 'product_detail.html',{

    })

def signup(request):
    return render(request, 'signup.html',{

    })

def forgot_password(request):
    return render(request, 'forgot_password.html',{

    })

def dashboard_prod(request):
    return render(request, 'dashboard_prod.html',{

    })

def dashboard(request):
    return render(request, 'dashboard.html',{

    })

def error404(request):
    return render(request, 'error404.html',{

    })

def error500(request):
    return render(request, 'error500.html',{

    })

