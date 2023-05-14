from django.db import models
from django.utils.text import slugify
from django.conf import settings
from ckeditor.fields import RichTextField
    
class Region(models.Model):
    choices = (
        ("Africa", "AF",),
        ("Antarctica", "AN",),
        ("Asia", "AS",),
        ("Europe", "EU",),
        ("North america", "NA",),
        ("Oceania", "OC",),
        ("South america", "SA",),
    )

    name = models.CharField(max_length=20, null=True, blank=True, choices=choices)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
    

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextField()
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)
    country = models.CharField(max_length=150 ,null=True, blank=True)
    image = models.ImageField(upload_to="blogs")
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)