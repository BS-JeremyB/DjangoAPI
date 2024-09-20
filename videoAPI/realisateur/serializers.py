from rest_framework import serializers
from .models import Realisateur

class RealisateurListSerializer(serializers.HyperlinkedModelSerializer):
    # Champ personnalisé pour afficher le nom complet
    nom_complet = serializers.SerializerMethodField()

    class Meta:
        model = Realisateur
        # Champs à inclure dans la sérialisation
        fields = ['url', 'nom_complet']

    def get_nom_complet(self, obj):
        # Méthode pour obtenir le nom complet du réalisateur
        return f"{obj.prenom} {obj.nom}"

class RealisateurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Realisateur
        # Inclure tous les champs du modèle
        fields = '__all__'
