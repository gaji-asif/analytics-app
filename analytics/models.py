from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # used for month/week/year comparison

    def __str__(self):
        return self.title


class BlogView(models.Model):
    
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="views")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    viewed_at = models.DateTimeField(auto_now_add=True)  # for  all time-range filtering

    def __str__(self):
        return f"View → {self.blog.title}"
