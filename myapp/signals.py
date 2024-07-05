# signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Hostel, BedType, BathType, City, Testimonial

# Cache keys
HOSTEL_LIST_CACHE_KEY = 'hostel_list_*'
CITY_LIST_CACHE_KEY = 'city_list'
TESTIMONIAL_LIST_CACHE_KEY = 'testimonial_list'

# Clear cache for hostels
@receiver(post_save, sender=Hostel)
@receiver(post_delete, sender=Hostel)
@receiver(post_save, sender=BedType)
@receiver(post_delete, sender=BedType)
@receiver(post_save, sender=BathType)
@receiver(post_delete, sender=BathType)
@receiver(post_save, sender=City)
@receiver(post_delete, sender=City)
def clear_hostel_list_cache(sender, **kwargs):
    keys = cache.keys(HOSTEL_LIST_CACHE_KEY)
    cache.delete_many(keys)

# Clear cache for cities
@receiver(post_save, sender=City)
@receiver(post_delete, sender=City)
def clear_city_cache(sender, **kwargs):
    cache.delete(CITY_LIST_CACHE_KEY)

# Clear cache for testimonials
@receiver(post_save, sender=Testimonial)
@receiver(post_delete, sender=Testimonial)
def clear_testimonial_cache(sender, **kwargs):
    cache.delete(TESTIMONIAL_LIST_CACHE_KEY)
