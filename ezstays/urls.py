"""
URL configuration for ezstays project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.shortcuts import render
from django.conf.urls import handler404

from django.urls import re_path
from django.views.static import serve
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', views.main_page, name='main'),
    path('landing/', views.landing_page, name='landing'),
    path('admin/', admin.site.urls),
    path('send-email/<str:message>', views.send_email_fun, name='send_email_fun'),
    path('about-us/', views.about_us, name='about'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('terms-and-conditions/', views.terms, name='terms'),
    path('refund-and-cancellation/', views.refund, name='refund'),
    path('why-ezstays/', views.why_us, name='why'),
    path('contact/', views.contact, name='about'),
    path('sitemap.xml/', views.sitemap, name='about'),
    path('googleadf5899225f786cc.html', views.googleadf, name='about'),
    path('house/<slug:slug>/', views.hostel_single, name='hostel_single'),
    path('hostel/<slug:slug>/', views.hostel_single, name='hostel_single'),
    path('house/<slug:slug>', views.hostel_single, name='hostel_single'),
    path('our-residences/', views.hostel_list, name='hostelList'),
    path('blogs/', views.blog_list, name='blogList'),
    path('blog/<slug:slug>/', views.blog_detail, name='blogDetail'),
    path('<slug:slug>/', views.blog_detail, name='blogDetail'),
    path('ajax/seofooter-urls/', views.get_seofooter_urls, name='ajax-seofooter-urls'),
    path('ajax/get-cities/', views.get_cities, name='ajax-get-cities'),
    path('ajax/get-testimonials/', views.get_testimonials, name='ajax-get-testimonials'),
    path('ajax/get-hostels/', views.get_hostels, name='get-hostels'),
    path('er/', views._404, name="404"),
     path('proxy/', views.proxy_request, name='proxy_request'),
]

# Serve media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files in both development and production modes
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # For production, you might still want to configure static file serving via Django for simplicity
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', cache_page(86400)(serve), {'document_root': settings.STATIC_ROOT}),
    ]

# Ensure cache_page decorator is applied correctly for both modes
urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', cache_page(86400)(serve), {'document_root': settings.STATIC_ROOT}),
]

# handler404 = custom_404
handler404 = views.custom_404


