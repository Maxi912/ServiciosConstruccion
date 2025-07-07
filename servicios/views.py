from django.shortcuts import render, redirect
from .models import Servicio
from .forms import ServicioForm
from django.contrib.auth.decorators import login_required

def lista_servicios(request):
    servicios = Servicio.objects.all().order_by('-fecha_creacion')
    return render(request, 'servicios/lista.html', {'servicios': servicios})

@login_required
def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.autor = request.user
            servicio.save()
            return redirect('lista_servicios')
    else:
        form = ServicioForm()
    return render(request, 'servicios/crear.html', {'form': form})