# Generated by Django 2.1.3 on 2018-11-25 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0003_auto_20181125_0026'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Votes',
            new_name='Vote',
        ),
    ]
