# Generated by Django 4.1.3 on 2022-12-11 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplikacja_Django', '0003_rating_movie_alter_actor_name_alter_actor_surname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True),
        ),
    ]
