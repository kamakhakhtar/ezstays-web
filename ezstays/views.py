# ========= DJANGO ===========
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from myapp.models import Hostel,Testimonial, Blog,BlogTag,SEO,City, BedType,BathType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests

from .utlis import send_email_to_client


def send_email_fun(request, message):
     send_email_to_client(message)
     return redirect('/')



def main_page(request):
    #  products = Product.objects.filter(status='Publish').order_by('?')[:10]    
     hostels = Hostel.objects.filter()
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

    imageCount = hostel.images.count()
    context = {
          'hostel':hostel,
          'citites':city,
          'nearby_context': nearby_context,
          'similar' : similarHostel,
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
     blog_list = Blog.objects.all()

     # Set the number of hostels per page
     per_page = 5

     # Create a Paginator object
     paginator = Paginator(blog_list, per_page)

     # Get the page number from the request GET parameters
     page = request.GET.get('page')

     try:
          # Try to fetch the page number
          hostels = paginator.page(page)
     except PageNotAnInteger:
          # If page is not an integer, deliver first page.
          blogs = paginator.page(1)
     except EmptyPage:
          # If page is out of range, deliver last page of results.
          blogs = paginator.page(paginator.num_pages)

     tags = BlogTag.objects.all()
     context = {
          'blogs': blogs,
          'citites':city,
          'tags':tags,
          'seo':seo,
          'footer_urls':footer_urls
     }
     return render(request, 'blog-list.html', context)

def blog_detail(request,slug):
     city = City.objects.filter()
     footer_urls = Blog.objects.filter()
     blog = get_object_or_404(Blog, slug=slug)
     tags = BlogTag.objects.all()
     context = {
          'blog':blog,
          'citites':city,
          'tags':tags,
          'footer_urls':footer_urls
     }

     return render(request, 'blog-details.html', context)
