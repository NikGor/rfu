"""rfu URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rfu.blog import views
from rfu.views import IndexView, GDPRView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('main_page/', include('rfu.main_page.urls')),
    path('blog/', include('rfu.blog.urls')),
    path('about/', include('rfu.about.urls')),
    path('api/like/<int:post_id>/', views.LikeView.as_view(), name='like_post'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('gcdp/', GDPRView.as_view(), name='gdpr'),
    path("cookies/", include("cookie_consent.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)