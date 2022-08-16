from django.contrib import admin



from .models import (TeamMember, Metric, Product, ProductModel, ProductModelFeature, Service,Basket,ServiceRequest,ProductOrder)


# Register your models here.

class ModelFeatureInline(admin.TabularInline):
    model = ProductModelFeature

class ProductModelAdmin(admin.ModelAdmin):
    inlines = [ModelFeatureInline]

admin.site.register(ProductModel, ProductModelAdmin) 
admin.site.register(ProductModelFeature) 
admin.site.register(TeamMember)
admin.site.register(Metric)
admin.site.register(Service)


class ProductFeatureInline(admin.TabularInline):
    model = ProductModel

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductFeatureInline]
admin.site.register(Product,ProductAdmin)
admin.site.register(Basket)
admin.site.register(ServiceRequest)
admin.site.register(ProductOrder)


