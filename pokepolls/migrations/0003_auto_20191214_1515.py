# Generated by Django 3.0 on 2019-12-14 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokepolls', '0002_pokemon_evolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='evolution',
            field=models.CharField(max_length=200),
        ),
    ]
