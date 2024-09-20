from .models import Film
from .serializers import FilmSerializer
from rest_framework import viewsets

class FilmViewSet(viewsets.ModelViewSet):
    # VueSet pour gérer les opérations CRUD sur les films
    queryset = Film.objects.all()
    # Utilisation du sérialiseur défini précédemment
    serializer_class = FilmSerializer
