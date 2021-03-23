from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Post, Image


class Category(ListView):
    model = Category


class PostList(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['category'] = Category.objects.all()
        return context


class PostDetail(DetailView):
    model = Post
