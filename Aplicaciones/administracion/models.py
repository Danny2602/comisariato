# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.utils import timezone

class Categoria(models.Model):
    idcategoria = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    portada = models.CharField(max_length=100)
    datecreated = models.DateTimeField(default=timezone.now)
    ruta = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'categoria'


class Contacto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mensaje = models.TextField()
    ip = models.CharField(max_length=15)
    dispositivo = models.CharField(max_length=25)
    useragent = models.TextField()
    datecreated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contacto'


class DetallePedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    pedidoid = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='pedidoid')
    productoid = models.ForeignKey('Producto', models.DO_NOTHING, db_column='productoid')
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_pedido'


class DetalleTemp(models.Model):
    id = models.BigAutoField(primary_key=True)
    personaid = models.BigIntegerField()
    productoid = models.ForeignKey('Producto', models.DO_NOTHING, db_column='productoid')
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    cantidad = models.IntegerField()
    transaccionid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'detalle_temp'


class Imagen(models.Model):
    id = models.BigAutoField(primary_key=True)
    productoid = models.ForeignKey('Producto', models.DO_NOTHING, db_column='productoid', related_name='imagenes')
    img = models.ImageField(upload_to='imagenes/')

    class Meta:
        managed = False
        db_table = 'imagen'


class Modulo(models.Model):
    idmodulo = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'modulo'


class Pedido(models.Model):
    idpedido = models.BigAutoField(primary_key=True)
    referenciacobro = models.CharField(max_length=255, blank=True, null=True)
    idtransaccionpaypal = models.CharField(max_length=255, blank=True, null=True)
    datospaypal = models.TextField(blank=True, null=True)
    personaid = models.ForeignKey('Persona', models.DO_NOTHING, db_column='personaid')
    fecha = models.DateTimeField()
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2)
    monto = models.DecimalField(max_digits=11, decimal_places=2)
    tipopagoid = models.ForeignKey('Tipopago', models.DO_NOTHING, db_column='tipopagoid')
    direccion_envio = models.TextField()
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido'


class Permisos(models.Model):
    idpermiso = models.BigAutoField(primary_key=True)
    rolid = models.ForeignKey('Rol', models.DO_NOTHING, db_column='rolid')
    moduloid = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='moduloid')
    r = models.IntegerField()
    w = models.IntegerField()
    u = models.IntegerField()
    d = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permisos'


class Persona(models.Model):
    idpersona = models.BigAutoField(primary_key=True)
    identificacion = models.CharField(max_length=30, blank=True, null=True)
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email_user = models.CharField(max_length=100)
    password = models.CharField(max_length=75)
    nit = models.CharField(max_length=20, blank=True, null=True)
    nombrefiscal = models.CharField(max_length=80, blank=True, null=True)
    direccionfiscal = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True)
    rolid = models.ForeignKey('Rol', models.DO_NOTHING, db_column='rolid')
    datecreated = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'persona'


class Post(models.Model):
    idpost = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    portada = models.CharField(max_length=100, blank=True, null=True)
    datecreate = models.DateTimeField()
    ruta = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'post'


class Producto(models.Model):
    idproducto = models.BigAutoField(primary_key=True)
    categoriaid = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoriaid')
    codigo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.CharField(max_length=100, blank=True, null=True)
    datecreated = models.DateTimeField(default=timezone.now)
    ruta = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'producto'


class Reembolso(models.Model):
    id = models.BigAutoField(primary_key=True)
    pedidoid = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='pedidoid')
    idtransaccion = models.CharField(max_length=255)
    datosreembolso = models.TextField()
    observacion = models.TextField()
    status = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'reembolso'


class Rol(models.Model):
    idrol = models.BigAutoField(primary_key=True)
    nombrerol = models.CharField(max_length=50)
    descripcion = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rol'


class Suscripciones(models.Model):
    idsuscripcion = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    datecreated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'suscripciones'


class Tipopago(models.Model):
    idtipopago = models.BigAutoField(primary_key=True)
    tipopago = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipopago'
