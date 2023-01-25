
import uuid
from django.db import models
from utils.constants import TINY_STR_LEN, SHORT_STR_LEN, LONG_STR_LEN

from location_field.models.plain import PlainLocationField

from django.db import models
from utils.constants import TINY_STR_LEN, SHORT_STR_LEN, LONG_STR_LEN, ICON_CHOICES


# Create your models here.


def icon_image_directory(instance, filename):
    return '/'.join(['images', 'team-member', str(instance.first_name), filename])


def product_image_directory(instance, filename):
    return '/'.join(['images', 'team-member', str(instance.name), filename])


class TeamMember(models.Model):
    first_name = models.CharField(max_length=SHORT_STR_LEN)
    other_names = models.CharField(
        max_length=SHORT_STR_LEN, null=True, blank=True)
    last_name = models.CharField(max_length=SHORT_STR_LEN)
    role = models.CharField(max_length=SHORT_STR_LEN)
    image = models.ImageField(upload_to=icon_image_directory)
    linked_in = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Metric(models.Model):
    name = models.CharField(max_length=SHORT_STR_LEN)
    count = models.IntegerField()
    icon = models.CharField(max_length=SHORT_STR_LEN,
                            choices=ICON_CHOICES, default="icofont-water-drop")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=SHORT_STR_LEN)
    description = models.TextField()
    image = models.ImageField(upload_to=product_image_directory)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_models")
    name = models.CharField(max_length=SHORT_STR_LEN)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True,)

    def __str__(self):
        return f"{self.product} - {self.name}"


class ProductModelFeature(models.Model):
    product_model = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE, related_name="product_model_features")
    description = models.CharField(max_length=LONG_STR_LEN)

    def __str__(self):
        return self.description


class Service(models.Model):
    name = models.CharField(max_length=SHORT_STR_LEN)
    description = models.CharField(max_length=LONG_STR_LEN, null=True)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    icon = models.CharField(max_length=SHORT_STR_LEN,
                            choices=ICON_CHOICES, default="icofont-water-drop")

    def __str__(self):
        return self.name


class Basket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    customer_name = models.CharField(max_length=SHORT_STR_LEN)
    customer_email = models.EmailField()
    # https://django-location-field.readthedocs.io/en/latest/tutorials.html#using-django-location-field-in-the-django-admin
    #! location = PlainLocationField(based_fields=['city'], zoom=7)
    customer_phone_number = models.CharField(max_length=SHORT_STR_LEN)
    date_ordered = models.DateTimeField(auto_now_add=True)
    extra_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ServiceRequest(models.Model):
    # total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    basket = models.ForeignKey(
        Basket, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.service.name


class ProductOrder(models.Model):
    # product = models.ForeignKey(Product,on_delete=models.CASCADE)
    # unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_model = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    basket = models.ForeignKey(
        Basket, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.product_model.name

    def save(self, *args, **kwargs):
        self.total_amount = self.product_model.price * self.quantity
        return super(ProductOrder, self).save(*args, **kwargs)
