from django import template
from urllib.parse import urlparse, parse_qs

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

@register.filter(name='hostel_type')
def hostel_type(url, check_value):
    # Parse the URL to get the query string part
    parsed_url = urlparse(url)

    # Extract the query parameters into a dictionary
    query_params = parse_qs(parsed_url.query)

    # Get the value of 'hostel_type'
    current_type = query_params.get('hostel_type', [None])[0]

    # Return "selected" if the current type matches the check_value, otherwise return an empty string
    return "selected" if current_type == check_value else ""


@register.filter(name='location')
def location(url, check_value):
    # Parse the URL to get the query string part
    parsed_url = urlparse(url)

    # Extract the query parameters into a dictionary
    query_params = parse_qs(parsed_url.query)

    # Get the value of 'location' and convert it to string
    current_location = query_params.get('location', [None])[0]
    
    # Check_value is expected to be an integer since it's a primary key, convert it to string for comparison
    check_value_str = str(check_value)

    # Return "selected" if the current location matches the check_value, otherwise return an empty string
    return "selected" if current_location == check_value_str else ""


@register.filter(name='selected_if_matches')
def selected_if_matches(url, expected_value):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    # Assuming expected_value comes in format 'field:value', e.g., 'bed:Single'
    field, value = expected_value.split(':')
    current_value = query_params.get(field, [None])[0]
    
    return "selected" if current_value == value else ""