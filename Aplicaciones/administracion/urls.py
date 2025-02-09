
from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categorias/', views.categorias, name='categorias'),
    path('categoria_create/', views.categoria_create, name='categoria_create'),
    path('categoria_update/', views.categoria_update, name='categoria_update'),
    path('categoria_delete/', views.categoria_delete, name='categoria_delete'),
    path('categoria_detail/', views.categoria_detail, name='categoria_detail'),

]