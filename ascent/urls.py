"""ascent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path(
        "login/", RedirectView.as_view(pattern_name="magic-link:create"), name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("magic-link/", include("magic_links.urls"), name="magic-link"),
    path("pingpong/", include("pingpong.urls"), name="pingpong"),
    path("reflections/", include("reflections.urls"), name="reflections"),
    path("mileage_tracker/", include("mileage_tracker.urls"), name="mileage_tracker"),
    path("shoutouts/", include("shoutouts.urls"), name="shoutouts")
]
