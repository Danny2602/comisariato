from django.contrib import admin

from .models import Categoria, Contacto, DetallePedido, DetalleTemp, Imagen, Pedido, Persona, Producto, Modulo,Permisos,Post,Reembolso,Rol,Suscripciones,Tipopago
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Contacto)
admin.site.register(DetallePedido)
admin.site.register(DetalleTemp)
admin.site.register(Imagen)
admin.site.register(Pedido)
admin.site.register(Persona)
admin.site.register(Producto)
admin.site.register(Modulo)
admin.site.register(Permisos)
admin.site.register(Post)
admin.site.register(Reembolso)
admin.site.register(Rol)
admin.site.register(Suscripciones)
admin.site.register(Tipopago)

