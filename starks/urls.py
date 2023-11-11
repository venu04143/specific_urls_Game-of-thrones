from starks.views import*
from django.urls import path
app_name='you know nothing'

urlpatterns=[
    path('winterfell/',winterfell,name='winterfell'),
]