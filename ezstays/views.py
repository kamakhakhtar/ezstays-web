# ========= DJANGO ===========
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from myapp.models import Hostel,Testimonial, Blog,BlogTag,SEO,City, BedType,BathType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
import random
from django.http import JsonResponse
from .utlis import send_email_to_client
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
import os
from django.core.cache import cache
from django.conf import settings


from django.template.loader import render_to_string

def get_seo_for_page(page_name):
    return SEO.objects.get(name=page_name)

def get_recent_blogs():
    return Blog.objects.filter(status='Publish').order_by('-published_date')[:3]

def get_tags_with_counts():
    tags = BlogTag.objects.all()
    return [(tag, tag.blog_set.count()) for tag in tags]


def send_email_fun(request, message):
     send_email_to_client(message)
     return redirect('/')



def get_hostels(request):
    hostel_ids = list(Hostel.objects.values_list('id', flat=True))
    random_ids = random.sample(hostel_ids, min(len(hostel_ids), 5))
    hostels = Hostel.objects.filter(id__in=random_ids).prefetch_related('images')    
     # Serialize the hostels data into JSON
    hostels_data = []
    for hostel in hostels:
        hostel_dict = {
            "id": hostel.id,
            "name": hostel.name,
            "slug": hostel.slug,
            "address": hostel.address,
            "price": round(hostel.price/12)-1,
            "hostelType": hostel.hostelType,
            "image_url": hostel.images.all()[0].image.url if hostel.images.all() else None
        }
        hostels_data.append(hostel_dict)

    return JsonResponse({'hostels': hostels_data})

    
def main_page(request):
    seo = get_seo_for_page("home")
    return render(request, 'index.html', {'seo': seo})

def landing_page(request):
    seo = get_seo_for_page("home")
    return render(request, 'landing.html', {'seo': seo})

def about_us(request):
    seo = get_seo_for_page("about")
    testimonials = Testimonial.objects.all()
    return render(request, 'about-us.html', {
        'seo': seo,
        'testimonials': testimonials
    })

def why_us(request):
    seo = get_seo_for_page("why")
    return render(request, 'why-ezstays.html', {'seo': seo})

def terms(request):
    seo = get_seo_for_page("terms")
    return render(request, 'terms-and-conditions.html', {'seo': seo})

def refund(request):
    seo = get_seo_for_page("refund")
    return render(request, 'refund-and-cancellation.html', {'seo': seo})

def privacy(request):
    seo = get_seo_for_page("privacy")
    return render(request, 'privacy-policy.html', {'seo': seo})

def contact(request):
    seo = get_seo_for_page("contact")
    footer_urls = Blog.objects.all()
    return render(request, 'contact.html', {
        'seo': seo,
        'footer_urls': footer_urls
    })

def blog_list(request):
    seo = get_seo_for_page("blog")
    tag_slug = request.GET.get('tag')
    blogs = Blog.objects.filter(tags__name=tag_slug) if tag_slug else Blog.objects.all()
    
    paginator = Paginator(blogs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog-list.html', {
        'blogs': page_obj,
        'tags': get_tags_with_counts(),
        'recent_blogs': get_recent_blogs(),
        'seo': seo
    })

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog-details.html', {
        'blog': blog,
        'tags': get_tags_with_counts(),
        'recent_blogs': get_recent_blogs(),
    })

def hostel_single(request, slug):
    hostel = get_object_or_404(Hostel, slug=slug)
    nearby_places = [place.split(' : ') for place in hostel.nearby.split('\n') if place]

    # Optimize by using related_name and select_related if foreign keys exist for performance
    similar_hostels = Hostel.objects.filter(city=hostel.city).exclude(id=hostel.id)[:5]
    
    context = {
        'hostel': hostel,
        'nearby_context': nearby_places,
        'similar': similar_hostels,
    }
    return render(request, 'hostel-single.html', context)

