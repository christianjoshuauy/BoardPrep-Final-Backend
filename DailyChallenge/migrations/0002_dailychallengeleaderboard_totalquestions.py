# Generated by Django 4.2.4 on 2024-08-05 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyChallenge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailychallengeleaderboard',
            name='totalQuestions',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]