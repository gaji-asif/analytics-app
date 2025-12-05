from django.db.models import Count, Q, Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from analytics.models import Blog, BlogView


class BlogViewsAPI(APIView):
    def get(self, request):
        #  Object type: user or country
        object_type = request.query_params.get('object_type', 'user')

        #  Time range filtering
        range_type = request.query_params.get('range', None)
        blogs = Blog.objects.all()

        if range_type == 'month':
            start_date = timezone.now() - timedelta(days=30)
            blogs = blogs.filter(created_at__gte=start_date)
        elif range_type == 'week':
            start_date = timezone.now() - timedelta(days=7)
            blogs = blogs.filter(created_at__gte=start_date)
        elif range_type == 'year':
            start_date = timezone.now() - timedelta(days=365)
            blogs = blogs.filter(created_at__gte=start_date)

        #  Dynamic filters (example: user, country)
        filters = Q()
        user_filter = request.query_params.get('user', None)
        country_filter = request.query_params.get('country', None)

        if user_filter:
            filters &= Q(user__username=user_filter)
        if country_filter:
            filters &= Q(country__name=country_filter)

        blogs = blogs.filter(filters)

        #  Grouping and aggregation
        if object_type == 'user':
            data = blogs.values('user__username').annotate(
                number_of_blogs=Count('id'),
                total_views=Count('views')
            )
            result = [
                {"x": d['user__username'], "y": d['number_of_blogs'], "z": d['total_views']}
                for d in data
            ]

        elif object_type == 'country':
            data = blogs.values('country__name').annotate(
                number_of_blogs=Count('id'),
                total_views=Count('views')
            )
            result = [
                {"x": d['country__name'], "y": d['number_of_blogs'], "z": d['total_views']}
                for d in data
            ]
        else:
            result = []

        return Response(result)