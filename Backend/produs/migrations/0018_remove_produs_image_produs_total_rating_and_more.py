# Generated by Django 4.2.1 on 2023-11-07 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produs', '0017_produs_image_delete_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produs',
            name='image',
        ),
        migrations.AddField(
            model_name='produs',
            name='total_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='produs',
            name='total_votes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('create_da', models.DateTimeField(auto_now_add=True)),
                ('produs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produs.produs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', null=True, upload_to='car/')),
                ('produs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='produs.produs')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('produs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produs.produs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]