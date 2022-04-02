from django.contrib.admin.sites import site
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    CHOICES = (
        ('draft', 'Próbny'),
        ('published', 'Opublikowany'))
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=13, choices=CHOICES, default='draft')
    image = models.ImageField(upload_to='fetured_image/%Y/%m/%d/',blank=True)

    tags=TaggableManager()
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'), self.slug])
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments', null=False)
    name=models.CharField(max_length=70)
    email=models.EmailField(null=False)
    body=models.TextField(max_length=3500,error_messages={'unique':"This email has already been registered."})
    created=models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering =('created',)
        
    def __str__(self):
        return f'Komentarz autorstwa {self.name} do posta {self.post}'
