from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detalle', views.detalle_list, name='detalle.html'), # primer termino va nombre que uso en navegador, segundo termino va la funcion que uso para esa vista, nombre archivo html
]