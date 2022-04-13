from django.urls import path, include

from project import views

urlpatterns = [
    path('', views.my_project)
]
