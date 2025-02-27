from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.id


class AboutUs(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    image = models.ImageField(upload_to='about_us/')

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=225)
    img = models.ImageField(upload_to='blog_images/', height_field=None, width_field=None, max_length=None)  # Stores images in media/blog_images/
    content =RichTextField()
    author = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title


# Contact Model
class ContactUs(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    phone = models.CharField(max_length=225, blank=True, null=True)  # Phone is optional
    message = models.TextField()

    def __str__(self):
        return self.name
