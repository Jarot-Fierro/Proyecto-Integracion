from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import logout
from productos.forms import RegisterForm
from productos.models import Producto,ProductoEliminado
from django.db.models import Q

from django.contrib.auth.decorators import login_required

from django.utils import timezone
import openpyxl


def error_404(request, exception):
    return render(request, 'error/404.html', status=404)

def inicio(request):
    return render(request,'web/presentacion.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request,'Usuario o contraseña no validos')
    return render(request,'usuarios/login.html',{
        
    })
@login_required
def index(request):
    return render(request,'web/index.html')

def gestion_productos(request):
    # Obtener todos los productos por defecto
    productos = Producto.objects.all()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            nombre_producto = form.cleaned_data['nombre_producto']
            precio = form.cleaned_data['precio']
            stock = form.cleaned_data['stock']
            fecha_compra = form.cleaned_data['fecha_compra']

            # Crear una instancia del modelo Product y guardarla en la base de datos
            product = Producto(nombre_producto=nombre_producto, precio=precio, stock=stock, fecha_compra=fecha_compra)
            product.save()

    else:
        form = RegisterForm()

    # Si se envía un parámetro de búsqueda por GET
    query = request.GET.get('search')
    if query:
        # Filtrar productos que comiencen con el nombre de búsqueda
        productos = Producto.objects.filter(nombre_producto__startswith=query)

    # Crear el formulario de registro de producto
    form = RegisterForm()

    return render(request, 'web/gestionproductos.html', {
        'productos': productos,
        'form': form,
    })  

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect ('login_view')

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    # Obtener los datos del producto a eliminar
    datos_producto = producto.__dict__

    # Crear un ProductoEliminado a partir de los datos del Producto eliminado
    producto_eliminado = ProductoEliminado(**datos_producto, fecha_eliminacion=timezone.now())
    producto_eliminado.save()

    producto.delete()   
    return redirect('gestion_productos')

def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)

    # Crear una instancia del producto eliminado y guardar la fecha actual
    producto_eliminado = ProductoEliminado(
        nombre_producto=producto.nombre_producto,
        precio=producto.precio,
        stock=producto.stock,
        fecha_compra=producto.fecha_compra,
        fecha_eliminacion=timezone.now(),
    )
    producto_eliminado.save()
    producto.delete()

    return redirect('gestion_productos')

def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            producto.nombre_producto = form.cleaned_data['nombre_producto']
            producto.precio = form.cleaned_data['precio']
            producto.stock = form.cleaned_data['stock']
            producto.fecha_compra = form.cleaned_data['fecha_compra']
            producto.save()
            return redirect('gestion_productos')
    else:
        form = RegisterForm(initial={
            'nombre_producto': producto.nombre_producto,
            'precio': producto.precio,
            'stock': producto.stock,
            'fecha_compra': producto.fecha_compra.strftime('%Y-%m-%d'),
        })

    return render(request, 'web/actualizarproducto.html', {'form': form, 'producto': producto})



def reportes(request):
    productos_eliminados = ProductoEliminado.objects.all()
    return render(request,'web/reportes.html',{
        'productos_eliminados': productos_eliminados
    })

def descargar_reportes(request):
    productos_eliminados = ProductoEliminado.objects.all()
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="registro_productos_eliminados.xlsx"'
    
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['ID', 'Nombre Producto', 'Precio', 'Stock', 'Fecha de Compra', 'Fecha de Eliminación'])

    for producto in productos_eliminados:
        fecha_compra_str = producto.fecha_compra.strftime('%Y-%m-%d')
        fecha_eliminacion_str = producto.fecha_eliminacion.strftime('%Y-%m-%d %H:%M:%S')
        ws.append([producto.id, producto.nombre_producto, producto.precio, producto.stock, fecha_compra_str, fecha_eliminacion_str])

    wb.save(response)
    return response