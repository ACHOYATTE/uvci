# Generated by Django 4.2.3 on 2023-08-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_pharmacie_garde'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacie',
            name='garde',
            field=models.BooleanField(default=0, verbose_name='valider la personne'),
        ),
    ]