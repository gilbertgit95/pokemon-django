from django.db import models

# Create your models here.
class Pokemon(models.Model):

    poke_id = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    image = models.CharField(max_length=500)
    held_items = models.CharField(max_length=500)
    abilities = models.CharField(max_length=500)
    types = models.CharField(max_length=500)
    stats = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Pokemon'

    def save(self, data):
        # required fields
        # poki_id

        if (data['poke_id']):
            pokemon = Pokemon(
                poke_id= data['poke_id'],
                name= data['name'],
                weight= data['weight'],
                height= data['height'],
                image= data['image'],
                held_items= data['items'],
                abilities= data['abilities'],
                types= data['types'],
                stats= data['stats']
            )
            pokemon.save()
        else:
            raise RequiredDataError('poke_id is required.')