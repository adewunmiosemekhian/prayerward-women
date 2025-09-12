# blog/admin.py
from django.contrib import admin
from .models import Post, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']
    list_editable = ['color']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    list_filter = ['created_at', 'categories']
    filter_horizontal = ['categories']
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at', 'approved']
    list_filter = ['approved', 'created_at']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)