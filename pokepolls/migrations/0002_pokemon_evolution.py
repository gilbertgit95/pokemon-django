# Generated by Django 3.0 on 2019-12-14 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokepolls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='evolution',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
