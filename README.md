# Django API Project

Ce guide vous détaillera la création d'une API Django, avec un focus sur les modèles relationnels, les serializers, les permissions, et d'autres fonctionnalités comme le filtrage et l'authentification JWT.

---

## Étapes de développement

### 1. Installation d'un environnement virtuel

Créez un environnement virtuel pour isoler les dépendances :

```bash
python -m venv .venv
source .venv/bin/activate   # Sur Windows : .venv\Scripts\activate
```

### 2. Installation des dépendances

Installez les modules listés dans `requirements.txt`, qui incluent :

- **Django** : Framework principal.
- **django-filter** : Pour le filtrage dans les API.
- **djangorestframework** : Pour gérer les API REST dans Django.
- **SimpleJWT** : Pour l'authentification avec JWT.
- **psycopg2** : Pour la connexion à PostgreSQL.

Installez ces modules :

```bash
pip install -r requirements.txt
```

### 3. Création du projet Django

Créez le projet :

```bash
django-admin startproject myproject
```

### 4. Création des apps `Film` et `Realisateur`

Créez les deux apps nécessaires au projet :

```bash
python manage.py startapp film
python manage.py startapp realisateur
```

### 5. Configuration de `settings.py`

Dans `settings.py`, ajoutez les apps et configurez la base de données avec `django-environ` pour sécuriser les informations sensibles.

---

## 6. Modèles et relations

Les modèles sont au cœur de votre projet. Ils définissent les structures de données et les relations entre les entités.

### Exemple de modèle avec relation

Dans `film/models.py` et `realisateur/models.py`, vous allez créer des modèles avec une relation **many-to-one** (plusieurs films peuvent avoir le même réalisateur). Voici comment cela se présente :

```python
# realisateur/models.py
from django.db import models

class Realisateur(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
```

```python
# film/models.py
from django.db import models
from realisateur.models import Realisateur

class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    director = models.ForeignKey(Realisateur, related_name='films', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

#### Explication des relations

- Le modèle `Film` a une relation **ForeignKey** avec le modèle `Realisateur`. Cela signifie que chaque film est associé à un réalisateur, mais un réalisateur peut être associé à plusieurs films (relation "un-à-plusieurs").
- L'argument `related_name='films'` permet d'accéder à tous les films d'un réalisateur depuis une instance de `Realisateur`.

Une fois les modèles créés, exécutez les migrations :

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 7. Serializers et relations

Les **serializers** transforment les objets Django en formats comme JSON (ou XML). Ils jouent un rôle essentiel dans une API, car ils définissent comment les données sont présentées et validées.

### Exemple de Serializer

Un serializer de base pour le modèle `Film` :

```python
from rest_framework import serializers
from .models import Film

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'release_date', 'director']
```

#### Serializers avec relations

Il est possible d'inclure les relations dans le serializer. Par exemple, pour afficher le nom du réalisateur au lieu de l'ID, vous pouvez utiliser un **SerializerMethodField** ou directement référencer l'attribut via la relation :

```python
class FilmSerializer(serializers.ModelSerializer):
    director_name = serializers.CharField(source='director.name', read_only=True)

    class Meta:
        model = Film
        fields = ['id', 'title', 'release_date', 'director', 'director_name']
```

### Utilisation d'hyperliens

Django REST Framework propose également des **serializers avec hyperliens**, qui permettent de représenter les relations avec des URLs, ce qui est particulièrement utile dans les APIs RESTful. Vous pouvez utiliser `HyperlinkedModelSerializer` pour ce faire.

```python
class FilmHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    director = serializers.HyperlinkedRelatedField(
        view_name='realisateur-detail',
        read_only=True
    )

    class Meta:
        model = Film
        fields = ['url', 'title', 'release_date', 'director']
```

#### Pourquoi utiliser des hyperliens ?

L'utilisation d'hyperliens dans les serializers rend l'API plus conforme au style **RESTful** en permettant aux clients de suivre les relations directement à travers des URLs. Cela aide à mieux structurer l'API en créant une navigation claire entre les différentes entités.

Par exemple, dans un client REST, vous pouvez suivre le lien du réalisateur directement depuis la représentation d'un film, au lieu de simplement récupérer un ID.

---

### 8. Vue avec ViewSets

Créez une vue simple avec un **ViewSet** qui va gérer les actions CRUD pour les films :

```python
from rest_framework import viewsets
from .models import Film
from .serializers import FilmSerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
```

### 9. Configuration des routes

Utilisez un **DefaultRouter** pour gérer automatiquement les routes pour vos ViewSets :

```python
from rest_framework.routers import DefaultRouter
from .views import FilmViewSet

router = DefaultRouter()
router.register(r'films', FilmViewSet)

urlpatterns = router.urls
```

Le **DefaultRouter** crée automatiquement des routes pour les actions **list**, **create**, **retrieve**, **update**, et **destroy**.

---

### 10. Permissions

Vous pouvez définir des permissions dans votre vue via `permission_classes` ou les personnaliser en surchargant `get_permissions`. Voici un exemple de permissions personnalisées dans un ViewSet :

```python
from rest_framework.permissions import IsAuthenticated, AllowAny

class FilmViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]
```

---

### 11. Pagination

Configurez la pagination dans `settings.py` :

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

---

### 12. Filtrage avec `django-filter`

Ajoutez le filtrage dans vos vues avec `django-filter` :

```python
from django_filters.rest_framework import DjangoFilterBackend

class FilmViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'release_date']
```

---

### 13. Ordering

Vous pouvez aussi ajouter un backend de tri :

```python
from rest_framework.filters import OrderingFilter

class FilmViewSet(viewsets.ModelViewSet):
    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'release_date']
```

