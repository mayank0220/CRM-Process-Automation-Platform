```python
"""
URL configuration for the CRM project.

The `urlpatterns` list routes URLs to views.

For more information, see:
https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path

from leads import views


urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),

    # CRM Dashboard
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard",
    ),

    # Lead Management
    path(
        "all-leads/",
        views.all_leads,
        name="all_leads",
    ),

    # Lead Source Analytics
    path(
        "source-analysis/",
        views.source_analysis,
        name="source_analysis",
    ),
]
```
