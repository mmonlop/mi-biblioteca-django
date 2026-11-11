from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='principal'),
    path('<int:pk>', views.detalle_libro,name='detalle'),
]