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

    # Método to string
    def __str__(self):
        return self.nombre_articulo

    class Meta:
        verbose_name = 'Articulo' # Cuando se registre la BD en Django
        verbose_name_plural = 'Articulos'
        db_table = 'articulos' # Nombre de la tabla


class Barrios(models.Model):
    id_barrio = models.AutoField(primary_key=True)
    nombre_barrio = models.CharField(unique=True, max_length=30)
    localidad = models.ForeignKey('Localidades', models.DO_NOTHING)

        # Método to string
    def __str__(self):
        return self.nombre_barrio

    class Meta:
        verbose_name = 'Barrio' # Cuando se registre la BD en Django
        verbose_name_plural = 'Barrios'
        db_table = 'barrios' # Nombre de la tabla


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(unique=True, max_length=30)
    descuento_categoria = models.IntegerField()

        # Método to string
    def __str__(self):
        return self.nombre_categoria

    class Meta:
        verbose_name = 'Categoria' # Cuando se registre la BD en Django
        verbose_name_plural = 'Categorias'
        db_table = 'categorias' # Nombre de la tabla


class Colores(models.Model):
    id_color = models.AutoField(primary_key=True)
    nombre_color = models.CharField(unique=True, max_length=30)

        # Método to string
    def __str__(self):
        return self.nombre_color

    class Meta:
        verbose_name = 'Color' # Cuando se registre la BD en Django
        verbose_name_plural = 'Colores'
        db_table = 'colores' # Nombre de la tabla


class DetallePedido(models.Model):
    id_detalle_pedido = models.AutoField(primary_key=True)
    producto = models.ForeignKey('Productos', models.DO_NOTHING)
    pedido = models.ForeignKey('Pedidos', models.DO_NOTHING)
    cantidad_solicitada = models.IntegerField()

        # Método to string
    def __str__(self):
        return self.id_detalle_pedido

    class Meta:
        verbose_name = 'Detalle pedido' # Cuando se registre la BD en Django
        verbose_name_plural = 'Detalle pedidos'
        db_table = 'detalle_pedido' # Nombre de la tabla


class Direcciones(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    detalles = models.CharField(max_length=100)
    barrio = models.ForeignKey(Barrios, models.DO_NOTHING)

    def __str__(self):
        return self.id_direccion

    class Meta:
        verbose_name = 'Direccion' # Cuando se registre la BD en Django
        verbose_name_plural = 'Direcciones'
        db_table = 'direccion' # Nombre de la tabla


class EntregaMateriales(models.Model):
    id_entrega_material = models.AutoField(primary_key=True)
    fecha_entrega_material = models.DateTimeField()
    cantidad_entrega_material = models.IntegerField()
    proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING)

    def __str__(self):
        return self.id_entrega_material

    class Meta:
        verbose_name = 'Entrega material' # Cuando se registre la BD en Django
        verbose_name_plural = 'Entregas materiales'
        db_table = 'entrega_materiales' # Nombre de la tabla



class EntregasArticulos(models.Model):
    articulo = models.ForeignKey(Articulos, models.DO_NOTHING)
    entrega_material = models.ForeignKey(EntregaMateriales, models.DO_NOTHING)

    def __str__(self):
        return self.articulo

    class Meta:
        verbose_name = 'Entrega articulo' # Cuando se registre la BD en Django
        verbose_name_plural = 'Entregas articulos'
        db_table = 'entregas_articulos' # Nombre de la tabla



class EstadoPedido(models.Model):
    id_estado_pedido = models.AutoField(primary_key=True)
    nombre_estado_pedido = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.nombre_estado_pedido

    class Meta:
        verbose_name = 'Estado pedido' # Cuando se registre la BD en Django
        verbose_name_plural = 'Estado pedidos'
        db_table = 'estado_pedido' # Nombre de la tabla



class EstadosArticulos(models.Model):
    id_estado_articulo = models.AutoField(primary_key=True)
    nombre_estado_articulo = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.nombre_estado_articulo

    class Meta:
        verbose_name = 'Estado articulo' # Cuando se registre la BD en Django
        verbose_name_plural = 'Estado articulos'
        db_table = 'estados_articulos' # Nombre de la tabla


