from django.db import models
from django.utils import timezone
from realisateur.models import Realisateur

# Modèle représentant un film
class Film(models.Model):
    # Titre du film
    titre = models.CharField(max_length=150)
    # Description du film
    description = models.TextField()
    # Date de sortie du film, par défaut la date actuelle
    date_sortie = models.DateField(default=timezone.now)
    # Référence au réalisateur du film (clé étrangère)
    realisateur = models.ForeignKey(Realisateur, on_delete=models.RESTRICT)

    def __str__(self):
        # Représentation en chaîne de caractères du film
        return f'{self.titre} ({self.date_sortie})'