from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views import View
from .models import Pokemon
import re
import json

def get_name_from_url(path):
    p = re.compile(matching_slug_regex)
    return p.search(path).group('name')

class PokemonView(View):
    def get(self, request):
        pokemons = Pokemon.objects.all()
        pokemons = list(pokemons)
        return render(request, 'home.html', {'pokemons': pokemons})

class DetailView(View):
    def get(self, request, name):
        poke = serializers.serialize('json', Pokemon.objects.filter(name=name))
        poke = json.loads(poke)[0]
        poke = poke['fields']

        poke['abilities'] = poke['abilities'].replace(',', ', ')
        poke['held_items'] = poke['held_items'].replace(',', ', ')
        poke['types'] = poke['types'].replace(',', ', ')

        poke['stats'] = poke['stats'].split(',')
        poke['stats'] = [item.split(':') for item in poke['stats']]

        return render(request, 'pokemon.html', {'pokemon': poke})