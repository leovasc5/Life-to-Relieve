from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

def local(request, titulo_evento):
    objeto = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('<h1>Titulo: {}</h1>'.format(objeto.descricao))

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)
