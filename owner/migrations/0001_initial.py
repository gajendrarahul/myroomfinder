# Generated by Django 3.0.5 on 2021-03-29 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50, null=True)),
                ('contact', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_room', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='owner.Owner')),
            ],
        ),
    ]
