from django.contrib import admin
from django.db.models.base import Model
from .models import Post, Comment

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date", "id")
    inlines = [
        CommentInline
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
