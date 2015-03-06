from django.db import models
from django.template.defaultfilters import slugify

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