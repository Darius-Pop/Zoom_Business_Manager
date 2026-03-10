# ════════════════════════════════════════════
# clienti/views.py
# ════════════════════════════════════════════
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Client


class ClientiListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clienti/clienti_list.html'
    context_object_name = 'clienti'
    login_url = '/login/'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'clienti/client_form.html'
    fields = ['nume', 'email', 'telefon', 'adresa', 'cui', 'activ']
    success_url = reverse_lazy('clienti')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Client adăugat cu succes!')
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = 'clienti/client_form.html'
    fields = ['nume', 'email', 'telefon', 'adresa', 'cui', 'activ']
    success_url = reverse_lazy('clienti')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Client actualizat cu succes!')
        return super().form_valid(form)


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'clienti/client_confirm_delete.html'
    success_url = reverse_lazy('clienti')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Client șters cu succes!')
        return super().form_valid(form)
