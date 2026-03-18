from django.urls import path
from . import views

urlpatterns = [
    path('',               views.OfertareListView.as_view(),  name='ofertare'),
    path('adauga/',        views.OfertaCreateView.as_view(),  name='oferta_adauga'),
    path('<int:pk>/edit/', views.OfertaUpdateView.as_view(),  name='oferta_edit'),
    path('<int:pk>/del/',  views.OfertaDeleteView.as_view(),  name='oferta_delete'),
    path('trimite/<int:pk>/', views.trimite_oferta_email, name='trimite_oferta_email'),
]