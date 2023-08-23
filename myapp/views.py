from django.shortcuts import render
from django.http import HttpResponse
from .models import Camiseta
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

#Home donde están cargadas todas las camisetas registradas en la base de datos
def index(request):
    camisetas = Camiseta.objects.all()

    return render(request, "index.html", {"camisetas": camisetas})

#Información acerca del Ecomerce
def nosotros(request):
    title = 'nosotros'
    
    return render(request, 'nosotros.html', {'title': title})

#Permite cargar una camiseta seleccionada en la sección de tienda de index.html. Se muestra la imágen y sus datos. Recibe el id de la camiseta seleccionada para hacer la consulta en la base de datos
def ver_camiseta(request, id):
    camiseta = Camiseta.objects.get(pk = id) 
    
    return render(request, "productos.html", {"camiseta": camiseta})

#Administrador para acceder al formulario de creación de nueva camiseta
def adm_camiseta(request):

    return render(request, "adminCamiseta.html")


#Permite crear una nueva camiseta. Verifica que no exista una camiseta con el mismo nombre 
def crear_camiseta(request):
    nombre = request.POST.get('inp_nombre')
    descripcion = request.POST.get('inp_descripcion')
    precio = request.POST.get('inp_precio')
    imagen = request.FILES['inp_imagen']

    #Pregunta por la existencia de la camiseta actual
    validacion = Camiseta.objects.filter(nombre = nombre)

    if validacion:
        messages.error(request, '¡La camiseta ya existe!')
        return redirect('/adminCamiseta')        
    else:
        camiseta = Camiseta.objects.create(
            nombre = nombre,
            descripcion = descripcion,
            precio = precio,
            imagen = imagen
        )

        messages.success(request, '¡Camiseta creada correctamente!')
        return redirect('/adminCamiseta')


