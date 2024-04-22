from django.contrib import admin
from .models import *

class ImagesTublerinLine(admin.TabularInline):
    model= Images


class HostelAdmin(admin.ModelAdmin):
    inlines =[ImagesTublerinLine]


# class AmmenitiesTublerinLine(admin.TabularInline):
#     model= Amenity

    # list_display = ('name', 'unique_id', 'price', 'condition', 'stock', 'status')

# Register your models here.
admin.site.register(Blog)
admin.site.register(SEO)
admin.site.register(City)
admin.site.register(Amenity)
admin.site.register(BlogTag)
admin.site.register(Hostel,HostelAdmin)
admin.site.register(Testimonial)
admin.site.register(Comment)
admin.site.register(BedType)

