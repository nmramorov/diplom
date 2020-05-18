from django.urls import path

from . import views


app_name = 'participants'
urlpatterns = [
    path('participants/', views.show_participants, name='participants'),
]