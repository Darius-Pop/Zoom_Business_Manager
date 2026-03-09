from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login/',    views.login_view,    name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/',   views.logout_view,   name='logout'),

    # Pagini principale
    path('',           views.home,      name='home'),
    path('angajati/',  views.angajati,  name='angajati'),
    path('documente/', views.documente, name='documente'),
    path('clienti/',   views.clienti,   name='clienti'),
    path('comenzi/',   views.comenzi,   name='comenzi'),
    path('ofertare/',  views.ofertare,  name='ofertare'),
]
