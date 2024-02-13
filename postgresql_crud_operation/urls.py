from django.contrib import admin
from django.urls import path 
from .views import *

urlpatterns = [
    path('' , add_data , name='add_data'),
    path('show_data/' , view_data , name='view_data'),
    path('show_data/update_data/<id>/' , update_data , name="update_data"),
    path('show_data/delete_data/<id>/' , delete_data , name="delete_data")
]
