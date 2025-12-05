from django.urls import path
from .views import BlogViewsAPI, TopAnalyticsAPI, PerformanceAnalyticsAPI

urlpatterns = [
    path('blog-views/', BlogViewsAPI.as_view()),
    path('top/', TopAnalyticsAPI.as_view()), 
    path('performance/', PerformanceAnalyticsAPI.as_view()),
]
