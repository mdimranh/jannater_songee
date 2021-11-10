from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Message
from django.views.decorators.csrf import csrf_exempt

def Contact(request):
    return render(request, 'management/contact.html')

@csrf_exempt
def message(request):
    message = Message(
        name = request.POST['name'],
        subject = request.POST['subject'],
        message = request.POST['message'],
    )
    message.save()
    return HttpResponse("success")
