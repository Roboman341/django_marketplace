"""puddle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# this is needed for viewing the images, should not be used for production
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(
        "", include("core.urls")
    ),  # it'll loop through all the urls in puddle/core/urls.py until goes to the next path
    path(
        "items/", include("item.urls")
    ),  # all urls that starts with item will go to item/urls.py
    path("dashboard", include("dashboard.urls")),
    path("inbox/", include("conversation.urls")),
    path("admin/", admin.site.urls),
] + static(  # this for dev only also
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
