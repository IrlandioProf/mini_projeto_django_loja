from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente

class ClienteList(ListView):
    model = Cliente
    paginate_by = 20
    template_name = 'clientes/lista.html'

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone']
    success_url = reverse_lazy('clientes:lista')
    template_name = 'clientes/form.html'

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone']
    success_url = reverse_lazy('clientes:lista')
    template_name = 'clientes/form.html'

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes:lista')
    template_name = 'clientes/confirma_exclusao.html'
