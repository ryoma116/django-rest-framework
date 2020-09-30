from django.contrib import admin

# Register your models here.
from app.models import TweetModel

admin.site.register(TweetModel)
