from django.urls import path
from . import views

urlpatterns = [
    path('create_biodata', views.CreateBiodata, name='create_biodata'),
    path('b_<str:id>', views.biodata, name='biodata'),
    path('b_<str:id>/edit', views.EditBiodata, name='editbiodata'),
    path('notifications', views.Notifications, name='notifications'),
    path('notification_seen_time', views.notifications_seen, name='notification_seen'),
]