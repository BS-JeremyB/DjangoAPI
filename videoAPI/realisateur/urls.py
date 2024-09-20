from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# Enregistrement du RealisateurViewSet dans le routeur
router.register(r'', views.RealisateurViewSet)

urlpatterns = [
    # Inclusion des URLs générées par le routeur pour l'application 'realisateur'
    path('', include(router.urls))
]
