from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Post, Image


class CategoryList(ListView):
    model = Category


def postList(request, slug):
    category = Category.objects.get(slug_url=slug)
    post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/Post_list.html',
        {
            'post_list': post_list,
            'category': category,
        }
    )


class PostDetail(DetailView):
    model = Post
