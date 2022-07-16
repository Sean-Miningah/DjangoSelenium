from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, 'home.html', {
        # wer use POST.get('item_text', '') to cater for get request
        'new_item_text': request.POST.get('item_text', '')
    })

