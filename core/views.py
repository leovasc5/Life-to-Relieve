from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404, JsonResponse

def login_user(request):
    return render(request, 'login.html')

def register_user(request):
    return render(request, 'register.html')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario).order_by('data_evento')
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
        return redirect('/login')

def submit_register(request):
    if request.POST:
        if request.POST.get('password') != request.POST.get('password2'):
            messages.error(request, "As senhas devem ser iguais!")
            return redirect('/register')
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            query = User.objects.get(username=username)
            messages.error(request, "O username já está sendo usado!")
            return redirect('/register')
        except:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Conta criada com sucesso!")
            return redirect('/login')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        local_evento = request.POST.get('local_evento')
        descricao = request.POST.get('descricao')
        id_evento = request.POST.get('id_evento')
        usuario = request.user
        if id_evento:
            Evento.objects.filter(id=id_evento).update(
                titulo=titulo,
                data_evento=data_evento,
                local_evento=local_evento,
                descricao=descricao,
            )
        else:
            Evento.objects.create(
                titulo=titulo,
                data_evento=data_evento,
                local_evento=local_evento,
                descricao=descricao,
                usuario=usuario
            )

    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

@login_required(login_url='/login/')
def json_lista_evento(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    return JsonResponse(list(evento), safe=False)