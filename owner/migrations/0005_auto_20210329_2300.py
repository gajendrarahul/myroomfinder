# Generated by Django 3.0.5 on 2021-03-29 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_remove_owner_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='user',
            new_name='account',
        ),
    ]