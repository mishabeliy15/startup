from django.contrib import admin
from .models import SubCategory, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('display', 'name')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'display', 'name')
