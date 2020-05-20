from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from . import models
from . import views


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Participants
        fields = ['sheet', 'index', 'identifier', 'initials']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.Participants.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

app_name = 'participants_app'
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.index, name='index'),
    path('participants', views.show_participants, name='participants_app',)
]
