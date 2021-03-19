from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Post, Image

class Category(ListView):
    model = Category
    def get_queryset(self):
        return Category.objects.order_by()
