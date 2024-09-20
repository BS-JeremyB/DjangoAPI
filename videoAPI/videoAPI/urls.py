"""
Configuration des URLs pour le projet videoAPI.

La liste `urlpatterns` route les URLs vers les vues. Pour plus d'informations, consultez :
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Exemples :
Fonctions de vues
    1. Importez une vue :  from my_app import views
    2. Ajoutez une URL à urlpatterns :  path('', views.home, name='home')
Vues basées sur les classes
    1. Importez une vue :  from other_app.views import Home
    2. Ajoutez une URL à urlpatterns :  path('', Home.as_view(), name='home')
Inclure une autre URLconf
    1. Importez la fonction include() : from django.urls import include, path
    2. Ajoutez une URL à urlpatterns :  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # URL pour accéder à l'interface d'administration Django
    path('admin/', admin.site.urls),
    # Inclusion des URLs de l'application 'realisateur'
    path('api/realisateur/', include('realisateur.urls')),
    # Inclusion des URLs de l'application 'film'
    path('api/film/', include('film.urls')),
    # URL pour obtenir un jeton JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # URL pour rafraîchir le jeton JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
