from django.urls import path,include
from . import views

urlpatterns = [
    path('data_view/', views.view,name='event_data_view'),
    path('data_view/school', views.view_school,name='view_school')


]
