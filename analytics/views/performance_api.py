from django.db.models import Count, Q, Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from analytics.models import Blog, BlogView

class PerformanceAnalyticsAPI(APIView):
    def get(self, request):

        compare = request.query_params.get('compare', 'month')  
        user_filter = request.query_params.get('user', None)
        country_filter = request.query_params.get('country', None)
        category_filter = request.query_params.get('category', None)

        filters = Q()

        if user_filter:
            filters &= Q(user__username=user_filter)
        if country_filter:
            filters &= Q(country__name=country_filter)
        if category_filter:
            filters &= Q(category__name=category_filter)

        # Decide comparison period
        now = timezone.now()

        if compare == 'day':
            periods = 30          # last 30 days
            delta = timedelta(days=1)
            date_format = "%Y-%m-%d"
        elif compare == 'week':
            periods = 12          # last 12 weeks
            delta = timedelta(weeks=1)
            date_format = "Week %W"
        elif compare == 'year':
            periods = 5           # last 5 years
            delta = timedelta(days=365)
            date_format = "%Y"
        else:
            compare = 'month'
            periods = 12          # last 12 months
            delta = timedelta(days=30)
            date_format = "%Y-%m"

        results = []
        previous_views = None
        end_date = now

        for i in range(periods):

            start_date = end_date - delta

            # Count blogs created in this period
            blogs = Blog.objects.filter(
                created_at__gte=start_date,
                created_at__lt=end_date
            ).filter(filters)

            blog_count = blogs.count()

            # Count views in this period
            views = BlogView.objects.filter(
                viewed_at__gte=start_date,
                viewed_at__lt=end_date,
                blog__in=blogs
            ).count()

            # Growth / Decline %
            if previous_views is None:
                growth = None
            else:
                if previous_views == 0:
                    growth = 100 if views > 0 else 0
                else:
                    growth = round(((views - previous_views) / previous_views) * 100, 2)

            results.append({
                "x": f"{start_date.strftime(date_format)} ({blog_count} blogs)",
                "y": views,
                "z": growth
            })

            previous_views = views
            end_date = start_date

        return Response(results[::-1])  