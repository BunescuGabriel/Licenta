# Generated by Django 4.2.1 on 2023-12-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produs', '0021_produsex_cutia_produsex_motor'),
    ]

    operations = [
        migrations.AddField(
            model_name='produsex',
            name='Limita_de_KM',
            field=models.CharField(default='fără limită', max_length=200),
        ),
        migrations.AddField(
            model_name='produsex',
            name='caroserie',
            field=models.IntegerField(choices=[(0, 'Van'), (1, 'Universal'), (2, 'Minivan'), (3, 'Roadster'), (4, 'SUV'), (5, 'Cabriolet'), (6, 'Microvan'), (7, 'Pickup'), (8, 'Sedan'), (9, 'Crossover'), (10, 'Hatchback'), (11, 'Combi'), (12, 'Coupe'), (13, 'Not specified')], default=13),
        ),
        migrations.AddField(
            model_name='produsex',
            name='descriere',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produsex',
            name='numar_pasageri',
            field=models.IntegerField(choices=[(0, '2'), (1, '4'), (2, '5'), (3, '7'), (4, 'Not specified')], default=4),
        ),
        migrations.AddField(
            model_name='produsex',
            name='numar_usi',
            field=models.IntegerField(choices=[(0, '3'), (1, '5'), (2, 'Not specified')], default=2),
        ),
    ]
