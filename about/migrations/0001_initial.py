# Generated by Django 4.2.1 on 2023-12-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conditii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlu', models.TextField()),
                ('descrierea', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Termini',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlu', models.TextField()),
                ('descrierea', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
    ]
