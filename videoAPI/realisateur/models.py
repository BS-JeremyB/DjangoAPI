from django.db import models

# Create your models here.

class Realisateur (models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.prenom} {self.nom}'