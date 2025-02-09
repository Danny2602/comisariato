
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
]