from django.db import models

from django.utils import timezone

from django.contrib.auth import get_user_model

from django.contrib.auth.models import User

from django.urls import reverse

from taggit.managers import TaggableManager 

import readtime 

class Author(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)

    profile = models.ImageField()

    def __str__(self):

        return self.user.username

class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'), ('published', 'Published')
    )

    title = models.CharField(max_length=200)

    slug = models.SlugField(max_length=200, unique_for_date= 'publish')

    author = models.ForeignKey(

        Author, 

        on_delete= models.CASCADE,

        related_name= 'blog_posts'
    )

    body = models.TextField()

    tags = TaggableManager()

    thumbnail = models.ImageField(upload_to = 'uploads/')

    # categories = models.ManyToManyField(Categories)

    publish = models.DateTimeField(default=timezone.now)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    featured = models.BooleanField()

    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default = 'draft')

    class Meta:

        ordering = ('-publish',)

    def get_readtime(self):

        result = readtime.of_text(self.body)

        return result.text

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse(
            'blog:post_detail',
            args = [
                self.publish.year, 
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )