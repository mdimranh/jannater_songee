from django.contrib import admin
from django.contrib.auth.models import User

from .models import EmailConfirmed, Favourite
from django.contrib.auth.models import Group

admin.site.register(EmailConfirmed)
admin.site.register(Favourite)
admin.site.unregister(Group)
