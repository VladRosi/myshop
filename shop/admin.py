from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class Category(admin.ModelAdmin):
  list_display = ['name', 'slug']
  prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class Category(admin.ModelAdmin):
  list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
  list_filter = ['available', 'created', 'updated']
  list_editable = ['price', 'available']
  prepopulated_fields = {'slug': ('name', )}