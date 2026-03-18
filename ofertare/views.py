from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Oferta

# --- View-ul nou pentru butonul de trimitere ---
def trimite_oferta_email(request, pk):
    oferta = get_object_or_404(Oferta, pk=pk)
    
    # Verificăm dacă clientul are email
    email_destinatar = getattr(oferta.client, 'email', None)
    
    if not email_destinatar:
        messages.error(request, f"Clientul {oferta.client} nu are o adresă de email validă!")
        return redirect('ofertare')

    try:
        subject = f"Ofertă nouă: {oferta.numar}"
        message = (
            f"Bună ziua, {oferta.client}\n\n"
            f"Vă transmitem oferta nr. {oferta.numar}.\n"
            f"Valoare: {oferta.valoare} RON\n"
            f"Valabilitate: până la {oferta.valabila_pana}\n\n"
            "Vă mulțumim!"
        )
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email_destinatar],
            fail_silently=False,
        )
        
        # Opțional: Marcăm oferta ca trimisă în baza de date
        oferta.status = 'trimisa'
        oferta.save()
        
        messages.success(request, f"Oferta {oferta.numar} a fost trimisă cu succes către {email_destinatar}!")
    except Exception as e:
        messages.error(request, f"Eroare la trimitere email: {e}")

    return redirect('ofertare')

# --- View-urile existente (curățate) ---

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
        messages.success(self.request, 'Ofertă creată cu succes! Acum o poți trimite prin email.')
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