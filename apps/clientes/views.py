from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
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


class HomeView(TemplateView):
    """Página inicial que mostra os últimos clientes adicionados.

    Usa TemplateView e injeta `ultimos_clientes` no contexto com os 5
    clientes mais recentes (ordenados por id decrescente).
    """
    template_name = 'clientes/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Importa localmente para evitar problemas de import cycle em tempo de carregamento
        from .models import Cliente
        context['ultimos_clientes'] = Cliente.objects.order_by('-id')[:5]
        return context
