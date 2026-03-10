from django.db import models

class Angajat(models.Model):
    nume        = models.CharField(max_length=100)
    prenume     = models.CharField(max_length=100)
    email       = models.EmailField(unique=True)
    telefon     = models.CharField(max_length=20, blank=True)
    functie     = models.CharField(max_length=100)
    departament = models.CharField(max_length=100, blank=True)
    data_angajare = models.DateField()
    activ       = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.prenume} {self.nume}"

    class Meta:
        verbose_name = "Angajat"
        verbose_name_plural = "Angajati"
        ordering = ['nume']