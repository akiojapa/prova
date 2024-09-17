from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Computador, Periferico, ComputadorForm, PerifericoForm


def index(request):
    computadores = Computador.objects.all()
    context = {"computador_lista": computadores}
    return render(request, "core/index.html", context)

def computador(request):
    computadores = Computador.objects.all()
    context = {"computador_lista": computadores}
    return render(request, "core/index.html", context)

def criar_computador(request):
    if request.method == 'POST':
        form = ComputadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = ComputadorForm()
    return render(request, 'core/criar_computadores.html', {'form': form})

def editar_computador(request, id):
    computador = Computador.objects.get(pk=id)
    form = ComputadorForm(request.POST or None, instance=computador)
    if form.is_valid():
        form.save()
        return redirect('core:index')
    return render(request, 'core/criar_computadores.html', {'form': form})

def deletar_computador(request, id):
    computador = Computador.objects.get(pk=id)
    computador.delete()
    return redirect('core:index')

def periferico(request):
    perifericos = Periferico.objects.select_related('computador').all()
    context = {"periferico_lista": perifericos}
    return render(request, "core/perifericos.html", context)


def criar_periferico(request):
    if request.method == 'POST':
        form = PerifericoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = PerifericoForm()
    return render(request, 'core/criar_perifericos.html', {'form': form})

def editar_periferico(request, id):
    periferico = Periferico.objects.get(pk=id)
    form = PerifericoForm(request.POST or None, instance=periferico)
    if form.is_valid():
        form.save()
        return redirect('core:index')
    return render(request, 'core/criar_perifericos.html', {'form': form})

def deletar_periferico(request, id):
    periferico = Periferico.objects.get(pk=id)
    periferico.delete()
    return redirect('core:index')



