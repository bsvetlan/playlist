# Generated by Django 3.2.4 on 2021-09-16 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('albumid', models.IntegerField(db_column='AlbumId', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('creationdate', models.DateField(blank=True, db_column='CreationDate', null=True)),
            ],
            options={
                'db_table': 'Album',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('executorid', models.IntegerField(db_column='ExecutorId', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('participants', models.TextField(blank=True, db_column='Participants', null=True)),
                ('apperanceyear', models.DateField(blank=True, db_column='ApperanceYear', null=True)),
            ],
            options={
                'db_table': 'Executor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('playlistid', models.IntegerField(db_column='PlaylistId', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=150, null=True)),
            ],
            options={
                'db_table': 'Playlist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('rewardid', models.IntegerField(db_column='RewardId', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('issueyear', models.DateField(blank=True, db_column='IssueYear', null=True)),
            ],
            options={
                'db_table': 'Reward',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('songid', models.IntegerField(db_column='SongId', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('genre', models.CharField(blank=True, db_column='Genre', max_length=50, null=True)),
                ('releaseyear', models.DateField(blank=True, db_column='ReleaseYear', null=True)),
                ('rating', models.IntegerField(blank=True, db_column='Rating', null=True)),
            ],
            options={
                'db_table': 'Song',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.IntegerField(db_column='UserId', primary_key=True, serialize=False)),
                ('login', models.CharField(db_column='Login', max_length=50)),
                ('username', models.CharField(blank=True, db_column='Username', max_length=255, null=True)),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Songexecutor',
            fields=[
                ('songid', models.OneToOneField(db_column='SongId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='playlist_app.song')),
            ],
            options={
                'db_table': 'SongExecutor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Songplaylist',
            fields=[
                ('playlistid', models.OneToOneField(db_column='PlaylistId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='playlist_app.playlist')),
            ],
            options={
                'db_table': 'SongPlaylist',
                'managed': False,
            },
        ),
    ]
