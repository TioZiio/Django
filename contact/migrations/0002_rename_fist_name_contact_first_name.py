# Generated by Django 5.1.1 on 2024-09-20 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='fist_name',
            new_name='first_name',
        ),
    ]
