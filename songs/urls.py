from django.urls import path
from . import views


urlpatterns = [
    path("api/albums/<int:album_id>/songs/", views.SongView.as_view()),
]
