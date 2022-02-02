from django.conf.urls import url
from CbvApp import views

# app_name = 'CbvApp'

urlpatterns = [
    path('',views.index)
]