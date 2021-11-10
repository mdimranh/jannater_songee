from django.urls import path
from . import views


urlpatterns = [
    path('qa', views.qa, name='qa'),
]