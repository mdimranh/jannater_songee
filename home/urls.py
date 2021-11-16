from django.urls import path
from .views import Accept, Cancel, Reject, GetReject, home, All, Male, Female, Suggest, Send, Get, Love


urlpatterns = [
    path('', home, name='home'),
    path('all_biodata', All, name='all'),
    path('male_biodata', Male, name='male'),
    path('female_biodata', Female, name='female'),
    path('favourite_biodata', Love.as_view(), name='love'),
    path('suggested_biodata', Suggest, name='suggest'),
    path('b_<int:id>/send', Send, name='send'),
    path('b_<int:id>/get', Get, name='get'),
    path('b_<int:id>/accept', Accept, name='accept'),
    path('b_<int:id>/reject', Reject, name='reject'),
    path('b_<int:id>/getreject', GetReject, name='getreject'),
    path('b_<int:id>/cancel', Cancel, name='cancel'),
]