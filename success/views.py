from django.shortcuts import render
from .models import Post

def Success(request):
    post = Post.objects.all()
    return render(request, 'successpost.html', {'post':post, 'id':'couple'})
