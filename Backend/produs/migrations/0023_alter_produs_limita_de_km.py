# Generated by Django 4.2.1 on 2024-01-21 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produs', '0022_alter_produs_limita_de_km'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produs',
            name='Limita_de_KM',
            field=models.TextField(default='fara limita'),
        ),
    ]
