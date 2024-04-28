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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main'),
    path('send-email/<str:message>', views.send_email_fun, name='send_email_fun'),
    path('about-us/', views.about_us, name='about'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('terms-and-conditions/', views.terms, name='terms'),
    path('why-ezstays/', views.why_us, name='why'),
    path('contact/', views.contact, name='about'),
    path('house/<slug:slug>/', views.hostel_single, name='hostel_single'),
    # path('hostel-single/', views.hostel_single, name='hostelSingle'),
    path('our-residences/', views.hostel_list, name='hostelList'),
    path('blogs/', views.blog_list, name='blogList'),
    path('blog/<slug:slug>/', views.blog_detail, name='blogDetail'),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# handler404 = custom_404

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
