from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Guest, Reply
from .form import GuestForm
# Create your views here.

def index(request):
    reply_list = Reply.objects.order_by('-id')
    return render(request, 'bbs/reply_list.html', {'reply_list':reply_list})

def guestcreate(request):
    reply_list = Reply.objects.order_by('-id')
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.date = timezone.now()
            guest.save()
            return redirect('bbs:bbs')
    else:
        form = GuestForm()
    return render(request, 'bbs/reply_list.html', {'reply_list':reply_list, 'form': form})