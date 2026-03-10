from django.db import models
from clienti.models import Client

class Comanda(models.Model):
    STATUS_CHOICES = [
        ('noua',      'Nouă'),
        ('in_lucru',  'În lucru'),
        ('finalizata','Finalizată'),
        ('anulata',   'Anulată'),
    ]
    numar         = models.CharField(max_length=50, unique=True)
    client        = models.ForeignKey(Client, on_delete=models.CASCADE)
    descriere     = models.TextField(blank=True)
    status        = models.CharField(max_length=20, choices=STATUS_CHOICES, default='noua')
    data_comanda  = models.DateField(auto_now_add=True)
    data_livrare  = models.DateField(null=True, blank=True)
    valoare       = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.numar} — {self.client}"

    class Meta:
        verbose_name = "Comanda"
        verbose_name_plural = "Comenzi"
        ordering = ['-data_comanda']