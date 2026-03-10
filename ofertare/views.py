# ════════════════════════════════════════════
# ofertare/views.py
# ════════════════════════════════════════════
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Oferta


class OfertareListView(LoginRequiredMixin, ListView):
    model = Oferta
    template_name = 'ofertare/ofertare_list.html'
    context_object_name = 'oferte'
    login_url = '/login/'


class OfertaCreateView(LoginRequiredMixin, CreateView):
    model = Oferta
    template_name = 'ofertare/oferta_form.html'
    fields = ['numar', 'client', 'descriere', 'status', 'valoare', 'valabila_pana']
    success_url = reverse_lazy('ofertare')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Ofertă adăugată cu succes!')
        return super().form_valid(form)


class OfertaUpdateView(LoginRequiredMixin, UpdateView):
    model = Oferta
    template_name = 'ofertare/oferta_form.html'
    fields = ['numar', 'client', 'descriere', 'status', 'valoare', 'valabila_pana']
    success_url = reverse_lazy('ofertare')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Ofertă actualizată cu succes!')
        return super().form_valid(form)


class OfertaDeleteView(LoginRequiredMixin, DeleteView):
    model = Oferta
    template_name = 'ofertare/oferta_confirm_delete.html'
    success_url = reverse_lazy('ofertare')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Ofertă ștearsă cu succes!')
        return super().form_valid(form)