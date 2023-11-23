from django.urls import path
from . import views

urlpatterns = [
    path('total-views', views.total_views, name='api-total-views'),
]
