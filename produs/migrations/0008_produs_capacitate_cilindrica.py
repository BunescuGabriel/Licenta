# Generated by Django 4.2.1 on 2023-10-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produs', '0007_remove_produs_capacitate_cilindrica'),
    ]

    operations = [
        migrations.AddField(
            model_name='produs',
            name='capacitate_cilindrica',
            field=models.FloatField(choices=[(1.0, '1.0'), (1.1, '1.1'), (1.2, '1.2'), (1.3, '1.3'), (1.4, '1.4'), (1.5, '1.5'), (1.6, '1.6'), (1.7, '1.7'), (1.8, '1.8'), (1.9, '1.9'), (2.0, '2.0'), (2.1, '2.1'), (2.2, '2.2'), (2.3, '2.3'), (2.4, '2.4'), (2.5, '2.5'), (2.6, '2.6'), (2.7, '2.7'), (2.8, '2.8'), (2.9, '2.9'), (3.0, '3.0'), (3.1, '3.1'), (3.2, '3.2'), (3.3, '3.3'), (3.4, '3.4'), (3.5, '3.5'), (3.6, '3.6'), (3.7, '3.7'), (3.8, '3.8'), (3.9, '3.9'), (4.0, '4.0')], default=1.0),
        ),
    ]
