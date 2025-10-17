from django.contrib import admin
from .models import Category, Photo, ContactMessage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("category", "caption", "created_at")
    list_filter = ("category",)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "email", "created_at")
    search_fields = ("full_name", "phone", "email")
