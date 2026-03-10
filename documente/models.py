from django.db import models
from angajati.models import Angajat

class Document(models.Model):
    TIP_CHOICES = [
        ('contract', 'Contract'),
        ('revizie',  'Revizie medicală'),
        ('autorizatie', 'Autorizație'),
        ('alt', 'Altul'),
    ]
    nume          = models.CharField(max_length=200)
    tip           = models.CharField(max_length=50, choices=TIP_CHOICES)
    angajat       = models.ForeignKey(Angajat, on_delete=models.SET_NULL, null=True, blank=True)
    data_emitere  = models.DateField()
    data_expirare = models.DateField(null=True, blank=True)
    fisier        = models.FileField(upload_to='documente/', blank=True)
    observatii    = models.TextField(blank=True)

    def __str__(self):
        return self.nume

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documente"
        ordering = ['data_expirare']
