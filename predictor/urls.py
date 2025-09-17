from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # povezuje index stranicu sa views.py funkcijom
]
