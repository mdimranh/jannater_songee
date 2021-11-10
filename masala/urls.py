from django.urls import path
from . import views

urlpatterns = [
    path('masala', views.Masala, name="masala"),
    path('masala/<str:id>', views.GetMasala, name="getmasala"),
    path('masala/catagory/<str:title>', views.MasalaCat, name="masalacat")
]
