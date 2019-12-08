from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Pokemon

class PokemonView(View):
    def get(sef, request):
        pokemons = Pokemon.objects.all()
        pokemons = list(pokemons)
        return render(request, 'home.html', {'pokemons': pokemons})