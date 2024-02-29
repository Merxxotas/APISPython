from django.contrib import admin
from django.urls import path

from jenkinsMain.views import create_get_names, update_name
urlpatterns = [
    path('name/', create_get_names),
    path('name/<int:name_id>/', update_name),
    # path('name/', listNames),
]
