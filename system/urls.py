from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from .views import DrawMenuView

urlpatterns = [
    path('<name>', DrawMenuView.as_view())
]
