from rest_framework import serializers
from .models import Film
from realisateur.models import Realisateur

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    # Champ pour afficher le lien hypertexte vers le détail du réalisateur
    realisateur = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='realisateur-detail'
    )
    # Champ pour spécifier l'ID du réalisateur lors de la création ou de la mise à jour
    realisateur_id = serializers.PrimaryKeyRelatedField(
        queryset=Realisateur.objects.all(), source='realisateur'
    )

    class Meta:
        model = Film
        # Champs à inclure dans la sérialisation
        fields = ['url', 'id', 'titre', 'description', 'date_sortie', 'realisateur', 'realisateur_id']
