from django.db.models import Count, Q, Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from analytics.models import Blog, BlogView

class TopAnalyticsAPI(APIView):
    def get(self, request):
        top_type = request.query_params.get('top', 'user') 
        limit = int(request.query_params.get('limit', 10))

        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)

        blogs = Blog.objects.all()

        # Apply time range filters
        if start_date:
            blogs = blogs.filter(created_at__gte=start_date)
        if end_date:
            blogs = blogs.filter(created_at__lte=end_date)

        # Dynamic filters
        filters = Q()
        user_filter = request.query_params.get('user', None)
        country_filter = request.query_params.get('country', None)
        category_filter = request.query_params.get('category', None)

        if user_filter:
            filters &= Q(user__username=user_filter)
        if country_filter:
            filters &= Q(country__name=country_filter)
        if category_filter:
            filters &= Q(category__name=category_filter)

        blogs = blogs.filter(filters)

        # Grouping and aggregation
        if top_type == 'user':
            data = blogs.values('user__username').annotate(
                total_views=Sum('views')
            ).order_by('-total_views')[:limit]

            result = [
                {"name": d['user__username'], "views": d['total_views']}
                for d in data
            ]

        elif top_type == 'country':
            data = blogs.values('country__name').annotate(
                total_views=Sum('views')
            ).order_by('-total_views')[:limit]

            result = [
                {"name": d['country__name'], "views": d['total_views']}
                for d in data
            ]

        elif top_type == 'blog':
            data = blogs.values('title').annotate(
                total_views=Sum('views')
            ).order_by('-total_views')[:limit]

            result = [
                {"name": d['title'], "views": d['total_views']}
                for d in data
            ]
        else:
            result = []

        return Response(result)