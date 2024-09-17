from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmList.as_view(), name="list-film"),
    path('<int:pk>', views.FilmDetail.as_view(), name="detail-film")
]
