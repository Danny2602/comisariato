
from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categorias/', views.categorias, name='categorias'),
    path('categoria_create/', views.categoria_create, name='categoria_create'),
    path('categoria_update/', views.categoria_update, name='categoria_update'),
    path('categoria_delete/', views.categoria_delete, name='categoria_delete'),
    path('categoria_detail/', views.categoria_detail, name='categoria_detail'),
    #producto
    path('productos/', views.productos, name='productos'),
    path('producto_create/', views.producto_create, name='producto_create'),
    path('producto_update/', views.producto_update, name='producto_update'),
    path('producto_delete/', views.producto_delete, name='producto_delete'),
    path('producto_detail/', views.producto_detail, name='producto_detail'),
    #imagenes
    path('imagenes/', views.imagenes, name='imagenes'),
    path('imagen_create/', views.imagen_create, name='imagen_create'),
    path('imagen_update/', views.imagen_update, name='imagen_update'),
    path('imagen_delete/', views.imagen_delete, name='imagen_delete'),
    path('imagen_detail/', views.imagen_detail, name='imagen_detail'),
    #tipo de pago
    path('tipopagos/', views.tipopagos, name='tipopagos'),
    path('tipopago_create/', views.tipopago_create, name='tipopago_create'),
    path('tipopago_update/', views.tipopago_update, name='tipopago_update'),
    path('tipopago_delete/', views.tipopago_delete, name='tipopago_delete'),
    path('tipopago_detail/', views.tipopago_detail, name='tipopago_detail'),
    # ROl
    path('roles/', views.roles, name='roles'),
    path('rol_create/', views.rol_create, name='rol_create'),
    path('rol_update/', views.rol_update, name='rol_update'),
    path('rol_delete/', views.rol_delete, name='rol_delete'),
    path('rol_detail/', views.rol_detail, name='rol_detail'),
    # persona
    path('personas/', views.personas, name='personas'),
    path('persona_create/', views.persona_create, name='persona_create'),
    path('persona_update/', views.persona_update, name='persona_update'),
    path('persona_delete/', views.persona_delete, name='persona_delete'),
    path('persona_detail/', views.persona_detail, name='persona_detail'),
    # pedido
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedido_create/', views.pedido_create, name='pedido_create'),
    path('pedido_update/', views.pedido_update, name='pedido_update'),
    path('pedido_delete/', views.pedido_delete, name='pedido_delete'),
    path('pedido_detail/', views.pedido_detail, name='pedido_detail'),
    # detalle pedido
    path('detalle_pedidos/', views.detalle_pedidos, name='detalle_pedidos'),
    path('detalle_pedido_create/', views.detalle_pedido_create, name='detalle_pedido_create'),
    path('detalle_pedido_update/', views.detalle_pedido_update, name='detalle_pedido_update'),
    path('detalle_pedido_delete/', views.detalle_pedido_delete, name='detalle_pedido_delete'),
    path('detalle_pedido_detail/', views.detalle_pedido_detail, name='detalle_pedido_detail'),
]