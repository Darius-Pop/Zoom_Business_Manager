from django.urls import path
from . import views

urlpatterns = [
    path('',               views.ComenziListView.as_view(),   name='comenzi'),
    path('adauga/',        views.ComandaCreateView.as_view(), name='comanda_adauga'),
    path('<int:pk>/edit/', views.ComandaUpdateView.as_view(), name='comanda_edit'),
    path('<int:pk>/del/',  views.ComandaDeleteView.as_view(), name='comanda_delete'),
]