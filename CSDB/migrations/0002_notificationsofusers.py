# Generated by Django 3.2 on 2021-04-17 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSDB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationsOfUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NotificationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSDB.notifications')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSDB.users')),
            ],
        ),
    ]