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


def send_email_fun(request, message):
     send_email_to_client(message)
     return redirect('/')


def get_hostels(request):
    hostel_ids = list(Hostel.objects.values_list('id', flat=True))
    random_ids = random.sample(hostel_ids, min(len(hostel_ids), 5))
    hostels = Hostel.objects.filter(id__in=random_ids).prefetch_related('images')
    
    data = [{
        'id': hostel.id,
        'name': hostel.name,
        'slug': hostel.slug,
        'address': hostel.address,
        'price': hostel.price,
        'hostelType': hostel.hostelType,
        'images': [{'url': img.image.url} for img in hostel.images.all()]
    } for hostel in hostels]
    
    return JsonResponse({'hostels': data})

    

def main_page(request):
    #  products = Product.objects.filter(status='Publish').order_by('?')[:10]    
    #  hostels = Hostel.objects.filter()
    # Assuming you are using PostgreSQL, which supports random ordering directly
     hostels = Hostel.objects.order_by('?')[:5]

    # If the above method does not work or is inefficient on your database, use Python's random.sample
    # This method fetches all IDs, picks five randomly, and then retrieves these records.
    # Note: This method can be memory-intensive if the number of Hostel objects is large.
     hostel_ids = list(Hostel.objects.values_list('id', flat=True))
     random_ids = random.sample(hostel_ids, min(len(hostel_ids), 5))
     hostels = Hostel.objects.filter(id__in=random_ids)
     footer_urls = Blog.objects.filter()
     city = City.objects.filter()
     testimonials = Testimonial.objects.filter()
     seo = SEO.objects.get(name="home")
     context = {
          'hostels':hostels,
          'citites':city,
          'testimonials':testimonials,
          'seo':seo,
          'footer_urls':footer_urls
     }
     return render(request, 'index.html', context)

def about_us(request):
     city = City.objects.filter()
     footer_urls = Blog.objects.filter()
     seo = SEO.objects.get(name="about")
     testimonials = Testimonial.objects.filter()
     context ={
          'seo':seo,
          'citites':city,
          'testimonials':testimonials,
          'footer_urls':footer_urls
     }
     return render(request, 'about-us.html',context)

def why_us(request):
     city = City.objects.filter()
     footer_urls = Blog.objects.filter()
     seo = SEO.objects.get(name="why")
     testimonials = Testimonial.objects.filter()
     context ={
          'seo':seo,
          'citites':city,
          'testimonials':testimonials,
          'footer_urls':footer_urls
     }
     return render(request, 'why-ezstays.html',context)

def terms(request):
     city = City.objects.filter()
     footer_urls = Blog.objects.filter()
     seo = SEO.objects.get(name="terms")
     testimonials = Testimonial.objects.filter()
     context ={
          'seo':seo,
          'citites':city,
          'testimonials':testimonials,
          'footer_urls':footer_urls
     }
     return render(request, 'terms-and-conditions.html',context)

def privacy(request):
     city = City.objects.filter()
     footer_urls = Blog.objects.filter()
     seo = SEO.objects.get(name="privacy")
     testimonials = Testimonial.objects.filter()
     context ={
          'seo':seo,
          'citites':city,
          'testimonials':testimonials,
          'footer_urls':footer_urls
     }
     return render(request, 'privacy-policy.html',context)


def contact(request):
     seo = SEO.objects.get(name="contact")
     footer_urls = Blog.objects.filter()
     context ={
          'seo':seo,
          'footer_urls':footer_urls
     }
     return render(request, 'contact.html',context)

def hostel_single(request, slug):
    city = City.objects.filter()
    footer_urls = Blog.objects.filter()
    hostel = get_object_or_404(Hostel, slug=slug)
    nearby_places = hostel.nearby.split('\n')  # Splitting the string into a list by newline
    nearby_context = [place.split(' : ') for place in nearby_places if place]  # Further splitting each place into name and distance
    
    similarHostel = Hostel.objects.filter(city=hostel.city)

    hostels = Hostel.objects.order_by('?')[:5]

    # If the above method does not work or is inefficient on your database, use Python's random.sample
    # This method fetches all IDs, picks five randomly, and then retrieves these records.
    # Note: This method can be memory-intensive if the number of Hostel objects is large.
    hostel_ids = list(Hostel.objects.values_list('id', flat=True))
    random_ids = random.sample(hostel_ids, min(len(hostel_ids), 5))
    hostels = Hostel.objects.filter(id__in=random_ids)
    
    context = {
          'hostel':hostel,
          'citites':city,
          'nearby_context': nearby_context,
          'similar' : hostels,
          'footer_urls':footer_urls
     }
    return render(request, 'hostel-single.html',context)


