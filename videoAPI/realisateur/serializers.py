from rest_framework import serializers
from .models import Realisateur


class RealisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realisateur
        fields = '__all__'


# class RealisateurSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     nom = serializers.CharField(max_length=100)
#     prenom = serializers.CharField(max_length=100)
#     date_naissance = serializers.DateField(required=False, allow_null=True)


#     def create(self, validated_data):
#         return Realisateur.objects.create(**validated_data)
    

#     def update(self, instance, validated_data):
#         instance.nom = validated_data.get('nom', instance.nom)
#         instance.prenom = validated_data.get('prenom', instance.prenom)
#         instance.date_naissance = validated_data.get('date_naissance', instance.date_naissance)

#         instance.save()
#         return instance
    
