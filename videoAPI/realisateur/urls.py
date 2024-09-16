from django.urls import path
from . import views

urlpatterns = [
    path('', views.RealisateurList.as_view(), name="realisateur_list"),
    path('<int:pk>', views.RealisateurDetail.as_view(), name="realisateur_detail")
]
