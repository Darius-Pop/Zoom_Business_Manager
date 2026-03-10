# ════════════════════════════════════════════
# comenzi/views.py
# ════════════════════════════════════════════
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Comanda


class ComenziListView(LoginRequiredMixin, ListView):
    model = Comanda
    template_name = 'comenzi/comenzi_list.html'
    context_object_name = 'comenzi'
    login_url = '/login/'


class ComandaCreateView(LoginRequiredMixin, CreateView):
    model = Comanda
    template_name = 'comenzi/comanda_form.html'
    fields = ['numar', 'client', 'descriere', 'status', 'data_livrare', 'valoare']
    success_url = reverse_lazy('comenzi')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Comandă adăugată cu succes!')
        return super().form_valid(form)


class ComandaUpdateView(LoginRequiredMixin, UpdateView):
    model = Comanda
    template_name = 'comenzi/comanda_form.html'
    fields = ['numar', 'client', 'descriere', 'status', 'data_livrare', 'valoare']
    success_url = reverse_lazy('comenzi')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Comandă actualizată cu succes!')
        return super().form_valid(form)


class ComandaDeleteView(LoginRequiredMixin, DeleteView):
    model = Comanda
    template_name = 'comenzi/comanda_confirm_delete.html'
    success_url = reverse_lazy('comenzi')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Comandă ștearsă cu succes!')
        return super().form_valid(form)