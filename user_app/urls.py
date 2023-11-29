from django.urls import path
from . import views
from . import models

urlpatterns = [
    path('', views.index, name='app-index'),
    path('result', views.reco_sys, name='app-result'),
    path('result', views.reco_sys_click, name='app-result-click'),
    path('search', views.search, name='app-search'),
    path('list', views.lst, name='app-list'),
    path('booking', views.booking, name='app-booking'),
    path('settings', views.settings, name='app-settings'),
    path('stats', views.stats, name='app-stats'),
]