def hostel_list(request):
    

    city_ = City.objects.filter()
    footer_urls = Blog.objects.filter()
    seo = SEO.objects.get(name="residences")
    # Get query parameters from request
    hostel_type = request.GET.get('hostel_type', '')  # corresponds to 'I’m looking for...' in the form
    location_id = request.GET.get('location', '')    # corresponds to 'Location' in the form
    bed_type = request.GET.get('bed', '')        # corresponds to 'Bedroom' in the form
    bath_type = request.GET.get('bath', '')      # corresponds to 'Washroom' in the form
    
    # Start with all hostels
    hostels_list = Hostel.objects.all()

    # Filter by hostel type if provided
    if hostel_type:
        hostels_list = hostels_list.filter(hostelType=hostel_type)

    # Filter by location if provided
    if location_id:
        city = City.objects.get(pk=location_id)
        hostels_list = hostels_list.filter(city=city)

    # Filter by bed type if provided
    if bed_type:
         # Get BedType instance(s) that match the description
        bed_types = BedType.objects.filter(type=bed_type)

        # Filter hostels by those bed types
        hostels_list = hostels_list.filter(beds__in=bed_types)

    # Filter by bath type if provided
    if bath_type:
        bath_types = BathType.objects.filter(type=bath_type)
        hostels_list = hostels_list.filter(bath__in=bath_types)

    # Set the number of hostels per page
    per_page = 5
    paginator = Paginator(hostels_list, per_page)
    page = request.GET.get('page')

    try:
        hostels = paginator.page(page)
    except PageNotAnInteger:
        hostels = paginator.page(1)
    except EmptyPage:
        hostels = paginator.page(paginator.num_pages)

    context = {
        'hostels': hostels,
        'citites':city_,
        'seo':seo,
        'footer_urls':footer_urls
    }
    return render(request, 'hostel-list.html', context)

def blog_list(request):
    seo = SEO.objects.get(name="blog")
    footer_urls = Blog.objects.filter()
    city = City.objects.filter()

    # Get tag from the query parameters
    tag_slug = request.GET.get('tag', None)

    if tag_slug:
        # Filter blogs by the specified tag
        blogs = Blog.objects.filter(tags__name=tag_slug)
    else:
        # Otherwise, retrieve all blogs
        blogs = Blog.objects.all()

    per_page = 2
    paginator = Paginator(blogs, per_page)
    page = request.GET.get('page')

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    tags = BlogTag.objects.all()


     # Assuming your Blog model has a 'published_date' field
    recent_blogs = Blog.objects.filter(status='Publish').order_by('-published_date')[:3]
    
    # Adding a count of blogs associated with each tag
    tags_with_count = []
    for tag in tags:
        count = tag.blog.count()  # `blog` is the related_name in BlogTag ManyToManyField
        tags_with_count.append((tag, count))

    context = {
        'blogs': blogs,
        'cities': city,
        'tags': tags_with_count,
        'recent_blogs': recent_blogs,
        'seo': seo,
        'footer_urls': footer_urls
    }
    return render(request, 'blog-list.html', context)

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    city = City.objects.filter()  # Assuming City is a model you have defined elsewhere
    footer_urls = Blog.objects.filter()  # Assuming this fetches relevant blog entries for the footer
    tags = BlogTag.objects.all()

     # Assuming your Blog model has a 'published_date' field
    recent_blogs = Blog.objects.filter(status='Publish').order_by('-published_date')[:3]
    
    # Adding a count of blogs associated with each tag
    tags_with_count = []
    for tag in tags:
        count = tag.blog.count()  # `blog` is the related_name in BlogTag ManyToManyField
        tags_with_count.append((tag, count))

    context = {
        'tags': tags_with_count,
        'recent_blogs': recent_blogs,
        'blog': blog,
        'cities': city,  # Typo corrected from 'citites' to 'cities'
        'footer_urls': footer_urls
    }

    return render(request, 'blog-details.html', context)

def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)

def _404(request):
    return render(request, '404.html')