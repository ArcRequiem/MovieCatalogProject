# Generated by Django 2.1.3 on 2018-12-02 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvdmovie', '0005_auto_20181126_0145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dvd',
            options={'ordering': ('name', 'dateadded')},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('title', 'releasedate')},
        ),
        migrations.AlterModelOptions(
            name='partofseries',
            options={'ordering': ('series', 'number', 'movie'), 'verbose_name': 'Series Belongs To', 'verbose_name_plural': 'Series Belong To'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('nameknownby', 'prefix', 'surname', 'givenname', 'suffix')},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'ordering': ('name',), 'verbose_name_plural': 'Series'},
        ),
        migrations.AlterModelOptions(
            name='star',
            options={'ordering': ('movie', 'actor', 'role')},
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='Genre Name'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='Language Name'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='releasedate',
            field=models.DateField(verbose_name='Release Date'),
        ),
        migrations.AlterField(
            model_name='partofseries',
            name='number',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='givenname',
            field=models.CharField(max_length=128, verbose_name='Given Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='nameknownby',
            field=models.CharField(blank=True, max_length=128, verbose_name='Name Known By'),
        ),
        migrations.AlterField(
            model_name='person',
            name='prefix',
            field=models.CharField(blank=True, max_length=64, verbose_name='Prefix'),
        ),
        migrations.AlterField(
            model_name='person',
            name='suffix',
            field=models.CharField(blank=True, max_length=64, verbose_name='Suffix'),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(max_length=128, verbose_name='Surname'),
        ),
    ]
