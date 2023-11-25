from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def movies(request):
    return render(request, 'movies.html')

def casting(request):
    return render(request, 'casting.html')

def market(request):
    return render(request, 'market.html')

def userstats(request):
    return render(request, 'userstats.html')