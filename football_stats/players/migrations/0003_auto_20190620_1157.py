# Generated by Django 2.2.1 on 2019-06-20 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20190620_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='accurate_cross',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='accurate_passes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='accurate_shots',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='catch_saves',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='complete_tackles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='created_situations',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='crosses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='culpable_goals',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='distance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='dribble',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='fouls_on',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='heads',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='interceptions',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='key_heads',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='key_passes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='key_tackles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='mistakes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='offsides',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='passes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='saves',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='saves_on_corner',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='shots',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='tackles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='win_heads',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='assists',
            field=models.IntegerField(default=0),
        ),
    ]
