from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import RedirectView
from allauth.account.views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('app.urls')),
    path('accounts/', include('allauth.urls')),
    path("", SignupView.as_view(), name="account_signup"),
    path("accounts/signup/", RedirectView.as_view(url="/")),
]

# DEBUG-ONLY URLS
if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
