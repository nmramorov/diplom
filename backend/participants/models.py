from excel_data.excel_data_getter import ExcelDataGetter

from django.db import models
from django.utils import timezone


# Create your models here.
class Participant(models.Model):
    participant_id = models.IntegerField(max_length=10)
    participant_start_number = models.IntegerField(max_length=4)
    participant_initials = models.CharField(max_length=25)
    participant_result = models.DateTimeField('date published')

    def __str__(self):
        return f'Участник {self.participant_initials} с ID {self.participant_id}'

    def arrange_data(self):
        now = timezone.now()
        return now
