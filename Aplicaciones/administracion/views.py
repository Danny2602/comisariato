from django.shortcuts import render,get_object_or_404
from .models import Categoria, DetallePedido, Imagen, Pedido, Persona,Producto, Rol, Tipopago
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
        
def roles(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        roles = Rol.objects.all()
        html = render_to_string('rol/partials/rol_list.html', {'roles': roles})
        return JsonResponse({'html': html})
    roles = Rol.objects.all()
    return render(request, 'rol/rol.html', {'roles': roles})

def rol_create(request):
    if request.method == "POST":
        nombrerol = request.POST.get('nombrerol')
        descripcion = request.POST.get('descripcion')
        status = request.POST.get('status')

        try:
            Rol.objects.create(
                nombrerol=nombrerol,
                descripcion=descripcion,
                status=status
            )
            return JsonResponse({'title':'Exito','message': 'Rol creado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al crear el rol: ' + str(e), 'type': 'danger'}, status=400)
    return render(request, 'rol/rol.html')

def rol_update(request):
    if request.method == "POST":
        idrol = request.POST.get('rolId')
        rol = get_object_or_404(Rol, idrol=idrol)
        rol.nombrerol = request.POST.get('nombrerol')
        rol.descripcion = request.POST.get('descripcion')
        rol.status = request.POST.get('status')

        try:
            rol.save()
            return JsonResponse({'title':'Exito','message': 'Rol actualizado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al actualizar el rol: ' + str(e), 'type': 'danger'}, status=400)

def rol_detail(request):
    idrol = request.GET.get('id')
    rol = get_object_or_404(Rol, idrol=idrol)
    data = {
        'idrol': rol.idrol,
        'nombrerol': rol.nombrerol,
        'descripcion': rol.descripcion,
        'status': rol.status,
    }
    return JsonResponse(data)

def rol_delete(request):
    if request.method == "POST":
        idrol = request.POST.get('id')
        try:
            rol = get_object_or_404(Rol, idrol=idrol)
            rol.delete()
            return JsonResponse({'title':'Exito','message': 'Rol eliminado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al eliminar el rol: ' + str(e), 'type': 'danger'}, status=400)
        
def personas(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        personas = Persona.objects.all()
        html = render_to_string('persona/partials/persona_list.html', {'personas': personas})
        return JsonResponse({'html': html})
    personas = Persona.objects.all()
    roles = Rol.objects.all()
    return render(request, 'persona/persona.html', {'personas': personas, 'roles': roles})

def persona_create(request):
    if request.method == "POST":
        identificacion = request.POST.get('identificacion')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        telefono = request.POST.get('telefono')
        email_user = request.POST.get('email_user')
        password = request.POST.get('password')
        nit = request.POST.get('nit')
        nombrefiscal = request.POST.get('nombrefiscal')
        direccionfiscal = request.POST.get('direccionfiscal')
        token = request.POST.get('token')
        rolid = request.POST.get('rolid')
        status = request.POST.get('status')

        try:
            Persona.objects.create(
                identificacion=identificacion,
                nombres=nombres,
                apellidos=apellidos,
                telefono=telefono,
                email_user=email_user,
                password=password,
                nit=nit,
                nombrefiscal=nombrefiscal,
                direccionfiscal=direccionfiscal,
                token=token,
                rolid_id=rolid,
                status=status
            )
            return JsonResponse({'title':'Exito','message': 'Persona creada exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al crear la persona: ' + str(e), 'type': 'danger'}, status=400)
    return render(request, 'persona/persona.html')

def persona_update(request):
    if request.method == "POST":
        idpersona = request.POST.get('personaId')
        persona = get_object_or_404(Persona, idpersona=idpersona)
        persona.identificacion = request.POST.get('identificacion')
        persona.nombres = request.POST.get('nombres')
        persona.apellidos = request.POST.get('apellidos')
        persona.telefono = request.POST.get('telefono')
        persona.email_user = request.POST.get('email_user')
        persona.password = request.POST.get('password')
        persona.nit = request.POST.get('nit')
        persona.nombrefiscal = request.POST.get('nombrefiscal')
        persona.direccionfiscal = request.POST.get('direccionfiscal')
        persona.token = request.POST.get('token')
        persona.rolid_id = request.POST.get('rolid')
        persona.status = request.POST.get('status')

        try:
            persona.save()
            return JsonResponse({'title':'Exito','message': 'Persona actualizada exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al actualizar la persona: ' + str(e), 'type': 'danger'}, status=400)

def persona_detail(request):
    idpersona = request.GET.get('id')
    persona = get_object_or_404(Persona, idpersona=idpersona)
    data = {
        'idpersona': persona.idpersona,
        'identificacion': persona.identificacion,
        'nombres': persona.nombres,
        'apellidos': persona.apellidos,
        'telefono': persona.telefono,
        'email_user': persona.email_user,
        'password': persona.password,
        'nit': persona.nit,
        'nombrefiscal': persona.nombrefiscal,
        'direccionfiscal': persona.direccionfiscal,
        'token': persona.token,
        'rolid': persona.rolid_id,
        'status': persona.status,
    }
    return JsonResponse(data)

def persona_delete(request):
    if request.method == "POST":
        idpersona = request.POST.get('id')
        try:
            persona = get_object_or_404(Persona, idpersona=idpersona)
            persona.delete()
            return JsonResponse({'title':'Exito','message': 'Persona eliminada exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al eliminar la persona: ' + str(e), 'type': 'danger'}, status=400)
        
def pedidos(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        pedidos = Pedido.objects.all()
        html = render_to_string('pedido/partials/pedido_list.html', {'pedidos': pedidos})
        return JsonResponse({'html': html})
    pedidos = Pedido.objects.all()
    personas = Persona.objects.all()
    tipopagos = Tipopago.objects.all()
    return render(request, 'pedido/pedido.html', {'pedidos': pedidos, 'personas': personas, 'tipopagos': tipopagos})

def pedido_create(request):
    if request.method == "POST":
        personaid = request.POST.get('personaid')
        referenciacobro = request.POST.get('referenciacobro')
        idtransaccionpaypal = request.POST.get('idtransaccionpaypal')
        datospaypal = request.POST.get('datospaypal')
        fecha = request.POST.get('fecha')
        costo_envio = request.POST.get('costo_envio')
        monto = request.POST.get('monto')
        tipopagoid = request.POST.get('tipopagoid')
        direccion_envio = request.POST.get('direccion_envio')
        status = request.POST.get('status')

        try:
            Pedido.objects.create(
                personaid_id=personaid,
                referenciacobro=referenciacobro,
                idtransaccionpaypal=idtransaccionpaypal,
                datospaypal=datospaypal,
                fecha=fecha,
                costo_envio=costo_envio,
                monto=monto,
                tipopagoid_id=tipopagoid,
                direccion_envio=direccion_envio,
                status=status
            )
            return JsonResponse({'title':'Exito','message': 'Pedido creado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al crear el pedido: ' + str(e), 'type': 'danger'}, status=400)
    return render(request, 'pedido/pedido.html')

def pedido_update(request):
    if request.method == "POST":
        idpedido = request.POST.get('pedidoId')
        pedido = get_object_or_404(Pedido, idpedido=idpedido)
        pedido.personaid_id = request.POST.get('personaid')
        pedido.referenciacobro = request.POST.get('referenciacobro')
        pedido.idtransaccionpaypal = request.POST.get('idtransaccionpaypal')
        pedido.datospaypal = request.POST.get('datospaypal')
        pedido.fecha = request.POST.get('fecha')
        pedido.costo_envio = request.POST.get('costo_envio')
        pedido.monto = request.POST.get('monto')
        pedido.tipopagoid_id = request.POST.get('tipopagoid')
        pedido.direccion_envio = request.POST.get('direccion_envio')
        pedido.status = request.POST.get('status')

        try:
            pedido.save()
            return JsonResponse({'title':'Exito','message': 'Pedido actualizado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al actualizar el pedido: ' + str(e), 'type': 'danger'}, status=400)

def pedido_detail(request):
    idpedido = request.GET.get('id')
    pedido = get_object_or_404(Pedido, idpedido=idpedido)
    data = {
        'idpedido': pedido.idpedido,
        'personaid': pedido.personaid_id,
        'referenciacobro': pedido.referenciacobro,
        'idtransaccionpaypal': pedido.idtransaccionpaypal,
        'datospaypal': pedido.datospaypal,
        'fecha': pedido.fecha,
        'costo_envio': pedido.costo_envio,
        'monto': pedido.monto,
        'tipopagoid': pedido.tipopagoid_id,
        'direccion_envio': pedido.direccion_envio,
        'status': pedido.status,
    }
    return JsonResponse(data)

def pedido_delete(request):
    if request.method == "POST":
        idpedido = request.POST.get('id')
        try:
            pedido = get_object_or_404(Pedido, idpedido=idpedido)
            pedido.delete()
            return JsonResponse({'title':'Exito','message': 'Pedido eliminado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al eliminar el pedido: ' + str(e), 'type': 'danger'}, status=400)

def detalle_pedidos(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        detalle_pedidos = DetallePedido.objects.all()
        html = render_to_string('detalle_pedido/partials/detalle_pedido_list.html', {'detalle_pedidos': detalle_pedidos})
        return JsonResponse({'html': html})
    detalle_pedidos = DetallePedido.objects.all()
    pedidos = Pedido.objects.all()
    productos = Producto.objects.all()
    return render(request, 'detalle_pedido/detalle_pedido.html', {'detalle_pedidos': detalle_pedidos, 'pedidos': pedidos, 'productos': productos})

def detalle_pedido_create(request):
    if request.method == "POST":
        pedidoid = request.POST.get('pedidoid')
        productoid = request.POST.get('productoid')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')

        try:
            DetallePedido.objects.create(
                pedidoid_id=pedidoid,
                productoid_id=productoid,
                precio=precio,
                cantidad=cantidad
            )
            return JsonResponse({'title':'Exito','message': 'Detalle de pedido creado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al crear el detalle de pedido: ' + str(e), 'type': 'danger'}, status=400)
    return render(request, 'detalle_pedido/detalle_pedido.html')

def detalle_pedido_update(request):
    if request.method == "POST":
        id = request.POST.get('detallePedidoId')
        detalle_pedido = get_object_or_404(DetallePedido, id=id)
        detalle_pedido.pedidoid_id = request.POST.get('pedidoid')
        detalle_pedido.productoid_id = request.POST.get('productoid')
        detalle_pedido.precio = request.POST.get('precio')
        detalle_pedido.cantidad = request.POST.get('cantidad')

        try:
            detalle_pedido.save()
            return JsonResponse({'title':'Exito','message': 'Detalle de pedido actualizado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al actualizar el detalle de pedido: ' + str(e), 'type': 'danger'}, status=400)

def detalle_pedido_detail(request):
    id = request.GET.get('id')
    detalle_pedido = get_object_or_404(DetallePedido, id=id)
    data = {
        'id': detalle_pedido.id,
        'pedidoid': detalle_pedido.pedidoid_id,
        'productoid': detalle_pedido.productoid_id,
        'precio': detalle_pedido.precio,
        'cantidad': detalle_pedido.cantidad,
    }
    return JsonResponse(data)

def detalle_pedido_delete(request):
    if request.method == "POST":
        id = request.POST.get('id')
        try:
            detalle_pedido = get_object_or_404(DetallePedido, id=id)
            detalle_pedido.delete()
            return JsonResponse({'title':'Exito','message': 'Detalle de pedido eliminado exitosamente', 'type': 'success'})
        except Exception as e:
            return JsonResponse({'title':'Error','message': 'Error al eliminar el detalle de pedido: ' + str(e), 'type': 'danger'}, status=400)