# Generated by Django 3.2.5 on 2021-07-27 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Zlecenia', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zlecenia.employee')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zlecenia.event')),
            ],
        ),
    ]
