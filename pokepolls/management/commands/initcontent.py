from django.core.management.base import BaseCommand, CommandError
import requests
import time
import re

from pokepolls.models import Pokemon

BASE_API = 'https://pokeapi.co/api/v2'
# from polls.models import Question as Poll
# https://pokeapi.co/api/v2/generation/1/

def getEvolution(id):
    try:
        species = requests.get(f'{ BASE_API }/pokemon-species/{ id }/')
        species = species.json()
        evol = requests.get(species['evolution_chain']['url'])
        evol = evol.json()

        chain = []

        chainSpecies = evol['chain']

        while chainSpecies:
            chain.append(chainSpecies['species']['name'])
            if chainSpecies['evolves_to'] and len(chainSpecies['evolves_to']):
                chainSpecies = chainSpecies['evolves_to'][0]
            else:
                chainSpecies = None

        return chain
    except:
        return []

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
       pass

    def handle(self, *args, **options):
        pokemons = []
        self.stdout.write('Note! this comand will takes minutes to complete due to pokeapi limitations.')
        time.sleep(2)
        self.stdout.write('- Fetching Pokemons')
        # request all 1 generation pokemons
        try:
            pokeInfo = requests.get(f'{ BASE_API }/generation/1/')
            pokeInfo = pokeInfo.json()
            pokeInfo = pokeInfo['pokemon_species']

            for poke in pokeInfo:
                # request information of a particular pokemon
                try:
                    # initiate variables
                    poke_id = int(re.split('\/', poke['url'])[-2])
                    evolution = '' #[]
                    name = ''
                    height = ''
                    weight = ''
                    image = ''
                    held_items = '' #[]
                    abilities = '' #[]
                    types = '' #[]
                    stats = '' #[]

                    pokemon = requests.get(f'{ BASE_API }/pokemon/{ poke_id }/')
                    pokemon = pokemon.json()

                    # extract only the information use in this app
                    # basic information
                    name = pokemon['name']
                    height = pokemon['height']
                    weight = pokemon['weight']
                    image = pokemon['sprites']['front_default']

                    evolution = getEvolution(poke_id)

                    # stringified list of information
                    evolution = ','.join(evolution)
                    held_items = ','.join(d['item']['name'] for d in pokemon['held_items'])
                    abilities = ','.join(d['ability']['name'] for d in pokemon['abilities'])
                    types = ','.join(d['type']['name'] for d in pokemon['types'])
                    stats = ','.join(f"{ d['stat']['name'] }:{ d['base_stat'] }:{ d['effort'] }" for d in pokemon['stats'])

                    pokemons.append({
                        'poke_id': poke_id,
                        'evolution': evolution,
                        'name': name,
                        'height': height,
                        'weight': weight,
                        'image': image,
                        'held_items': held_items,
                        'abilities': abilities,
                        'types': types,
                        'stats': stats
                    })
                    time.sleep(0.5)

                except:
                    pass

            self.stdout.write('  +-> Done')

        except:
            self.stderr.write('  +-> Error fetching the pokemons!')

        # save the pokemons to the model
        if pokemons and len(pokemons):
            self.stdout.write('- Saving all the pokemons')
            poke_objs = []
            for poke in pokemons:
                poke_objs.append(Pokemon(
                    poke_id=    poke['poke_id'],
                    evolution=  poke['evolution'],
                    name=       poke['name'],
                    height=     poke['height'],
                    weight=     poke['weight'],
                    image=      poke['image'],
                    held_items= poke['held_items'],
                    abilities=  poke['abilities'],
                    types=      poke['types'],
                    stats=       poke['stats']
                ))

            Pokemon.objects.bulk_create(poke_objs)
            self.stdout.write('  +-> Done')

        else:
            self.stderr.write('No Pokemon to be save!')

        self.stdout.write('End of the Process...')