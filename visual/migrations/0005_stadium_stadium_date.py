# Generated by Django 2.0.7 on 2018-07-19 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visual', '0004_auto_20180715_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='stadium',
            name='stadium_date',
            field=models.DateField(default='2018-06-14'),
        ),
    ]