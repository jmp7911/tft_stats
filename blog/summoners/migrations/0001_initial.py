# Generated by Django 4.2.1 on 2024-08-07 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AugmentDto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CompanionDto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_ID', models.CharField(max_length=100)),
                ('item_ID', models.CharField(blank=True, max_length=100)),
                ('skin_ID', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InfoDto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_datetime', models.BigIntegerField()),
                ('game_length', models.FloatField()),
                ('gameId', models.BigIntegerField()),
                ('mapId', models.IntegerField()),
                ('gameCreation', models.BigIntegerField()),
                ('game_version', models.CharField(max_length=100)),
                ('tft_set_number', models.IntegerField()),
                ('queue_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemDto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MetadataDto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_version', models.CharField(max_length=100)),
                ('match_id', models.CharField(max_length=100)),
                ('participants', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SummonerDto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=100)),
                ('puuid', models.CharField(max_length=100)),
                ('summoner_id', models.CharField(max_length=100)),
                ('summonerLevel', models.IntegerField()),
                ('profileIconId', models.IntegerField()),
                ('revisionDate', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TraitDto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('num_units', models.IntegerField()),
                ('style', models.IntegerField()),
                ('tier_current', models.IntegerField()),
                ('tier_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UnitDto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('rarity', models.IntegerField()),
                ('tier', models.IntegerField()),
                ('items', models.ManyToManyField(to='summoners.itemdto')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantDto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gold_left', models.IntegerField()),
                ('last_round', models.IntegerField()),
                ('level', models.IntegerField()),
                ('placement', models.IntegerField()),
                ('players_eliminated', models.IntegerField()),
                ('puuid', models.CharField(max_length=100)),
                ('time_eliminated', models.FloatField()),
                ('total_damage_to_players', models.IntegerField()),
                ('augments', models.ManyToManyField(to='summoners.augmentdto')),
                ('companion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summoners.companiondto')),
                ('traits', models.ManyToManyField(to='summoners.traitdto')),
                ('units', models.ManyToManyField(to='summoners.unitdto')),
            ],
        ),
        migrations.CreateModel(
            name='MatchDto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summoners.infodto')),
                ('metadata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summoners.metadatadto')),
            ],
        ),
        migrations.AddField(
            model_name='infodto',
            name='participants',
            field=models.ManyToManyField(to='summoners.participantdto'),
        ),
    ]
