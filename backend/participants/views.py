from django.shortcuts import render
from .models import Participants

# Create your views here.
def show_participants(request):
    participants = Participants()
    participants.save_participants()
    participants_to_show = participants.objects.order_by()
    return render(request, 'participants/participants.html', {'participants': participants_to_show})
