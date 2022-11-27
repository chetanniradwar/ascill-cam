from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def videoCam(request):
    return render(request, 'ascii_cam/index.html')