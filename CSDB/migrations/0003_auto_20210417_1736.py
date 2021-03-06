# Generated by Django 3.2 on 2021-04-17 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSDB', '0002_notificationsofusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playgrounds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='Название команды')),
                ('GeoCoords_Longitude', models.FloatField(verbose_name='Широта')),
                ('GeoCoords_Latitude', models.FloatField(verbose_name='Долгота')),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='Название спорта')),
                ('Type', models.CharField(max_length=100, verbose_name='Тип спорта')),
            ],
            options={
                'verbose_name': 'Вид спорта',
                'verbose_name_plural': 'Виды спорта',
                'ordering': ['Name', 'Type'],
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='Название команды')),
                ('City', models.CharField(max_length=100, verbose_name='Город')),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='Occupation',
        ),
        migrations.RemoveField(
            model_name='users',
            name='SocialNetworks',
        ),
        migrations.CreateModel(
            name='TeamsOfUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeamID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSDB.teams')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSDB.users')),
            ],
        ),
        migrations.CreateModel(
            name='SportsOfUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SportID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSDB.sports')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSDB.users')),
            ],
        ),
        migrations.CreateModel(
            name='SportsOfPlaygrounds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlaygroundID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSDB.playgrounds')),
                ('SportID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSDB.sports')),
            ],
        ),
        migrations.CreateModel(
            name='SocialNetworksOfUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Link', models.TextField(verbose_name='Ссылка')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSDB.users')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='Имя')),
                ('DateTime', models.DateTimeField(verbose_name='Запланированное дата и время')),
                ('Regularity', models.CharField(max_length=50, verbose_name='Частота')),
                ('Description', models.TextField(verbose_name='Описание')),
                ('PlaygroundID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSDB.playgrounds')),
                ('SportID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSDB.sports')),
                ('TeamID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSDB.teams')),
            ],
        ),
    ]
