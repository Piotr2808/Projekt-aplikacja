# Generated by Django 3.2.5 on 2021-07-27 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zlecenia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=80, verbose_name='Last Name')),
            ],
        ),
    ]