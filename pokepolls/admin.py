from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Pokemon

class PokemonAdmin(UserAdmin):
    model = Pokemon
    list_display = ('poke_id', 'name', 'created', 'image')
    search_fields = ('name',)
    readonly_fields = ('poke_id', 'created')

    ordering = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(Pokemon, PokemonAdmin)
