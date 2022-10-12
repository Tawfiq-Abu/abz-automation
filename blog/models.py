from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import readtime
from uuslug import uuslug


def blogs_image_directory(instance, filename):
    return '/'.join(['images', 'team-member', str(instance.title), filename])


# Create your models here.
class Blog(models.Model):
    # author = models.ForeignKey(User, on_delete=models.SET(get_default_user))
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=blogs_image_directory)
    description = RichTextUploadingField()
    # topics = models.ManyToManyField(Topic, related_name="blogs")
    slug = models.SlugField(max_length=256,unique=True,editable=False)
    is_active = models.BooleanField(default=False)
    views = models.BigIntegerField(default=0)
    
    def save(self,*args,**kwargs):
        self.slug = uuslug(self.title, instance=self)
        super().save(*args,**kwargs)
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title
    
    def increase_views(self):
        self.views += 1
        self.save()
    
    def get_duration(self):
        return str(readtime.of_html(self.description)).capitalize()
