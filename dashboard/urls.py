from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard-index'),
    path('movies', views.movies, name='dashboard-movies'),
    path('casting', views.casting, name='dashboard-casting'),
    path('market', views.market, name='dashboard-market'),
    path('userstats', views.userstats, name='dashboard-userstats'),
]