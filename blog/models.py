from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title=models.CharField(max_length=50)
    content=RichTextField(blank=True, null=True)
    date_posted=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    thumbnail=models.ImageField(upload_to='blog/',blank=True,null=True)
    slug_title=models.SlugField(null=False,blank=False,editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug_title = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)