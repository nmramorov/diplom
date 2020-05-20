# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Participants(models.Model):
    sheet = models.CharField(max_length=25, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    identifier = models.AutoField(primary_key=True)
    initials = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    year_of_birth = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=5, blank=True, null=True)
    first_track = models.DateTimeField(blank=True, null=True)
    second_track = models.DateTimeField(blank=True, null=True)
    sum = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participants'
