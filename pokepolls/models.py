from django.db import models

# Create your models here.
class Pokemon(models.Model):

    poke_id = models.PositiveIntegerField()
    evolution = models.CharField(max_length=200)
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