from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class QuotesCategory(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(default="")
    img  = models.ImageField(default="defaultCategory.png",upload_to="uploads/category")
   
    def __str__(self):
        return self.name


class BlogsCategory(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(default="")
   
    def __str__(self):
        return self.name

class Quote(models.Model):
    quote = models.CharField(max_length=400)
    slug = models.SlugField(default="")
    backgroundImage = models.ImageField(default="defaultBG.png",upload_to="static/images")
    keywords = models.CharField(max_length=400,default="")
    metaDesc = models.CharField(max_length=400,default="")
    category = models.ForeignKey(QuotesCategory,on_delete=models.PROTECT,related_name="quotescategory",null=True,blank=True)
    author = models.CharField(max_length=100,null=True,blank=True,default="")
    postStatus = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.quote


class Blog(models.Model):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(default="")
    featuredImage = models.ImageField(default="defaultBG.png",upload_to="static/images")
    keywords = models.CharField(max_length=400,default="")
    metaDesc = models.CharField(max_length=400,default="")
    mainCategory = models.ForeignKey(BlogsCategory,on_delete=models.PROTECT,related_name="category",null=True,blank=True)
    tags = models.ManyToManyField(BlogsCategory)
    body  =     HTMLField(blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.PROTECT,related_name="author")
    createdAt = models.DateField(null=True)
    postStatus = models.BooleanField(default=False)
    claps = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Contact(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField(null=True)
    message=models.TextField()

class SubscriberEmail(models.Model):

    email = models.EmailField()
    name  = models.CharField(max_length=100)
    subscriptionDate = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.email
