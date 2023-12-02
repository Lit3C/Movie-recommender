from django.urls import path
from . import views
from . import models

# app_name = 'user_app'

urlpatterns = [
    path('', views.index, name='app-index'),
    path('result', views.reco_sys, name='app-result'),
    path('search', views.filtrer_table, name='app-search'),
    path('list', views.list_view, name='app-list'),
    path('booking', views.booking, name='app-booking'),
    path('settings', views.settings, name='app-settings'),
    path('stats', views.stats, name='app-stats'),
]
