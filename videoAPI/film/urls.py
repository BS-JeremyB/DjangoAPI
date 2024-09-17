from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmList.as_view(), name="film-list"),
    path('<int:pk>', views.FilmDetail.as_view(), name="film-detail")
]
