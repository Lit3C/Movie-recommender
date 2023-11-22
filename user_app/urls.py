from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app-index'),
    # path('datatables', views.datatables, name='app-datatables'),
    # path('area-chart', views.area_chart, name='app-area-chart'),
    path('search', views.search, name='app-search'),
    path('list', views.list, name='app-list'),
    path('booking', views.booking, name='app-booking'),
    path('settings', views.settings, name='app-settings'),
    path('stats', views.stats, name='app-stats'),
]
