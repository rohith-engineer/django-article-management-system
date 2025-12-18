from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
    path("accounts/", include("allauth.urls")),
    
]

# 🔥 REQUIRED for django-browser-reload
urlpatterns += [
    path("__reload__/", include("django_browser_reload.urls")),
]
