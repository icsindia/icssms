from django.contrib import admin
from data import urls
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("data.urls")),
    path("exam/", include("exam.urls")),
]
