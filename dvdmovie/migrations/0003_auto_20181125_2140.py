# Generated by Django 2.1.3 on 2018-11-25 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvdmovie', '0002_auto_20181125_2137'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='partofseries',
            unique_together={('series', 'movie')},
        ),
    ]
