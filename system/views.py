

from django.shortcuts import render
from django.views import View


# Create your views here.

class DrawMenuView(View):
    def get(self, request, name):
        return render(request, 'system/menu.html', context={'name': name})
