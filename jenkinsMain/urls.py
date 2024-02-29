from django.contrib import admin
from django.urls import path

from jenkinsMain.views import createGetNames

urlpatterns = [
    path('name/', createGetNames),
    # path('name/', listNames),
]
