from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Angajat


class AngajatiListView(LoginRequiredMixin, ListView):
    model = Angajat
    template_name = 'angajati/angajati_list.html'
    context_object_name = 'angajati'
    login_url = '/login/'


class AngajatCreateView(LoginRequiredMixin, CreateView):
    model = Angajat
    template_name = 'angajati/angajat_form.html'
    fields = ['nume', 'prenume', 'email', 'telefon', 'functie', 'departament', 'data_angajare', 'activ']
    success_url = reverse_lazy('angajati')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Angajat adăugat cu succes!')
        return super().form_valid(form)


class AngajatUpdateView(LoginRequiredMixin, UpdateView):
    model = Angajat
    template_name = 'angajati/angajat_form.html'
    fields = ['nume', 'prenume', 'email', 'telefon', 'functie', 'departament', 'data_angajare', 'activ']
    success_url = reverse_lazy('angajati')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Angajat actualizat cu succes!')
        return super().form_valid(form)


class AngajatDeleteView(LoginRequiredMixin, DeleteView):
    model = Angajat
    template_name = 'angajati/angajat_confirm_delete.html'
    success_url = reverse_lazy('angajati')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Angajat șters cu succes!')
        return super().form_valid(form)