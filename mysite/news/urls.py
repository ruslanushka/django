from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>', get_category, name='category'),
    path('news/<int:news_id>', view_news, name='view_news')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()