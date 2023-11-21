from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/app.html')

def search(request):
    return render(request, 'app/search.html')

def list(request):
    return render(request, 'app/list.html')

def booking(request):
    return render(request, 'app/booking.html')

def setup(request):
    return render(request, 'app/setup.html')

def stats(request):
    return render(request, 'app/stats.html')
