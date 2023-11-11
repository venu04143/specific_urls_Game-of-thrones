from django.urls import path
from baratheons.views import *
app_name='nothing'

urlpatterns=[
    path('kingslanding/',kingslanding,name='kingslanding')
]