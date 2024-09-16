from rest_framework import serializers
from .models import Film
from realisateur.models import Realisateur

class FilmSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titre = serializers.CharField(max_lenght=150)
    description = serializers.CharField()
    date_sortie = serializers.DateField()
    realisateur_id = serializers.IntegerField(write_only=True)
    realisateur = serializers.CharField(read_only=True)

    def create(self, validated_data):
        realisateur = Realisateur.objects.get(id=validated_data['realisateur_id'])
        return Film.objects.create(realisateur=realisateur, **validated_data)
    

    def update(self, instance, validated_data):

        instance.titre = validated_data.get('titre', instance.titre)
        instance.description = validated_data.get('description', instance.description)
        instance.date_sortie = validated_data.get('date_sortie', instance.date_sortie)

        realisateur_id = validated_data('realisateur_id', None)
        if realisateur_id:
            instance.realisateur = Realisateur.objects.get(id=realisateur_id)

        instance.save()
        return instance
    

