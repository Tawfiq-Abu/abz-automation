from django.contrib import admin
from .models import TeamMember

from .models import Metric,ProductFeature,Product,Service,Basket

# Register your models here.
# class TeamMemberAdmin(admin.ModelAdmin):
#     list_display= ['firstname','othername', 'lastname','role','image','linked_in','email']


admin.site.register(TeamMember)
admin.site.register(Metric)
# admin.site.register(ProductFeature)
admin.site.register(Service)

class ProductFeatureInline(admin.TabularInline):
    model = ProductFeature

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductFeatureInline]
admin.site.register(Product,ProductAdmin)
admin.site.register(Basket)

