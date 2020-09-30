from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from app.urls import tweet_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(tweet_router.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
