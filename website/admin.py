from django.contrib import admin


from .models import Metric,ProductFeature,Product,Service,Basket,ServiceRequest

from .models import (TeamMember, Metric, Product, ProductModel, ProductModelFeature, Service)


# Register your models here.

class ModelFeatureInline(admin.TabularInline):
    model = ProductModelFeature

class ProductModelAdmin(admin.ModelAdmin):
    inlines = [ModelFeatureInline]

admin.site.register(Product)
admin.site.register(ProductModel, ProductModelAdmin) 
admin.site.register(ProductModelFeature) 
admin.site.register(TeamMember)
admin.site.register(Metric)
admin.site.register(Service)


class ProductFeatureInline(admin.TabularInline):
    model = ProductFeature

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductFeatureInline]
admin.site.register(Product,ProductAdmin)
admin.site.register(Basket)
# admin.site.register(ServiceRequest)

