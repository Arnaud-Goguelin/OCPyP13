from django.contrib import admin
from django.urls import path, include

from . import views


def trigger_error(request):
    return 1 / 0


urlpatterns = [
    path("", views.index, name="index"),
    path("profiles/", include("profile_app.urls")),
    path("lettings/", include("letting_app.urls")),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
]
