# Generated by Django 3.0.5 on 2021-03-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0005_auto_20210329_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='type',
        ),
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
