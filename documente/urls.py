from django.urls import path
from . import views

urlpatterns = [
    path('',               views.DocumenteListView.as_view(),  name='documente'),
    path('adauga/',        views.DocumentCreateView.as_view(), name='document_adauga'),
    path('<int:pk>/edit/', views.DocumentUpdateView.as_view(), name='document_edit'),
    path('<int:pk>/del/',  views.DocumentDeleteView.as_view(), name='document_delete'),
]