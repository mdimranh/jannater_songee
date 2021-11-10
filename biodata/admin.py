from django.contrib import admin
from django.contrib.auth import models

from .models import Biodata, Notification, Suggested, Request, Notification_seen


class BiodataAdmin(admin.ModelAdmin):
    search_fields=('name', 'present_address', 'birth_year', 'phone','email')
    list_filter=('present_address', 'marital_status', 'birth_year')
    list_display = ('name', 'present_address', 'birth_year', 'marital_status', 'email', 'publish')

admin.site.register(Biodata, BiodataAdmin)

class SuggestedAdmin(admin.ModelAdmin):
    list_filter=('user', 'suggested')
    list_display = ('user', 'suggested', 'percentage')

admin.site.register(Suggested, SuggestedAdmin)


class RequestAdmin(admin.ModelAdmin):
    list_filter=('user', 'request_user', 'accept')
    list_display = ('user', 'request_user', 'accept')

admin.site.register(Request, RequestAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_filter=('sender', 'receiver', 'type', 'created_at')
    list_display = ('sender', 'receiver', 'type', 'created_at')

admin.site.register(Notification, NotificationAdmin)


admin.site.register(Notification_seen)
