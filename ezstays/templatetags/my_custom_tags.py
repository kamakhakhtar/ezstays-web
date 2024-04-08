from django import template
# from myapp.models import Product

register = template.Library()

@register.filter(name='round')
def roundPrice(value):
    return round(value) 


@register.filter(name='monthly')
def roundPrice(value):
    return round(value/12) 

