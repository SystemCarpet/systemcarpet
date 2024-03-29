
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin:index'),
    path('', views.index, name='index'),
    path('login.html', views.login_view, name='login'),




    path('cart.html', views.cart, name='cart'),
    path('products.html', views.products, name='products'),
    path('product_detail.html', views.product_detail, name='product_detail'),
    path('signup.html', views.signup, name='signup'),
    path('forgot_password.html', views.forgot_password, name='forgot_password'),
    path('dashboard_prod.html', views.dashboard_prod, name='dashboard_prod'),
    path('dashboard.html', views.dashboard, name='dashboard'),
    path('error404.html', views.error404, name='error404'),
    path('error500.html', views.error500, name='error500'),
]
