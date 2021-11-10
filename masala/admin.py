from django.contrib import admin

from .models import Hadith, masala, masala_catagory

admin.site.register(masala)
admin.site.register(masala_catagory)
admin.site.register(Hadith)
