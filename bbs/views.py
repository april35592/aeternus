from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Guest, Reply
from .forms import GuestForm
# Create your views here.

def bbs(request):
    page = request.GET.get('page', '1')
    reply_list = Reply.objects.order_by('-id')
    paginator = Paginator(reply_list, 5)
    page_obj = paginator.get_page(page)
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save()
            return redirect('bbs:bbs')
    else:
        form = GuestForm()
    return render(request, 'bbs/reply_list.html', {'reply_list': page_obj, 'form': form})
    