from lannisters.views import*
from django.urls import path
app_name='you know nothing'

urlpatterns=[
    path('castlerock/',castlerock,name='castlerock')
]