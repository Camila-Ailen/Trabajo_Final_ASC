from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from .models import Cliente


def index(request):
    return HttpResponse("Iniciando mi primer clase del proyecto .-.")

def detail(request, id):    
    return HttpResponse("Estas viendo el id de un cliente %s" % id)

def resultado(request, id):
    response = "Estas viendo la funcion de resultado %s"
    return HttpResponse(response % id)

'''def index(request):
    ultimos = Cliente.objects.order_by('-pub_date')[:2]
    template = loader.get_template('cliente/index.html')
    context = {
        'ultimos': ultimos
    }
    # output = ', '.join([q.nombre_text for q in ultimos])
    # return HttpResponse(template.render(context, request))
    return render(request, 'cliente/index.html', context)
    '''