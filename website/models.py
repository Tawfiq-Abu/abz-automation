from django.db import models

from utils.constants import TINY_STR_LEN, SHORT_STR_LEN, ICON_CHOICES

# Create your models here.

class Metric(models.Model):
    name = models.CharField(max_length=SHORT_STR_LEN)
    count = models.IntegerField()
    icon = models.CharField(max_length=SHORT_STR_LEN, choices=ICON_CHOICES, default="icofont-water-drop")

    def __str__(self):
        return self.name