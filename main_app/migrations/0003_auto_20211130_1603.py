# Generated by Django 3.2.7 on 2021-11-30 16:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_delete_song'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='release',
            options={},
        ),
        migrations.RemoveField(
            model_name='release',
            name='date',
        ),
        migrations.AddField(
            model_name='movie',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Release Date'),
            preserve_default=False,
        ),
    ]
