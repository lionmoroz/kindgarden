# Generated by Django 3.1.6 on 2021-03-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='team_photo', verbose_name='Фото'),
        ),
    ]
