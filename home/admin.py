from django.contrib import admin
from .models import Quotes

admin.site.register(Quotes)

admin.site.site_header = 'Jannater Songee'
admin.site.site_title = 'JannaterSongee'
admin.site.index_title = 'Admin'