from django.shortcuts import render,get_object_or_404
from .models import Categoria
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