from django.db import models

class SEO(models.Model):
    name = models.CharField(max_length=255, default='home')
    title = models.CharField(max_length=550)
    description = models.TextField()
    keywords = models.TextField(null=True)
    
    def __str__(self):
        return self.name

class City(models.Model):
    city = models.CharField(max_length=55)
    
    def __str__(self):
        return self.city


class BlogTag(models.Model):
    name = models.CharField(max_length=100)    
    def __str__(self):
        return self.name

class Blog(models.Model):
    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
        ('Seo', 'Seo'),
    )
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE, related_name='blog')
    slug = models.SlugField(max_length=200, unique=True, null=True)
    image = models.ImageField(upload_to='media/blogs/' )
    title = models.CharField(max_length=255, null=True )
    content = models.TextField(null=True)
    tags = models.ManyToManyField(BlogTag, related_name='blog', blank=True)  # Added blank=True for optional amenities
    published_date = models.DateField(null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=50, default='Seo')
    def __str__(self):
        return self.seo.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.id} on {self.blog.seo.title}"

class Amenity(models.Model):
    name = models.CharField(max_length=100)    
    def __str__(self):
        return self.name

class BedType(models.Model):
    OCCUPANCY = (
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Tripple', 'Tripple'),
        ('Four', 'Four'),
    )
    type = models.CharField(max_length=50, choices=OCCUPANCY, unique=True)

    def __str__(self):
        return self.type

class BathType(models.Model):
    BATH = (
        ('Attached', 'Attached'),
        ('Common', 'Common'),
    )
    type = models.CharField(max_length=50, choices=BATH, unique=True)

    def __str__(self):
        return self.type

class Hostel(models.Model):
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE, related_name='hostel')
    slug = models.SlugField(max_length=200, unique=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hostels')  # Change to ForeignKey
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/hostels/', blank=True)
    google_map_location = models.TextField(max_length=2000, default="")
    amenities = models.ManyToManyField(Amenity, related_name='hostels', blank=True)  # Added blank=True for optional amenities
    
    beds = models.ManyToManyField(BedType, blank=True)  # 'null=True' is not needed on ManyToMany fields
    bath = models.ManyToManyField(BathType, blank=True)  # 'null=True' is not needed on ManyToMany fields

    
    TYPE = (
        ('Boys', 'Boys'),
        ('Girls', 'Girls'),
    )
    hostelType = models.CharField(choices=TYPE, max_length=50, default="Boys")
    
    BOOL =(
            ('Yes', 'Yes'),
            ('No','No')
            
        )
    cafeteria = models.CharField(choices=BOOL, max_length=50, default="Yes")
    
    nearby= models.TextField(max_length=550 , default='Sharda University : 0.2km')
    details = models.TextField(max_length=2055, default="")

    video = models.FileField(upload_to='media/hostel_videos/', blank=True, null=True)
    video_thumbnail = models.ImageField(upload_to='media/hostel_video_thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.name

class Images(models.Model):
    image = models.ImageField(upload_to="media/hostel_images/img")
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='images')  # Added related_name for reverse access

class Testimonial(models.Model):
    image = models.ImageField(upload_to='media/testimonials/')
    student_name = models.CharField(max_length=255)
    student_addr= models.CharField(max_length=255, null=True)
    review = models.TextField()
    
    def __str__(self):
        return self.student_name
    
class SentEmail(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    recipient = models.EmailField()
    sent_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email to {self.recipient} on {self.sent_datetime}"
