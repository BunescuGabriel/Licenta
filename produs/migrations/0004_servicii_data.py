# Generated by Django 4.2.1 on 2023-10-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produs', '0003_banner_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicii',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