class Estampados(models.Model):
    id_estampado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    imagen_url = models.TextField(unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Estampado' # Cuando se registre la BD en Django
        verbose_name_plural = 'Estampados'
        db_table = 'estampados' # Nombre de la tabla


class Localidades(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    nombre_localidad = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.nombre_localidad

    class Meta:
        verbose_name = 'Localidad' # Cuando se registre la BD en Django
        verbose_name_plural = 'Localidades'
        db_table = 'localidades' # Nombre de la tabla


class MarcasVehiculos(models.Model):
    id_marca_vehiculo = models.AutoField(primary_key=True)
    nombre_marca_vehiculo = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.nombre_marca_vehiculo

    class Meta:
        verbose_name = 'Marca vehiculo' # Cuando se registre la BD en Django
        verbose_name_plural = 'Marcas vehiculos'
        db_table = 'marcas_vehiculos' # Nombre de la tabla


class MaterialesOrdenPersonalizada(models.Model):
    articulo = models.ForeignKey(Articulos, models.DO_NOTHING)
    orden_personalizada = models.ForeignKey('OrdenPersonalizada', models.DO_NOTHING)

    def __str__(self):
        return self.articulo

    class Meta:
        verbose_name = 'Material orden personalizada' # Cuando se registre la BD en Django
        verbose_name_plural = 'Materiales orden personalizadas'
        db_table = 'materiales_orden_personalizada' # Nombre de la tabla


class MetodoEntrega(models.Model):
    id_metodo_entrega = models.AutoField(primary_key=True)
    nombre_metodo_entrega = models.CharField(unique=True, max_length=30)
    costo_metodo_entrega = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    def __str__(self):
        return self.nombre_metodo_entrega

    class Meta:
        verbose_name = 'Metodo entrega' # Cuando se registre la BD en Django
        verbose_name_plural = 'Metodos de entregas'
        db_table = 'metodo_entrega' # Nombre de la tabla


class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    nombre_metodo_pago = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.nombre_metodo_pago

    class Meta:
        verbose_name = 'Metodo pago' # Cuando se registre la BD en Django
        verbose_name_plural = 'Metodos de pagos'
        db_table = 'metodo_pago' # Nombre de la tabla


class ModelosVehiculos(models.Model):
    id_modelo_vehiculo = models.AutoField(primary_key=True)
    nombre_modelo_vehiculo = models.CharField(unique=True, max_length=30)
    numero_modelo_vehiculo = models.IntegerField()
    marca_vehiculo = models.ForeignKey(MarcasVehiculos, models.DO_NOTHING)
    tipo_vehiculo = models.ForeignKey('TiposVehiculos', models.DO_NOTHING)

    def __str__(self):
        return self.nombre_modelo_vehiculo

    class Meta:
        verbose_name = 'modelo vehiculo' # Cuando se registre la BD en Django
        verbose_name_plural = 'Modelos vehiculos'
        db_table = 'modelos_vehiculos' # Nombre de la tabla


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

    def __str__(self):
        return self.id_orden_personalizada

    class Meta:
        verbose_name = 'Orden Personalizada' # Cuando se registre la BD en Django
        verbose_name_plural = 'Ordenes personalizadas'
        db_table = 'orden_personalizada' # Nombre de la tabla


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    fecha_entrega_pedido = models.TimeField()
    precio_total_pedido = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    fecha_pago_pedido = models.DateTimeField()
    usuario = models.ForeignKey('Usuarios', models.DO_NOTHING)
    metodo_entrega = models.ForeignKey(MetodoEntrega, models.DO_NOTHING)
    metodo_pago = models.ForeignKey(MetodoPago, models.DO_NOTHING)
    estado_pedido = models.ForeignKey(EstadoPedido, models.DO_NOTHING)

    def __str__(self):
        return self.id_pedido

    class Meta:
        verbose_name = 'pedido' # Cuando se registre la BD en Django
        verbose_name_plural = 'pedidos'
        db_table = 'pedidos' # Nombre de la tabla


class PreciosProveedor(models.Model):
    id_precio_proveedor = models.AutoField(primary_key=True)
    precio_proveedor = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    articulo = models.ForeignKey(Articulos, models.DO_NOTHING)
    proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING)

    def __str__(self):
        return self.id_precio_proveedor

    class Meta:
        verbose_name = 'precio proveedor' # Cuando se registre la BD en Django
        verbose_name_plural = 'precios proveedores'
        db_table = 'precios_proveedor' # Nombre de la tabla


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    imagen_producto = models.TextField(unique=True)
    articulo = models.ForeignKey(Articulos, models.DO_NOTHING)
    categoria = models.ForeignKey(Categorias, models.DO_NOTHING)
    modelo_vehiculo = models.ForeignKey(ModelosVehiculos, models.DO_NOTHING)

    def __str__(self):
        return self.id_producto

    class Meta:
        verbose_name = 'producto' # Cuando se registre la BD en Django
        verbose_name_plural = 'productos'
        db_table = 'productos' # Nombre de la tabla


class Proveedores(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(unique=True, max_length=30)
    telefono_proveedor = models.CharField(unique=True, max_length=10)
    email_proveedor = models.CharField(unique=True, max_length=60)
    direccion = models.ForeignKey(Direcciones, models.DO_NOTHING)

    def __str__(self):
        return self.nombre_proveedor

    class Meta:
        verbose_name = 'proveedor' # Cuando se registre la BD en Django
        verbose_name_plural = 'proveedores'
        db_table = 'proveedores' # Nombre de la tabla


class TiposArticulos(models.Model):
    id_tipo_articulo = models.AutoField(primary_key=True)
    nombre_tipo_articulo = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.nombre_tipo_articulo

    class Meta:
        verbose_name = 'tipo articulo' # Cuando se registre la BD en Django
        verbose_name_plural = 'tipos articulos'
        db_table = 'tipos_articulos' # Nombre de la tabla


class TiposVehiculos(models.Model):
    id_tipo_vehiculo = models.AutoField(primary_key=True)
    nombre_tipo_vehiculo = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.nombre_tipo_vehiculo

    class Meta:
        verbose_name = 'tipo vehiculo' # Cuando se registre la BD en Django
        verbose_name_plural = 'tipos vehiculos'
        db_table = 'tipos_vehiculos' # Nombre de la tabla


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombres_usuario = models.CharField(max_length=30)
    apellidos_usuario = models.CharField(max_length=30)
    contrasenia = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=60)
    telefono = models.CharField(unique=True, max_length=10)
    direccion = models.ForeignKey(Direcciones, models.DO_NOTHING)

    def __str__(self):
        return self.nombres_usuario

    class Meta:
        verbose_name = 'usuario' # Cuando se registre la BD en Django
        verbose_name_plural = 'usuarios'
        db_table = 'usuarios' # Nombre de la tabla
