from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import ckeditor
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# slug
from django.utils.text import slugify
from random import random
from django.db.models.signals import pre_save
from blog.models import Author
# Create your models here.

        
class GadgetCategorey(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return self.title

class GadgetPost(models.Model):
  
    gadgetcategories = models.ManyToManyField(GadgetCategorey)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250,unique=True, null=True, blank=True)
    overview = models.TextField()
    content = RichTextUploadingField()
    
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d')
    
    featured = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gadgetdetails', kwargs={ 'slug': self.slug, 'id':self.id})



    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)