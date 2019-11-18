from django.shortcuts import render
from django.contrib import messages
from .forms import GradoForm
from alumnos.models import Grado, Pensum
# Create your views here.

def listar_grado(request):
	pubs = Grado.objects.all()
	return render(request,'alumnos/listar_grado.html', {'pubs': pubs})

def grado_nuevo(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'], descripcion = formulario.cleaned_data['descripcion'])
            for materia_id in request.POST.getlist('materias'):
                pensum = Pensum(materia_id=materia_id, grado_id = grado.id)
                pensum.save()
            messages.add_message(request, messages.SUCCESS, 'Grado guardado')
    else:
        formulario = GradoForm()
    return render(request, 'alumnos/grado_editar.html', {'formulario': formulario})