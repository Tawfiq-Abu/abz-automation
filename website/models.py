from django.db import models
from utils.constants import TINY_STR_LEN, SHORT_STR_LEN, LONG_STR_LEN, ICON_CHOICES


# Create your models here.



def icon_image_directory(instance, filename):
    return '/'.join(['images', 'team-member', str(instance.first_name), filename])

class TeamMember(models.Model):
    first_name = models.CharField(max_length=SHORT_STR_LEN)
    other_names = models.CharField(max_length=SHORT_STR_LEN, null=True, blank=True)
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
    icon = models.CharField(max_length=SHORT_STR_LEN, choices=ICON_CHOICES, default="icofont-water-drop")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=SHORT_STR_LEN)
    description = models.TextField()

    def __str__(self):
        return self.name

class ProductModel(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField(max_length=SHORT_STR_LEN)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product} - {self.name}"

class ProductModelFeature(models.Model):
    product_model = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    description = models.CharField(max_length=LONG_STR_LEN)

    def __str__(self):
        return self.description


class Service(models.Model):
    name = models.CharField(max_length=SHORT_STR_LEN)
    description = models.CharField(max_length=LONG_STR_LEN)
    icon = models.CharField(max_length=SHORT_STR_LEN, choices=ICON_CHOICES, default="icofont-water-drop")


    def __str__(self):
        return self.name




