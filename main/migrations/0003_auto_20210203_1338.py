# Generated by Django 3.1.5 on 2021-02-03 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210203_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='categories',
            new_name='category',
        ),
    ]
