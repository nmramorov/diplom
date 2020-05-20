from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    return render(request, 'participants_app/index.html')


def show_participants(request):
    participants_to_show = Participants.objects.all()
    print(participants_to_show)
    return render(request, 'participants_app/participants.html', {'participants_to_show': participants_to_show})
