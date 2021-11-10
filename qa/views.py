from django.shortcuts import render
from .models import qa as qs

def qa(request):
    qans = qs.objects.all()
    context = {
        'title': 'প্রশ্ন ও উত্তর',
        'qa': qans
    }
    return render(request, 'qa.html', context)
