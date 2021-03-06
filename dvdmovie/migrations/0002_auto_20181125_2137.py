# Generated by Django 2.1.3 on 2018-11-25 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvdmovie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partofseries',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='partofseries',
            old_name='series_id',
            new_name='series',
        ),
        migrations.RenameField(
            model_name='star',
            old_name='actor_id',
            new_name='actor',
        ),
        migrations.RenameField(
            model_name='star',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.AlterUniqueTogether(
            name='partofseries',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='star',
            unique_together={('actor', 'movie', 'role')},
        ),
    ]
