from django.contrib import admin
from .models import Food, Comment, Type


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    list_display_links = ['pk', 'title']


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'type', 'ingredient', 'price', 'created_at', 'updated_at']
    list_display_links = ['pk', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'food', 'text', 'created_at']
    list_display_links = ['pk', 'author']
