# Generated by Django 4.1.3 on 2022-12-12 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0003_rename_pais_a_amigos_pais_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amigos',
            old_name='Pais',
            new_name='pais',
        ),
    ]