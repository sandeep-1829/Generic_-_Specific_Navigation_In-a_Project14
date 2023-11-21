from django.urls import path
from specific.views import *
app_name='specific'
urlpatterns=[
    path('prabhas/',prabhas,name='prabhas'),
    path('salaar/',salaar,name='salaar'),
]