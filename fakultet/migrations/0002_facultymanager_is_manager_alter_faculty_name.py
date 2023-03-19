# Generated by Django 4.1.7 on 2023-03-19 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakultet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultymanager',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Fakultet nomi'),
        ),
    ]
