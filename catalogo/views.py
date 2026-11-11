from django.shortcuts import render
from .models import Libro

# Create your views here.
def principal(request):
    return render(request, 'base.html')

def lista_libros(request):
    libros = Libro.objects.all().order_by('titulo')
    return render(request, 'listadoLibros.html', {'libros':libros})

def detalle_libro(request,pk):
    libro = Libro.objects.get(pk=pk)
    return render(request,'detalleLibro.html',{'libro':libro})