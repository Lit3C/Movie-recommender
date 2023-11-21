from django.http import HttpResponse
from django.shortcuts import render

def mainhome(request):
    return render(request, 'index.html')