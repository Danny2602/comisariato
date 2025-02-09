from django.shortcuts import render,get_object_or_404
from .models import Categoria, Imagen,Producto, Tipopago
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def categorias(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        categorias = Categoria.objects.all()
        html = render_to_string('categoria/partials/categoria_list.html', {'categorias': categorias})
        return JsonResponse({'html': html})
    categorias = Categoria.objects.all()
    return render(request, 'categoria/categoria.html', {'categorias': categorias})

def categoria_create(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        portada = request.POST.get('portada')
        ruta = request.POST.get('ruta')
        status = request.POST.get('status')

        try:
            Categoria.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                portada=portada,
                ruta=ruta,
                status=status
            )
            return JsonResponse({'title':'Exito','message': 'Categoría creada exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al crear la categoría: ' + str(e), 'type': 'danger'}, status=400)
    return render(request, 'categoria/categoria.html')

def categoria_update(request):
    if request.method == "POST":
        idcategoria = request.POST.get('categoriaId')
        categoria = get_object_or_404(Categoria, idcategoria=idcategoria)
        categoria.nombre = request.POST.get('nombre')
        categoria.descripcion = request.POST.get('descripcion')
        categoria.portada = request.POST.get('portada')
        categoria.ruta = request.POST.get('ruta')
        categoria.status = request.POST.get('status')

        try:
            categoria.save()
            return JsonResponse({'title':'Exito','message': 'Categoría actualizada exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al actualizar la categoría: ' + str(e), 'type': 'danger'}, status=400)

def categoria_detail(request):
    idcategoria = request.GET.get('id')
    categoria = get_object_or_404(Categoria, idcategoria=idcategoria)
    data = {
        'idcategoria': categoria.idcategoria,
        'nombre': categoria.nombre,
        'descripcion': categoria.descripcion,
        'portada': categoria.portada,
        'ruta': categoria.ruta,
        'status': categoria.status,
    }
    return JsonResponse(data)

def categoria_delete(request):
    if request.method == "POST":
        idcategoria = request.POST.get('id')
        try:
            categoria = get_object_or_404(Categoria, idcategoria=idcategoria)
            categoria.delete()
            return JsonResponse({'title':'Exito','message': 'Categoría eliminada exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al eliminar la categoría: ' + str(e), 'type': 'danger'}, status=400)
        

def productos(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        productos = Producto.objects.all()
        html = render_to_string('producto/partials/producto_list.html', {'productos': productos})
        return JsonResponse({'html': html})
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'producto/producto.html', {'productos': productos, 'categorias': categorias})

def producto_create(request):
    if request.method == "POST":
        categoriaid = request.POST.get('categoriaid')
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        imagen = request.POST.get('imagen')
        ruta = request.POST.get('ruta')
        status = request.POST.get('status')

        try:
            Producto.objects.create(
                categoriaid_id=categoriaid,
                codigo=codigo,
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                stock=stock,
                imagen=imagen,
                ruta=ruta,
                status=status
            )
            return JsonResponse({'title':'Exito','message': 'Producto creado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al crear el producto: ' + str(e), 'type': 'danger'}, status=400)
    return render(request, 'producto/producto.html')

def producto_update(request):
    if request.method == "POST":
        idproducto = request.POST.get('productoId')
        producto = get_object_or_404(Producto, idproducto=idproducto)
        producto.categoriaid_id = request.POST.get('categoriaid')
        producto.codigo = request.POST.get('codigo')
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.imagen = request.POST.get('imagen')
        producto.ruta = request.POST.get('ruta')
        producto.status = request.POST.get('status')

        try:
            producto.save()
            return JsonResponse({'title':'Exito','message': 'Producto actualizado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al actualizar el producto: ' + str(e), 'type': 'danger'}, status=400)

def producto_detail(request):
    idproducto = request.GET.get('id')
    producto = get_object_or_404(Producto, idproducto=idproducto)
    data = {
        'idproducto': producto.idproducto,
        'categoriaid': producto.categoriaid_id,
        'codigo': producto.codigo,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'precio': producto.precio,
        'stock': producto.stock,
        'imagen': producto.imagen,
        'ruta': producto.ruta,
        'status': producto.status,
    }
    return JsonResponse(data)

def producto_delete(request):
    if request.method == "POST":
        idproducto = request.POST.get('id')
        try:
            producto = get_object_or_404(Producto, idproducto=idproducto)
            producto.delete()
            return JsonResponse({'title':'Exito','message': 'Producto eliminado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al eliminar el producto: ' + str(e), 'type': 'danger'}, status=400)
        

def imagenes(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        imagenes = Imagen.objects.all()
        html = render_to_string('imagen/partials/imagen_list.html', {'imagenes': imagenes})
        return JsonResponse({'html': html})
    imagenes = Imagen.objects.all()
    productos = Producto.objects.all()
    return render(request, 'imagen/imagen.html', {'imagenes': imagenes, 'productos': productos})

def imagen_create(request):
    if request.method == "POST":
        productoid = request.POST.get('productoid')
        img = request.FILES.get('img')

        try:
            Imagen.objects.create(
                productoid_id=productoid,
                img=img
            )
            return JsonResponse({'title':'Exito','message': 'Imagen creada exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al crear la imagen: ' + str(e), 'type': 'danger'}, status=400)
    return render(request, 'imagen/imagen.html')

def imagen_update(request):
    if request.method == "POST":
        id = request.POST.get('imagenId')
        imagen = get_object_or_404(Imagen, id=id)
        imagen.productoid_id = request.POST.get('productoid')
        if 'img' in request.FILES:
            imagen.img = request.FILES['img']

        try:
            imagen.save()
            return JsonResponse({'title':'Exito','message': 'Imagen actualizada exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al actualizar la imagen: ' + str(e), 'type': 'danger'}, status=400)

def imagen_detail(request):
    id = request.GET.get('id')
    imagen = get_object_or_404(Imagen, id=id)
    data = {
        'id': imagen.id,
        'productoid': imagen.productoid_id,
        'img': imagen.img.url if imagen.img else '',
    }
    return JsonResponse(data)

def imagen_delete(request):
    if request.method == "POST":
        id = request.POST.get('id')
        try:
            imagen = get_object_or_404(Imagen, id=id)
            imagen.delete()
            return JsonResponse({'title':'Exito','message': 'Imagen eliminada exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al eliminar la imagen: ' + str(e), 'type': 'danger'}, status=400)
        
def tipopagos(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        tipopagos = Tipopago.objects.all()
        html = render_to_string('tipopago/partials/tipopago_list.html', {'tipopagos': tipopagos})
        return JsonResponse({'html': html})
    tipopagos = Tipopago.objects.all()
    return render(request, 'tipopago/tipopago.html', {'tipopagos': tipopagos})

def tipopago_create(request):
    if request.method == "POST":
        tipopago = request.POST.get('tipopago')
        status = request.POST.get('status')

        try:
            Tipopago.objects.create(
                tipopago=tipopago,
                status=status
            )
            return JsonResponse({'title':'Exito','message': 'Tipo de pago creado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al crear el tipo de pago: ' + str(e), 'type': 'danger'}, status=400)
    return render(request, 'tipopago/tipopago.html')

def tipopago_update(request):
    if request.method == "POST":
        idtipopago = request.POST.get('tipopagoId')
        tipopago = get_object_or_404(Tipopago, idtipopago=idtipopago)
        tipopago.tipopago = request.POST.get('tipopago')
        tipopago.status = request.POST.get('status')

        try:
            tipopago.save()
            return JsonResponse({'title':'Exito','message': 'Tipo de pago actualizado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al actualizar el tipo de pago: ' + str(e), 'type': 'danger'}, status=400)

def tipopago_detail(request):
    idtipopago = request.GET.get('id')
    tipopago = get_object_or_404(Tipopago, idtipopago=idtipopago)
    data = {
        'idtipopago': tipopago.idtipopago,
        'tipopago': tipopago.tipopago,
        'status': tipopago.status,
    }
    return JsonResponse(data)

def tipopago_delete(request):
    if request.method == "POST":
        idtipopago = request.POST.get('id')
        try:
            tipopago = get_object_or_404(Tipopago, idtipopago=idtipopago)
            tipopago.delete()
            return JsonResponse({'title':'Exito','message': 'Tipo de pago eliminado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al eliminar el tipo de pago: ' + str(e), 'type': 'danger'}, status=400)