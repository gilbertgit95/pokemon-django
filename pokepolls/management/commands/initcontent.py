from django.core.management.base import BaseCommand, CommandError
import pokebase as pb
import requests

BASE_API = 'https://pokeapi.co/api/v2'
# from polls.models import Question as Poll
# https://pokeapi.co/api/v2/generation/1/

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
       pass

    def handle(self, *args, **options):
        self.stdout.write('Note! this comand will takes minutes to complete because of pokeapi limitations.')

        try:
            pokemons = requests.get(f'{ BASE_API }/generation/1/')

            # pokemons = pb.NamedAPIResource('berry', 'cherry')
            pokemons = pokemons.json()
            pokemons = pokemons['pokemon_species']
            print(len(pokemons))

        except:
            self.stderr.write('Error fetching the pokemons!')
        