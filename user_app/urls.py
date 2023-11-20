from django.urls import path
from . import views

urlpatterns = [
    path('area-chart', views.area_chart, name='app-area-chart'),
    path('', views.index, name='app-index'),
]
