from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.diary, name='main'),
    path('upload_image/', views.uploadImage),
]
