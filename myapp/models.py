from django.db import models

class SEO(models.Model):
    name = models.CharField(max_length=255, default='home')
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

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
    )
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE, related_name='blog')
    slug = models.SlugField(max_length=200, unique=True, null=True)
    image = models.ImageField(upload_to='blogs/')
    title = models.CharField(max_length=255, null=True )
    content = models.TextField()
    tags = models.ManyToManyField(BlogTag, related_name='blog', blank=True)  # Added blank=True for optional amenities
    published_date = models.DateField(null=True, blank=True)
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



class Hostel(models.Model):
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE, related_name='hostel')
    slug = models.SlugField(max_length=200, unique=True, null=True)
    city = models.OneToOneField(City, on_delete=models.CASCADE, related_name='hostel')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='hostels/', blank=True)
    google_map_location = models.TextField(max_length=2000, default="")
    amenities = models.ManyToManyField(Amenity, related_name='hostels', blank=True)  # Added blank=True for optional amenities
    
    bed = models.CharField(max_length=255 , default='Single/Double/Triple')
    bath = models.TextField(max_length=255 , default='Atachedt/Common')
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

    video = models.FileField(upload_to='hostel_videos/', blank=True, null=True)
    video_thumbnail = models.ImageField(upload_to='hostel_video_thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.name

class Images(models.Model):
    image = models.ImageField(upload_to="hostel_images/img")
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='images')  # Added related_name for reverse access

class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonials/')
    student_name = models.CharField(max_length=255)
    student_addr= models.CharField(max_length=255, null=True)
    review = models.TextField()
    
    def __str__(self):
        return self.student_name
