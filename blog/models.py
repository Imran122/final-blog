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


User = get_user_model()
# worked for views of a post

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='photos/%Y/%m/%d')
    
    def __str__(self):
        return self.user.username

class Categorey(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return self.title


class PostView(models.Model):
    client_ip = models.GenericIPAddressField()
    #view_count = models.IntegerField(default=0)
    #view_count = models.ForeignKey('Post', on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, blank=True, null=True)





    def __str__(self):
        return self.client_ip


        
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250,unique=True, null=True, blank=True)
    overview = models.TextField()
    content = RichTextUploadingField()
    
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d')
    categories = models.ManyToManyField(Categorey)
    featured = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post',kwargs={ 'slug': self.slug, 'id':self.id})

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

    
