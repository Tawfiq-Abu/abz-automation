from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active"]
    list_filter = ["title"]
    search_fields= ["title"]


admin.site.register(Blog,BlogAdmin)