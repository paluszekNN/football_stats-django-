# Generated by Django 2.2.1 on 2019-06-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20190620_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='distance',
        ),
        migrations.AddField(
            model_name='player',
            name='minutes',
            field=models.IntegerField(default=0),
        ),
    ]
