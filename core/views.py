from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def local(request, titulo_evento):
    objeto = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('<h1>Titulo: {}</h1>'.format(objeto.descricao))

def login_user(request):
    return render(request, 'login.html')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido!")
        return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')