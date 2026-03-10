from django.urls import path
from . import views

urlpatterns = [
    path('',               views.ClientiListView.as_view(),  name='clienti'),
    path('adauga/',        views.ClientCreateView.as_view(), name='client_adauga'),
    path('<int:pk>/edit/', views.ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/del/',  views.ClientDeleteView.as_view(), name='client_delete'),
]