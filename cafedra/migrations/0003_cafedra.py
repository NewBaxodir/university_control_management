# Generated by Django 4.1.7 on 2023-03-03 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fakultet', '0001_initial'),
        ('cafedra', '0002_delete_cafedra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafedra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Kafedra nomi')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fakultet.faculty', verbose_name='Fakulteti')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafedra.cafedramanager', verbose_name='Kafedra manageri')),
            ],
            options={
                'verbose_name': 'Kafedra',
                'verbose_name_plural': '2. Kafedralar',
            },
        ),
    ]
