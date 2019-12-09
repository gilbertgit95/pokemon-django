from django.shortcuts import render, redirect
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

class AddView(View):
    def get(self, request):
        poke = {}
        poke['name'] = 'Enter name here'
        poke['weight'] = 0
        poke['height'] = 0
        poke['image'] = ''
        poke['abilities'] = []
        poke['held_items'] = []
        poke['types'] = []

        poke['stats'] = [
            ['speed', 0, 0],
            ['special-defence', 0, 0],
            ['special-attack', 0, 0],
            ['defence', 0, 0],
            ['attack', 0, 0],
            ['hp', 0, 0]
        ]

        back_path = '/'
        action = '/add-pokemon' # or modify

        return render(request, 'poke-form.html', {'pokemon': poke, 'back_path': back_path, 'action': action })


    def post(self, request):
        try:
            name = request.POST.get('name')
            weight = request.POST.get('weight')
            height = request.POST.get('height')
            pokeid = request.POST.get('pokeid')
            abilities = request.POST.get('abilities')
            items = request.POST.get('items')
            types = request.POST.get('types')
            stats = request.POST.get('stats')
            image = request.POST.get('image')

            pokemon = Pokemon(
                poke_id=pokeid,
                name=name,
                weight=weight,
                height=height,
                image=image,
                held_items=items,
                abilities=abilities,
                types=types,
                stats=stats
            )
            pokemon.save()

        except:
            console.log('Error saving the product')
        

        return redirect('/')