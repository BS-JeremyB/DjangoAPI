from django.db import models

# Modèle représentant un réalisateur
class Realisateur(models.Model):
    # Nom de famille du réalisateur
    nom = models.CharField(max_length=100)
    # Prénom du réalisateur
    prenom = models.CharField(max_length=100)
    # Date de naissance du réalisateur (peut être nulle)
    date_naissance = models.DateField(blank=True, null=True)

    def __str__(self):
        # Représentation en chaîne de caractères du réalisateur
        return f'{self.prenom} {self.nom}'
