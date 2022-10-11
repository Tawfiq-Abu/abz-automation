from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "is_active"]
    list_filter = ["title", "author"]
    search_fields= ["title", "author"]


admin.site.register(Blog,BlogAdmin)