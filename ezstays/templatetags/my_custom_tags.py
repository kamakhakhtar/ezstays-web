from django import template
# from myapp.models import Product

register = template.Library()

@register.filter(name='round')
def roundPrice(value):
    return round(value) 


@register.filter(name='monthly')
def roundPrice(value):
    return round(value/12)-1 

@register.filter(name='gender')
def checkGender(value):
    if(value == "Boys"):
        return "boys"
    else:
        return "girls"
    
from bs4 import BeautifulSoup
@register.filter(name='iframe_src')
def extract_iframe_src(html_content):
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the first iframe in the content
    iframe = soup.find('iframe')
    
    # Return the src attribute of the iframe
    if iframe:
        return iframe.get('src')
    else:
        return "No iframe found"

@register.filter(name='batch_three')
def batch_three(value):
    # Calculate the length of each part, trying to distribute the items as evenly as possible
    total_len = len(value)
    size = (total_len + 2) // 2  # Use integer division rounding up

    return [value[i:i + size] for i in range(0, total_len, size)]