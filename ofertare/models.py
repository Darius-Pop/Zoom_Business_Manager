from django.db import models
from clienti.models import Client

class Oferta(models.Model):
    STATUS_CHOICES = [
        ('draft',      'Draft'),
        ('trimisa',    'Trimisă'),
        ('acceptata',  'Acceptată'),
        ('refuzata',   'Refuzată'),
    ]
    numar        = models.CharField(max_length=50, unique=True)
    client       = models.ForeignKey(Client, on_delete=models.CASCADE)
    descriere    = models.TextField(blank=True)
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    data_oferta  = models.DateField(auto_now_add=True)
    valoare      = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valabila_pana = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.numar} — {self.client}"

    class Meta:
        verbose_name = "Oferta"
        verbose_name_plural = "Oferte"
        ordering = ['-data_oferta']