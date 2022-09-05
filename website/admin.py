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

class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 0
    readonly_fields = ('product_model', 'quantity', 'total_amount')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class ServiceRequestInline(admin.TabularInline):
    model = ServiceRequest
    extra = 0
    readonly_fields = ('service', )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class BasketAdmin(admin.ModelAdmin):
    inlines = [
        ProductOrderInline,
        ServiceRequestInline
    ]
    readonly_fields = ('customer_name', 'customer_email', 'customer_phone_number', 'date_ordered')

admin.site.register(Product,ProductAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(ServiceRequest)
admin.site.register(ProductOrder)


