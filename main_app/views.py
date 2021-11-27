from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie, Song, Photo
from .forms import ReleaseForm

# Create your views here.

class Home(LoginView):
  template_name = "home.html"

def about(request):
  return render(request, 'about.html')

@login_required
def movies_index(request):
  movies = Movie.objects.filter(user=request.user)
  return render(request, 'movies/index.html', {'movies' : movies})

@login_required
def movies_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  songs_movies_doesnt_have = Song.objects.exclude( id__in = movie.songs.all().values_list('id'))
  release_form = ReleaseForm()
  return render(request, 'movies/index.html', {
    'movie' : movie, 'release_form' : release_form, 'songs' : songs_movies_doesnt_have,})

class MovieCreate(LoginRequiredMixin, CreateView):
  model = Movie
  fields = ['name', 'description' 'recommend']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class MovieUpdate(LoginRequiredMixin, UpdateView):
  model = Movie
  fields = ['name', 'description' 'recommend']

class MovieDelete(LoginRequiredMixin, DeleteView):
  model = Movie
  success_url = '/movies/'

@login_required
def add_releaseYr(request, movie_id):
  form = ReleaseForm(request.POST)
  if form.is_valid():
    new_releaseYr = form.save(commit=False)
    new_releaseYr.movie_id = movie_id
    new_releaseYr.save()
  return redirect("movies_detail", movie_id=movie_id)

class SongCreate(LoginRequiredMixin, CreateView):
  model = Song
  field = '__all__'

class SongList(LoginRequiredMixin, ListView):
  model = Song

class SongDetail(LoginRequiredMixin, DetailView):
  model = Song

class SongUpdate(LoginRequiredMixin, UpdateView):
  model = Song
  fields = ['name']

class SongDelete(LoginRequiredMixin, DeleteView):
  model = Song
  success_url = '/songs/'

@login_required

def signup(request):
  error_message = ""
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('movies_index')
    else:
      error_message = "Invalid sign up try again"
  form = UserCreationForm()
  context = {'form' : form, 'error_message' : error_message}
  return render(request, 'signup.html', context)

