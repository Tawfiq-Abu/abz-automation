import email
from django.db import models
from utils.constants import TINY_STR_LEN,SHORT_STR_LEN,LONG_STR_LEN
# Create your models here.



def icon_image_directory(instance, filename):
    return '/'.join(['images', 'team-member', str(instance.first_name), filename])

class TeamMember(models.Model):
    first_name = models.CharField(max_length=SHORT_STR_LEN)
    other_name = models.CharField(max_length=SHORT_STR_LEN,null=True)
    last_name = models.CharField(max_length=SHORT_STR_LEN)
    role = models.CharField(max_length=SHORT_STR_LEN)
    image = models.ImageField(upload_to=icon_image_directory)
    linked_in = models.URLField()
    email = models.EmailField()


    def __str__(self):
        return self.first_name