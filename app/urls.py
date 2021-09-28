from django.urls import path, include, re_path
from trener import urls

urlpatterns = [
    path(r'^api_auth/', include('rest_framework.urls')),
    path('api/', include(urls))
]