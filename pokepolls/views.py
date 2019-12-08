from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class PokemonView(View):
    def get(sef, request):
        return render(request, 'home.html')