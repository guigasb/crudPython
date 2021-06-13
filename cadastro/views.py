from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from cadastro.models import Meususer
from cadastro.forms import RegistroUsuario


#def homeView(request):
    #return HttpResponse("Hello World")


def CreateView(request):
    form = RegistroUsuario(request.POST)

    if form.is_valid(): #a views vai verificar se o formulário foi feito corretamente
        form.save() # o models vai salvar no banco
        return redirect("lista")

    return render(request, 'create.html', {'form':form})

def ReadView(request):

    nome = Meususer.objects.all()
    return render(request, 'read.html', {'nome': nome})



def UpdateView(request, id):
    nome = get_object_or_404(Meususer, pk=id)
    form = RegistroUsuario(request.POST or None, instance = nome)
    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'update.html', {'form': form})

def DeleteView(request, id):
    superman = get_object_or_404(Meususer, pk=id)
    if request.method == 'POST':
        superman.delete()
        return redirect('lista')
    return render(request, 'delete.html', {'superman': superman})