def hostel_list(request):
    # Generate a unique cache key based on query parameters
    cache_key = f"hostel_list_{request.GET.urlencode()}"
    cached_data = cache.get(cache_key)

    if cached_data:
        return render(request, 'hostel-list.html', cached_data)

    seo = get_seo_for_page("residences")
    hostels_list = Hostel.objects.all()

    # Chain filters to refine search based on provided query parameters
    if hostel_type := request.GET.get('hostel_type'):
        hostels_list = hostels_list.filter(hostelType=hostel_type)
    if location_id := request.GET.get('location'):
        hostels_list = hostels_list.filter(city__id=location_id)
    if bed_type := request.GET.get('bed'):
        hostels_list = hostels_list.filter(beds__type=bed_type)
    if bath_type := request.GET.get('bath'):
        hostels_list = hostels_list.filter(bath__type=bath_type)

    paginator = Paginator(hostels_list, 5)  # 5 hostels per page
    page_number = request.GET.get('page')
    try:
        hostels = paginator.get_page(page_number)
    except PageNotAnInteger:
        hostels = paginator.page(1)
    except EmptyPage:
        hostels = paginator.page(paginator.num_pages)

    context = {
        'hostels': hostels,
        'seo': seo,
    }

    cache.set(cache_key, context, timeout=60*60*24)  # Cache for 24 hours
    return render(request, 'hostel-list.html', context)

# ============= Blog ==========

from django.db.models import Count

def get_tags_with_counts():
    tags = BlogTag.objects.all()
    return [(tag, tag.blogs.count()) for tag in tags]


def get_recent_blogs():
    return Blog.objects.filter(status='Publish').order_by('-published_date')[:3]


def blog_list(request):
    seo = SEO.objects.get(name="blog")
    tag_slug = request.GET.get('tag')

    if tag_slug:
        blogs = Blog.objects.filter(tags__name=tag_slug)
    else:
        blogs = Blog.objects.all()

    paginator = Paginator(blogs, 2)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'blog-list.html', {
        'blogs': blogs,
        'tags': get_tags_with_counts(),
        'recent_blogs': Blog.objects.filter(status='Publish').order_by('-published_date')[:3],
        'seo': seo,
    })




def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    
    context = {
        'blog': blog,
        'tags': get_tags_with_counts(),
        'recent_blogs': get_recent_blogs(),
    }
    return render(request, 'blog-details.html', context)


#  ===== 404 Error Page =============

def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)

def _404(request):
    return render(request, '404.html')

def sitemap(request):
    return render(request, 'sitemap.xml')

def googleadf(request):
    return render(request, 'googleadf5899225f786cc.html')

# ====================================



# ======= Footer Link ==============


def get_seofooter_urls(request):
    cache_key = 'seo_footer_urls'
    footer_urls = cache.get(cache_key)
    
    if footer_urls is None:
        footer_data = Blog.objects.filter(status='Seo').values('title', 'slug')
        footer_urls = list(footer_data)
        cache.set(cache_key, footer_urls, timeout=60*60*24)  # Cache for 24 hours

    return JsonResponse({'footer_urls': footer_urls})


# =========================================
def get_cities(request):
    cache_key = 'city_list'
    city_list = cache.get(cache_key)

    if city_list is None:
        cities = City.objects.all().values('pk', 'city')
        city_list = list(cities)
        cache.set(cache_key, city_list, timeout=60*60*24)  # Cache for 24 hours

    return JsonResponse({'cities': city_list})

# ======== Testimony ============
def get_testimonials(request):
    cache_key = 'testimonial_list'
    testimonial_list = cache.get(cache_key)

    if testimonial_list is None:
        testimonials = Testimonial.objects.all()
        testimonial_list = [
            {
                'pk': testimonial.pk,
                'image_url': request.build_absolute_uri(testimonial.image.url),
                'student_name': testimonial.student_name,
                'student_addr': testimonial.student_addr,
                'review': testimonial.review,
            }
            for testimonial in testimonials
        ]
        cache.set(cache_key, testimonial_list, timeout=60*60*24)  # Cache for 24 hours

    return JsonResponse({'testimonials': testimonial_list})

def proxy_request(request):
    url = 'https://cdnml.global-cache.online/cfgpl_ae_5b.json'
    params = {'t': '2024-07-05T15:2'}
    response = requests.get(url, params=params)
    return JsonResponse(response.json())
