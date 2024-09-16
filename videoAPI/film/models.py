from django.db import models
from django.utils import timezone
from realisateur.models import Realisateur

# Create your models here.
class Film(models.Model):
    titre = models.CharField(max_length=150)
    description = models.TextField()
    date_sortie = models.DateField(default=timezone.now)
    realisateur = models.ForeignKey(Realisateur, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.titre} ({self.date_sortie})'