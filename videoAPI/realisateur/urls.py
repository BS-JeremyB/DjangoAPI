from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.RealisateurList.as_view(), name="realisateur-list"),
    path('<int:pk>', views.RealisateurDetail.as_view(), name="realisateur-detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)