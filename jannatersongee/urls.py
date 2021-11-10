
from django.conf.urls import include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('biodata.urls')),
    path('', include('qa.urls')),
    path('', include('masala.urls')),
    path('', include('success.urls')),
    path('', include('management.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('accounts.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
]
