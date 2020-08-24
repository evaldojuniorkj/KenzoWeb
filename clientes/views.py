from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Pessoa

# Create your views here.

def index(request):
    return print('OláMundo')

def listarCliente(request, tempate_name='listarCliente.html'):
    clientes = Pessoa.objects.all()
    return render(request, tempate_name, {'clientes': clientes})

def novoCliente(request, template_name = './clienteNovo.html'):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listarCliente')
    return render(request,template_name,{'form': form})

def editarCliente(request, pk, template_name='editarCliente.html'):
    cliente = get_object_or_404(Pessoa,pk = pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()
            return redirect('listarCliente')
    else:
        form = ClienteForm( instance=cliente )
    return render(request, template_name, {'form': form})

def removerCliente(request, pk):
    cliente = Pessoa.objects.get(pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('listarCliente')
    return render(request, 'removerCliente.html', {'cliente': cliente})