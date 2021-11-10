
from django.urls import path
from . import views

urlpatterns = [
    path('success', views.Success, name='success'),
]