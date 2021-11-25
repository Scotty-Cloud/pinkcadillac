from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),

    path('about/', views.about, name="about"),

    path('movies/',views.movies_index, name='movies_index'),

   path('movies/<int:movie_id>/', views.movies_detail, name='movies_detail'),

   path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),

   path('movies/<int:pk>/update', views.MovieUpdate.as_view(), name="movies_update"),

   path('movies/<int:pk>/delete', views.MovieDelete.as_views(), name="movies_delete"),

  path('movies/<int:movie_id>/add_releaseYr/', views.add_releaseYr, name="add_releaseYr"),

  path('songs/create/', views.SongCreate.as_view(), name='songs_create'),

  path('songs/<int:pk>/', views.SongDetail.as_view(), name='songs_detail'),

  path('songs/', views.SongList.as_views(), name='songs_index'),

  path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='songs_update'),

  path('songs/<int:pk>/delete/', views.SongDelete.as_views(), name='songs_delete'),


  path(),

  path("accounts/signup/", views.signup, name="signup")
]