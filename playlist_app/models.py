# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Album(models.Model):
    albumid = models.IntegerField(db_column='AlbumId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    creationdate = models.DateField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Album'


class Executor(models.Model):
    executorid = models.IntegerField(db_column='ExecutorId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    participants = models.TextField(db_column='Participants', blank=True, null=True)  # Field name made lowercase.
    apperanceyear = models.DateField(db_column='ApperanceYear', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Executor'


class Playlist(models.Model):
    playlistid = models.IntegerField(db_column='PlaylistId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Playlist'


class Reward(models.Model):
    rewardid = models.IntegerField(db_column='RewardId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    issueyear = models.DateField(db_column='IssueYear', blank=True, null=True)  # Field name made lowercase.
    songid = models.ForeignKey('Song', models.DO_NOTHING, db_column='SongId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reward'


class Song(models.Model):
    songid = models.IntegerField(db_column='SongId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    albumid = models.ForeignKey(Album, models.DO_NOTHING, db_column='AlbumId', blank=True, null=True)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    releaseyear = models.DateField(db_column='ReleaseYear', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Song'


class Songexecutor(models.Model):
    songid = models.OneToOneField(Song, models.DO_NOTHING, db_column='SongId', primary_key=True)  # Field name made lowercase.
    executorid = models.ForeignKey(Executor, models.DO_NOTHING, db_column='ExecutorId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SongExecutor'
        unique_together = (('songid', 'executorid'),)


class Songplaylist(models.Model):
    playlistid = models.OneToOneField(Playlist, models.DO_NOTHING, db_column='PlaylistId', primary_key=True)  # Field name made lowercase.
    songid = models.ForeignKey(Song, models.DO_NOTHING, db_column='SongId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SongPlaylist'
        unique_together = (('playlistid', 'songid'),)


class User(models.Model):
    userid = models.IntegerField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'
