# Generated by Django 4.2.1 on 2023-10-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_servicii', models.CharField(max_length=150, null=True)),
                ('servicii', models.ImageField(upload_to='servicii/')),
            ],
        ),
    ]