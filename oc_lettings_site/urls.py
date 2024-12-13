from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("profiles/", include("profile_app.urls")),
    path("lettings/", include("letting_app.urls")),
    path("admin/", admin.site.urls),
    # route to trigger an error for testing
    path("sentry-debug/", views.trigger_error),
]
