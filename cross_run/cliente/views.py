<<<<<<< HEAD
from tracemalloc import get_object_traceback
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic

from .models import Cliente

class IndexView(generic.ListView):
    template_name = 'cliente/index.html'
    context_objects_name = 'ultimos_usuarios'

    def get_queryset(self):
        return Cliente.objects.all()

'''
    ultimos_usuarios = Cliente.objects.all
    template = loader.get_template('cliente/index.html')
    context = {
        'ultimos_usuarios': ultimos_usuarios
    }
    return render(request, 'cliente/index.html', context)
'''


class DetailView(generic.DetailView):
    model = Cliente
    template_name = 'cliente/detail.html'

'''
    cliente = get_object_or_404 (Cliente, id=id)
    return render(request, 'cliente/detail.html', {'cliente': cliente})
'''


class ResultadoView(generic.DetailView):
    model = Cliente
    template_name = 'cliente/resultado.html'

''''
    response = "Estas viendo la funcion de resultado %s"
    return HttpResponse(response % id)
'''
=======
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Iniciando mi primer clase del proyecto .-.")
>>>>>>> parent of 0a3799a (Modelos de clases para base de datos)
