from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.PokemonView.as_view(), name='index'),
    path('add-pokemon', views.AddView.as_view(), name='add'),
    re_path(r'^pokemons/(?P<name>[\w-]+)/$', views.DetailView.as_view(), name='detail')
]