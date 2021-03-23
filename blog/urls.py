from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.Category.as_view(), name='category'),
    path('<slug:slug>/', views.PostList.as_view(), name='postList'),
    path('<int:id>/', views.PostDetail.as_view(), name='postDetail'),
]
