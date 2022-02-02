from django.urls import path,include
from CbvApp import views

app_name = 'CbvApp'

urlpatterns = [
    path('index',views.index),
    path('',views.SchoolListView.as_view(),name='list'),
    path('(?P<pk>\d+)/',views.SchoolDetailView.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/(?P<pk>\d+)/',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/(?P<pk>\d+)/',views.SchoolDeleteView.as_view(),name='delete')
]