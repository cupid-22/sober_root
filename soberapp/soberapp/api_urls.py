"""
Sober App API URLs
"""
from django.urls import re_path, include

urlpatterns = [
    re_path("user/", include("users.urls")),
    re_path("literature/", include("literature.urls")),
]
