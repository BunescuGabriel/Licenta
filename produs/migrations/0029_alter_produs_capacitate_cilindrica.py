# Generated by Django 4.2.1 on 2024-02-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produs', '0028_rename_capacitate_cilindricaa_produs_capacitate_cilindrica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produs',
            name='capacitate_cilindrica',
            field=models.CharField(default=0.8, max_length=100),
        ),
    ]
