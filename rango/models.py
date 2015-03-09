from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    #slug field
    slug = models.SlugField(unique=True)
    
    #To use slug, override the save() method
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args,**kwargs)
    
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        """
        Provides a unicode representation of a model instance
        """
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.title
    
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # The 'upload_to' attribute is conjoined with the project's MEDIA_ROOT setting 
    # to provide a path with which uploaded profile images will be stored.
    # Result in all profile images being stored in the directory 
    # <workspace>/tango_with_django_project/media/profile_images/
    # To use ImageField, remember to install the Python Imaging Library (PIL) (pip install pillow)!

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username