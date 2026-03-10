from django.urls import path
from . import views

urlpatterns = [
    path('',              views.AngajatiListView.as_view(),  name='angajati'),
    path('adauga/',       views.AngajatCreateView.as_view(), name='angajat_adauga'),
    path('<int:pk>/edit/',views.AngajatUpdateView.as_view(), name='angajat_edit'),
    path('<int:pk>/del/', views.AngajatDeleteView.as_view(), name='angajat_delete'),
]