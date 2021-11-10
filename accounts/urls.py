from django.urls import path
from . import views

urlpatterns = [
    path('auth', views.Accounts, name='create_account'),
    path('logout/', views.logout, name="logout"),
    path('account/verify/<str:activation_key>', views.email_confirm, name='email_confirm'),
    path('account/pass_recover/<str:activation_key>', views.password_recover, name='password_recover'),
    path('profile/favourite', views.Favourite_bio, name='email_confirm'),
    path('settings', views.Settings, name='settings'),
]