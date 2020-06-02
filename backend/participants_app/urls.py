from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

from . import models
from . import views


# Serializers define the API representation.
class ParticipantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Participants
        fields = ['sheet', 'index', 'identifier', 'initials', 'team',
                  'year_of_birth', 'grade', 'first_track', 'second_track', 'sum']


# ViewSets define the view behavior.
class ParticipantsViewSet(viewsets.ModelViewSet):
    queryset = models.Participants.objects.all()
    serializer_class = ParticipantsSerializer


class SheetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Sheets
        fields = ['sheet']


# ViewSets define the view behavior.
class SheetsViewSet(viewsets.ModelViewSet):
    queryset = models.Sheets.objects.all()
    serializer_class = SheetsSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'participants_api', ParticipantsViewSet)
router.register(r'sheets_api', SheetsViewSet)

app_name = 'participants_app'
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.index, name='index'),
    path('participants', views.show_participants, name='participants_app',)
]
