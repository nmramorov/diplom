from django.db import models


class Participants(models.Model):
    sheet = models.CharField(verbose_name='Стартовый протокол', max_length=25, blank=True, null=True)
    index = models.IntegerField(verbose_name='Стартовый номер', blank=True, null=True)
    identifier = models.AutoField(verbose_name='Индивидуальный номер', primary_key=True)
    initials = models.CharField(verbose_name='Фамилия Имя', max_length=50, blank=True, null=True)
    team = models.CharField(verbose_name='Команда', max_length=100, blank=True, null=True)
    year_of_birth = models.IntegerField(verbose_name='Год рождения', blank=True, null=True)
    grade = models.CharField(verbose_name='Спортивный разряд', max_length=25)
    first_track = models.DateTimeField(verbose_name='Трасса 1', blank=True)
    second_track = models.DateTimeField(verbose_name='Трасса 2', blank=True)
    sum = models.DateTimeField(verbose_name='Сумма', blank=True)

    def __str__(self):
        return self.initials

    class Meta:
        managed = False
        db_table = 'participants'


class Sheets(models.Model):
    sheet = models.CharField(max_length=25, blank=True, null=True)
    identifier = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'sheets'
