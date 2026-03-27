from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.


def Inicio(request):
    return render(request, "pages/home.html")


def verproductos(request):
    query=Productos.objects.all()
    data={
        'listaProductos':query
    }
    return render(request,'pages/verproductos.html',data)


def AgregarProd(request):
    data={
        'Formularios':FormularioProductos()
    }  
    # METODO Q LLEGA 
    if request.method=='POST':
# QUERY  accion en base de datos borrar, agregar , actualizar , seleccioar 
        query=FormularioProductos(data=request.POST,files=request.FILES)
        if  query.is_valid():
            query.save()           
            data['mensaje']='datos registrados'
        else: 
            data['Formularios']=FormularioProductos()
    
    return render(request,'pages/AgregarProductos.html', data)
