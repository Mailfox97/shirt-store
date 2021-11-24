"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.sitemaps import GenericSitemap
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView
from shirts.sitemaps import StaticViewSitemap
sitemaps = {
    'static': StaticViewSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shirts.urls')),
    path('paypal/',include('paypal.standard.ipn.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path("robots.txt", include('robots.urls')),  #add the robots.txt file
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
