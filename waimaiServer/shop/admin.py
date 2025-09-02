from django.contrib import admin
from .models import ShopCategory, Shop, Food

# Register your models here.

@admin.register(ShopCategory)
class ShopCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    list_per_page = 20


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'phone', 'address', 'is_open', 'created_at']
    list_filter = ['category', 'is_open', 'created_at']
    search_fields = ['name', 'phone', 'address']
    list_per_page = 20
    raw_id_fields = ['category']


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'shop', 'category', 'price', 'purchase_count', 'is_new', 'is_hot', 'created_at']
    list_filter = ['shop', 'category', 'is_new', 'is_hot', 'created_at']
    search_fields = ['name', 'description']
    list_per_page = 20
    raw_id_fields = ['shop']
