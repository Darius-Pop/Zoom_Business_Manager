from django.db import models

class Client(models.Model):
    nume      = models.CharField(max_length=200)
    email     = models.EmailField(blank=True)
    telefon   = models.CharField(max_length=20, blank=True)
    adresa    = models.TextField(blank=True)
    cui       = models.CharField(max_length=20, blank=True, verbose_name="CUI")
    activ     = models.BooleanField(default=True)
    creat_la  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nume

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clienti"
        ordering = ['nume']