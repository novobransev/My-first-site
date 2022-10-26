# Generated by Django 4.0.3 on 2022-04-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_abs', '0002_biology_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='chemistry',
            name='title',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='english',
            name='title',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='history',
            name='title',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='information',
            name='title',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='literature',
            name='title',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='math',
            name='title',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='obz',
            name='title',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='oid',
            name='title',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='physics',
            name='title',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='russian_language',
            name='title',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='social_studies',
            name='title',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='biology',
            name='title',
            field=models.CharField(default=None, max_length=2),
        ),
    ]