
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('templates/cart.html', views.cart, name='cart'),
    path('templates/login.html', views.login, name='login'),
    path('templates/products.html', views.products, name='products'),
    path('templates/product_detail.html', views.product_detail, name='product_detail'),
    path('templates/signup.html', views.signup, name='signup'),
    path('templates/forgot_password.html', views.forgot_password, name='forgot_password'),
    path('templates/dashboard_prod.html', views.dashboard_prod, name='dashboard_prod'),
    path('templates/dashboard.html', views.dashboard, name='dashboard'),
    path('templates/error404.html', views.error404, name='error404'),
    path('templates/error500.html', views.error500, name='error500'),   
]
