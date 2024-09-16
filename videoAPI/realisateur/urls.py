from django.urls import path
from . import views

urlpatterns = [
    path('', views.realisateur_list, name="realisateur_list"),
    path('<int:pk>', views.realisateur_detail, name="realisateur_detail")
]
