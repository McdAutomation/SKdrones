# Generated by Django 2.0.7 on 2018-07-14 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_a', models.CharField(max_length=50)),
                ('team_b', models.CharField(max_length=50)),
                ('game_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.IntegerField()),
                ('long', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stadiums', to='visual.Game')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
