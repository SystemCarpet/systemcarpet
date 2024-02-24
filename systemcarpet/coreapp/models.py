# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articulos(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    nombre_articulo = models.CharField(unique=True, max_length=30)
    cantidad_articulo = models.IntegerField()
    estado_articulo = models.ForeignKey('EstadosArticulos', models.DO_NOTHING)
    tipo_articulo = models.ForeignKey('TiposArticulos', models.DO_NOTHING)
    dimensiones_articulo = models.CharField(max_length=30, blank=True, null=True)
    descripcion_articulo = models.CharField(max_length=100, blank=True, null=True)
    precio_articulo = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'articulos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Barrios(models.Model):
    id_barrio = models.AutoField(primary_key=True)
    nombre_barrio = models.CharField(unique=True, max_length=30)
    localidad = models.ForeignKey('Localidades', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'barrios'


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(unique=True, max_length=30)
    descuento_categoria = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categorias'


class Colores(models.Model):
    id_color = models.AutoField(primary_key=True)
    nombre_color = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'colores'


class DetallePedido(models.Model):
    id_detalle_pedido = models.AutoField(primary_key=True)
    producto = models.ForeignKey('Productos', models.DO_NOTHING)
    pedido = models.ForeignKey('Pedidos', models.DO_NOTHING)
    cantidad_solicitada = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_pedido'


class Direcciones(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    detalles = models.CharField(max_length=100)
    barrio = models.ForeignKey(Barrios, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'direcciones'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EntregaMateriales(models.Model):
    id_entrega_material = models.AutoField(primary_key=True)
    fecha_entrega_material = models.DateTimeField()
    cantidad_entrega_material = models.IntegerField()
    proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entrega_materiales'


class EntregasArticulos(models.Model):
    articulo = models.ForeignKey(Articulos, models.DO_NOTHING)
    entrega_material = models.ForeignKey(EntregaMateriales, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entregas_articulos'


class EstadoPedido(models.Model):
    id_estado_pedido = models.AutoField(primary_key=True)
    nombre_estado_pedido = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class EstadosArticulos(models.Model):
    id_estado_articulo = models.AutoField(primary_key=True)
    nombre_estado_articulo = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'estados_articulos'


class Estampados(models.Model):
    id_estampado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    imagen_url = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'estampados'


class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    nombre_localidad = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'localidad'


class Localidades(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    nombre_localidad = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'localidades'


class MarcasVehiculos(models.Model):
    id_marca_vehiculo = models.AutoField(primary_key=True)
    nombre_marca_vehiculo = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'marcas_vehiculos'


class MaterialesOrdenPersonalizada(models.Model):
    articulo = models.ForeignKey(Articulos, models.DO_NOTHING)
    orden_personalizada = models.ForeignKey('OrdenPersonalizada', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'materiales_orden_personalizada'


class MetodoEntrega(models.Model):
    id_metodo_entrega = models.AutoField(primary_key=True)
    nombre_metodo_entrega = models.CharField(unique=True, max_length=30)
    costo_metodo_entrega = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'metodo_entrega'


class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    nombre_metodo_pago = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'metodo_pago'


class ModelosVehiculos(models.Model):
    id_modelo_vehiculo = models.AutoField(primary_key=True)
    nombre_modelo_vehiculo = models.CharField(unique=True, max_length=30)
    numero_modelo_vehiculo = models.IntegerField()
    marca_vehiculo = models.ForeignKey(MarcasVehiculos, models.DO_NOTHING)
    tipo_vehiculo = models.ForeignKey('TiposVehiculos', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'modelos_vehiculos'


class OrdenPersonalizada(models.Model):
    id_orden_personalizada = models.AutoField(primary_key=True)
    fecha_creacion_orden_personalizada = models.DateTimeField()
    base_antideslizante = models.BooleanField()
    impermeable = models.BooleanField()
    usuario = models.ForeignKey('Usuarios', models.DO_NOTHING)
    producto = models.ForeignKey('Productos', models.DO_NOTHING)
    color = models.ForeignKey(Colores, models.DO_NOTHING)
    estampado = models.ForeignKey(Estampados, models.DO_NOTHING)
    color_borde = models.ForeignKey(Colores, models.DO_NOTHING, related_name='ordenpersonalizada_color_borde_set')

    class Meta:
        managed = False
        db_table = 'orden_personalizada'


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    fecha_entrega_pedido = models.TimeField()
    precio_total_pedido = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    fecha_pago_pedido = models.DateTimeField()
    usuario = models.ForeignKey('Usuarios', models.DO_NOTHING)
    metodo_entrega = models.ForeignKey(MetodoEntrega, models.DO_NOTHING)
    metodo_pago = models.ForeignKey(MetodoPago, models.DO_NOTHING)
    estado_pedido = models.ForeignKey(EstadoPedido, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pedidos'


class PreciosProveedor(models.Model):
    id_precio_proveedor = models.AutoField(primary_key=True)
    precio_proveedor = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    articulo = models.ForeignKey(Articulos, models.DO_NOTHING)
    proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'precios_proveedor'


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    imagen_producto = models.TextField(unique=True)
    articulo = models.ForeignKey(Articulos, models.DO_NOTHING)
    categoria = models.ForeignKey(Categorias, models.DO_NOTHING)
    modelo_vehiculo = models.ForeignKey(ModelosVehiculos, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedores(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(unique=True, max_length=30)
    telefono_proveedor = models.CharField(unique=True, max_length=10)
    email_proveedor = models.CharField(unique=True, max_length=60)
    direccion = models.ForeignKey(Direcciones, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proveedores'


class TiposArticulos(models.Model):
    id_tipo_articulo = models.AutoField(primary_key=True)
    nombre_tipo_articulo = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'tipos_articulos'


class TiposVehiculos(models.Model):
    id_tipo_vehiculo = models.AutoField(primary_key=True)
    nombre_tipo_vehiculo = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'tipos_vehiculos'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombres_usuario = models.CharField(max_length=30)
    apellidos_usuario = models.CharField(max_length=30)
    contrasenia = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=60)
    telefono = models.CharField(unique=True, max_length=10)
    direccion = models.ForeignKey(Direcciones, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuarios'
