from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name="home"),

  path('about/', views.about, name="about"),

  path('movies/', views.movies_index, name='movies_index'),

  path('movies/<int:movie_id>/', views.movies_detail, name='movies_detail'),

  path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),

  path('movies/<int:pk>/update', views.MovieUpdate.as_view(), name="movies_update"),

  path('movies/<int:pk>/delete', views.MovieDelete.as_view(), name="movies_delete"),

  path('movies/<int:movie_id>/add_releaseYr/', views.add_releaseYr, name="add_releaseYr"),

  path("accounts/signup/", views.signup, name="signup"),
]