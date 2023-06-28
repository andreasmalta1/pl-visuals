# Generated by Django 4.2.2 on 2023-06-28 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('club_id', models.IntegerField(primary_key=True, serialize=False)),
                ('club_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerLeagueData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=10)),
                ('player_name', models.CharField(max_length=50)),
                ('nation', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('league', models.CharField(max_length=50)),
                ('matches_played', models.IntegerField()),
                ('starts', models.IntegerField()),
                ('minutes', models.IntegerField()),
                ('goals', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('penalty_kicks', models.IntegerField()),
                ('penalty_goals', models.IntegerField()),
                ('xg', models.FloatField()),
                ('non_penalty_xg', models.FloatField()),
                ('xa', models.FloatField()),
                ('yellow_cards', models.IntegerField()),
                ('red_cards', models.IntegerField()),
                ('progressive_passes', models.IntegerField()),
                ('progressive_carries', models.IntegerField()),
                ('progressive_receives', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.club')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerCompetitionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=10)),
                ('player_name', models.CharField(max_length=50)),
                ('nation', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('league', models.CharField(max_length=50)),
                ('matches_played', models.IntegerField()),
                ('starts', models.IntegerField()),
                ('minutes', models.IntegerField()),
                ('goals', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('penalty_kicks', models.IntegerField()),
                ('penalty_goals', models.IntegerField()),
                ('xg', models.FloatField()),
                ('non_penalty_xg', models.FloatField()),
                ('xa', models.FloatField()),
                ('yellow_cards', models.IntegerField()),
                ('red_cards', models.IntegerField()),
                ('progressive_passes', models.IntegerField()),
                ('progressive_carries', models.IntegerField()),
                ('progressive_receives', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.club')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=10)),
                ('num_matches', models.IntegerField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.club')),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
    ]
