from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def total_views(request):
    return JsonResponse({
        "labels": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        "data": [12545, 19512, 37897, 54574, 29564, 44547]
    })