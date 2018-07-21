# Generated by Django 2.0.7 on 2018-07-21 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visual', '0008_auto_20180719_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='score',
            field=models.CharField(default='0-0', max_length=5),
        ),
        migrations.AddField(
            model_name='game',
            name='stage',
            field=models.CharField(choices=[('Group', 'Group'), ('Round of 16', 'Round of 16'), ('Quarter', 'Quarter'), ('Semis', 'Semis')], default='Group', max_length=20),
        ),
    ]
