# ========= DJANGO ===========
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from myapp.models import Hostel,Testimonial, Blog,BlogTag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests

def main_page(request):
    #  products = Product.objects.filter(status='Publish').order_by('?')[:10]    
     hostels = Hostel.objects.filter()
     testimonials = Testimonial.objects.filter()
     context = {
          'hostels':hostels,
          'testimonials':testimonials,
     }
     return render(request, 'index.html', context)

def about_us(request):
     return render(request, 'about-us.html')


def contact(request):
     return render(request, 'contact.html')

def hostel_single(request, slug):
    
    hostel = get_object_or_404(Hostel, slug=slug)
    nearby_places = hostel.nearby.split('\n')  # Splitting the string into a list by newline
    nearby_context = [place.split(' : ') for place in nearby_places if place]  # Further splitting each place into name and distance
    
    similarHostel = Hostel.objects.filter(city=hostel.city)

    imageCount = hostel.images.count()
    context = {
          'hostel':hostel,
          'nearby_context': nearby_context,
          'similar' : similarHostel
     }
    return render(request, 'hostel-single.html',context)


def hostel_list(request):
    hostels_list = Hostel.objects.all()

    # Set the number of hostels per page
    per_page = 5

    # Create a Paginator object
    paginator = Paginator(hostels_list, per_page)

    # Get the page number from the request GET parameters
    page = request.GET.get('page')

    try:
        # Try to fetch the page number
        hostels = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        hostels = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        hostels = paginator.page(paginator.num_pages)

    context = {
        'hostels': hostels
    }
    return render(request, 'hostel-list.html', context)

def blog_list(request):
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
          'tags':tags
     }
     return render(request, 'blog-list.html', context)

def blog_detail(request,slug):
     blog = get_object_or_404(Blog, slug=slug)
     tags = BlogTag.objects.all()
     context = {
          'blog':blog,
          'tags':tags,
     }
     return render(request, 'blog-details.html', context)
