# ════════════════════════════════════════════
# documente/views.py
# ════════════════════════════════════════════
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Document


class DocumenteListView(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'documente/documente_list.html'
    context_object_name = 'documente'
    login_url = '/login/'


class DocumentCreateView(LoginRequiredMixin, CreateView):
    model = Document
    template_name = 'documente/document_form.html'
    fields = ['nume', 'tip', 'angajat', 'data_emitere', 'data_expirare', 'fisier', 'observatii']
    success_url = reverse_lazy('documente')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Document adăugat cu succes!')
        return super().form_valid(form)


class DocumentUpdateView(LoginRequiredMixin, UpdateView):
    model = Document
    template_name = 'documente/document_form.html'
    fields = ['nume', 'tip', 'angajat', 'data_emitere', 'data_expirare', 'fisier', 'observatii']
    success_url = reverse_lazy('documente')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Document actualizat cu succes!')
        return super().form_valid(form)


class DocumentDeleteView(LoginRequiredMixin, DeleteView):
    model = Document
    template_name = 'documente/document_confirm_delete.html'
    success_url = reverse_lazy('documente')
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, 'Document șters cu succes!')
        return super().form_valid(form)