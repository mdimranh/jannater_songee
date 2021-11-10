from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_filter=('send_at', 'seen', 'action')
    list_display = ('name', 'subject', 'seen', 'action')
admin.site.register(Message, MessageAdmin)
