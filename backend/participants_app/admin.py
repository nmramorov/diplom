from django.contrib import admin

from .models import Participants


class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ('initials', 'identifier', 'team')
    search_fields = ['initials']


admin.site.register(Participants, ParticipantsAdmin)
