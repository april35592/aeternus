from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password
from .models import Image, Reply
import hashlib

def diary(request):
    page = request.GET.get('page', '1')
    image_list = Image.objects.order_by('-id')
    paginator = Paginator(image_list, 5)
    page_obj = paginator.get_page(page)
    return render(
        request,
        'diary/diary_list.html',
        {
            'image_list' : page_obj,
            'reply_set' : Reply,
        })

def uploadImage(request):
    if request.method == 'POST':
        password = make_password(request.POST['image_password'])
        image_file = request.FILES['image_file']
        if image_file :
            image = Image(
                image = image_file,
                password = password,
            )
            image.save()
            return redirect('diary:main')