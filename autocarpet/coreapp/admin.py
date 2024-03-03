from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Articulos)
admin.site.register(Barrios)
admin.site.register(Categorias)
admin.site.register(Colores)
admin.site.register(DetallePedido)
admin.site.register(Direcciones)
admin.site.register(EntregaMateriales)
admin.site.register(EntregasArticulos)
admin.site.register(EstadoPedido)
admin.site.register(EstadosArticulos)
admin.site.register(Estampados)
admin.site.register(MarcasVehiculos)
admin.site.register(MaterialesOrdenPersonalizada)
admin.site.register(MetodoEntrega)
admin.site.register(MetodoPago)
admin.site.register(OrdenPersonalizada)
admin.site.register(ModelosVehiculos)
admin.site.register(Pedidos)
admin.site.register(Localidades)
admin.site.register(PreciosProveedor)
admin.site.register(Productos)
admin.site.register(Proveedores)
admin.site.register(TiposArticulos)
admin.site.register(TiposVehiculos)


@admin.register(Usuarios)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombres_usuario', 'apellidos_usuario','contrasenia','email','telefono','direccion')
    list_editable = ('email',)
    search_fields = ('nombres_usuario',)
    list_filter = ('email',)
    list_max_show_all = 10
    list_per_page = 10