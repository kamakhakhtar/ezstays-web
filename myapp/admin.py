from django.contrib import admin

from django.urls import reverse
from django.utils.html import format_html

from .models import *

class ImagesTublerinLine(admin.TabularInline):
    model= Images


class HostelAdmin(admin.ModelAdmin):
    inlines =[ImagesTublerinLine]


# class AmmenitiesTublerinLine(admin.TabularInline):
#     model= Amenity

    # list_display = ('name', 'unique_id', 'price', 'condition', 'stock', 'status')

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('get_serial_no', 'title', 'status', 'published_date')
    list_filter = ('status', 'published_date')
    search_fields = ('title',)

    def get_serial_no(self, obj):
        return obj.pk
    get_serial_no.short_description = 'Serial No.'

admin.site.register(Blog, BlogAdmin)

class SEOAdmin(admin.ModelAdmin):
    list_display = ('get_serial_no', 'name', 'title')
    search_fields = ('name', 'title')

    def get_serial_no(self, obj):
        return obj.pk
    get_serial_no.short_description = 'Serial No.'

admin.site.register(SEO, SEOAdmin)
class HostelAdmin(admin.ModelAdmin):
    list_display = ('get_serial_no', 'name', 'city', 'price', 'get_slug_url')
    search_fields = ('name', 'city__name', 'price', 'slug')

    def get_serial_no(self, obj):
        return obj.pk
    get_serial_no.short_description = 'Serial No.'

    def get_slug_url(self, obj):
        url = reverse('hostel_single', args=[obj.slug])  # Assuming 'hostel_single' is the URL name for the hostel detail page
        return format_html('<a href="{}" target="_blank">{}</a>', url, url)
    get_slug_url.short_description = 'Slug (URL)'

admin.site.register(Hostel, HostelAdmin)

admin.site.register(City)
admin.site.register(Amenity)
admin.site.register(BlogTag)
admin.site.register(Testimonial)
admin.site.register(Comment)
admin.site.register(BedType)
admin.site.register(BathType)
admin.site.register(SentEmail)

