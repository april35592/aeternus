from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.Category.as_view(), name='category'),
    path('<slug:slug>/', views.PostList.as_view(), name='postList'),
    path('<slug:slug>/<int:id>/', name='postDetail'),
]