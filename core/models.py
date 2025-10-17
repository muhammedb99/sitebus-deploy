from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "קטגוריה"
        verbose_name_plural = "קטגוריות"

    def __str__(self):
        return self.name
    
    def cover_photo(self):
        return self.photos.order_by('-created_at').first()

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='photos')
    image = CloudinaryField('image')  # נשמר בענן
    caption = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "תמונה"
        verbose_name_plural = "תמונות"

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "הודעת קשר"
        verbose_name_plural = "הודעות קשר"

    def __str__(self):
        return f"{self.full_name} - {self.phone}"
