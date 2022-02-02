from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

def index(request):
    return render(request,'index.html')


class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')