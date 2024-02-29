from django.contrib import admin

# Register your models here.

from .models import Usuarios,Direcciones,Barrios,Localidades

admin.site.register(Direcciones)
admin.site.register(Barrios)
admin.site.register(Localidades)



@admin.register(Usuarios)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombres_usuario', 'apellidos_usuario','contrasenia','email','telefono','direccion')
    list_editable = ('email',)
    search_fields = ('nombres_usuario',)
    list_filter = ('email',)
    list_max_show_all = 10
    list_per_page = 10