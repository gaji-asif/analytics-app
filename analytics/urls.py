from django.urls import path
from .views import BlogViewsAPI, TopAnalyticsAPI

urlpatterns = [
    path('blog-views/', BlogViewsAPI.as_view()),
    path('top/', TopAnalyticsAPI.as_view()), 
    # path('performance/', PerformanceAPI.as_view()),
]
