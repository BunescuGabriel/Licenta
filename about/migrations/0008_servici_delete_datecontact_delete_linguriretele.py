# Generated by Django 4.2.1 on 2023-12-14 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_descrierii'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servici',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviciu', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='DateContact',
        ),
        migrations.DeleteModel(
            name='LinguriRetele',
        ),
    ]
