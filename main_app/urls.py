from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),

    path('about/', views.about, name="about"),

    path('movies/',views.movies_index, name='movies_index'),

    

]
