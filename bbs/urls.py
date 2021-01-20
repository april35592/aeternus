from django.urls import path
from . import views

app_name = 'bbs'
urlpatterns = [
    path('', views.index, name='bbs'),
    path('guestcreate/', views.guestcreate, name='guestcreate'),
]
