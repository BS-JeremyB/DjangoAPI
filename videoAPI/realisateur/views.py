from .models import Realisateur
from .serializers import *
from videoAPI.permissions import IsAdminUser, IsAuthenticatedNoDelete, IsReadOnly
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class RealisateurViewSet(viewsets.ModelViewSet):
    # VueSet pour gérer les opérations CRUD sur les réalisateurs
    queryset = Realisateur.objects.all()
    # Définition des permissions d'accès
    permission_classes = [IsAdminUser | IsAuthenticatedNoDelete | IsReadOnly]
    # Ajout des fonctionnalités de filtrage et de tri
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Champs sur lesquels le filtrage est permis
    filterset_fields = ['nom', 'date_naissance']
    # Champs sur lesquels le tri est permis
    ordering_fields = ['nom', 'date_naissance']
    # Ordre de tri par défaut (par nom décroissant)
    ordering = ['-nom']

    def get_serializer_class(self):
        # Utiliser RealisateurListSerializer pour l'action 'list'
        if self.action == 'list':
            return RealisateurListSerializer
        # Utiliser RealisateurSerializer pour les autres actions (détail, création, mise à jour, suppression)
        return RealisateurSerializer
