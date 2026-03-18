from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta


# ── Autentificare ──────────────────────────────────────
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Utilizator sau parolă incorecte.')

    return render(request, 'registration/login.html')


# ── Înregistrare ───────────────────────────────────────
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name  = request.POST.get('last_name', '').strip()
        username   = request.POST.get('username', '').strip()
        email      = request.POST.get('email', '').strip()
        password1  = request.POST.get('password1', '')
        password2  = request.POST.get('password2', '')

        errors = []
        if not username:
            errors.append('Numele de utilizator este obligatoriu.')
        if User.objects.filter(username=username).exists():
            errors.append('Acest nume de utilizator există deja.')
        if User.objects.filter(email=email).exists():
            errors.append('Acest email este deja înregistrat.')
        if len(password1) < 8:
            errors.append('Parola trebuie să aibă minim 8 caractere.')
        if password1 != password2:
            errors.append('Parolele nu se potrivesc.')

        if errors:
            for err in errors:
                messages.error(request, err)
            return render(request, 'registration/register.html', {
                'form': request.POST
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name,
        )
        login(request, user)
        messages.success(request, f'Bine ai venit, {user.first_name or user.username}!')
        return redirect('home')

    return render(request, 'registration/register.html', {'form': {}})


# ── Deconectare ────────────────────────────────────────
def logout_view(request):
    logout(request)
    return redirect('login')


# ── Homepage ───────────────────────────────────────────
@login_required(login_url='login')
def home(request):
    from angajati.models import Angajat
    from documente.models import Document
    from clienti.models import Client
    from comenzi.models import Comanda
    from ofertare.models import Oferta

    azi = timezone.now().date()
    peste_30_zile = azi + timedelta(days=30)

    # Documente expirate deja SAU care expira in urmatoarele 30 zile
    documente_expirare = Document.objects.filter(
        data_expirare__lte=peste_30_zile
    ).order_by('data_expirare')

    # Comenzi cu livrare in curand (doar cele nefinalizate)
    comenzi_livrare = Comanda.objects.filter(
        data_livrare__lte=peste_30_zile,
        data_livrare__gte=azi,
        status__in=['noua', 'in_lucru']
    ).order_by('data_livrare')

    context = {
        'total_angajati':     Angajat.objects.count(),
        'total_documente':    Document.objects.count(),
        'total_clienti':      Client.objects.filter(activ=True).count(),
        'total_comenzi':      Comanda.objects.filter(status__in=['noua', 'in_lucru']).count(),
        'total_oferte':       Oferta.objects.count(),
        'documente_expirare': documente_expirare,
        'comenzi_livrare':    comenzi_livrare,
        'notificari_urgente': [],
    }
    return render(request, 'home/homepage.html', context)