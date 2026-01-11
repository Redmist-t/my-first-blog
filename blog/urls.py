from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('nosotros', views.nosotros_list, name='nosotros.html'), # primer termino va nombre que uso en navegador, segundo termino va la funcion que uso para esa vista, nombre archivo html
]

#crear 5 plantillas html, inicio, quienes somos, contactos, galeria. 