
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True) # to store the last modified
    content=RichTextField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)# when created first
    status = models.IntegerField(choices=STATUS, default=0) # if the post is published or not
    likes=models.ManyToManyField(User,related_name='blog_post')
    def total_likes(self):
        return self.likes.count()
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    class Meta:
        ordering = ['-created_on'] # in descending order of created
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comment',on_delete=models.CASCADE)
    name=models.TextField(null=False)
    body=RichTextField(null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s-%s' % (self.post.title,self.name.username)

    def get_absolute_url(self):
        return reverse('add_post')



