from django.urls import path
from . import views
from rest_framework import routers
from .views import TweetViewSet

tweet_router = routers.DefaultRouter()
tweet_router.register(r'tweets', TweetViewSet)

