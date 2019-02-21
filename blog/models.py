from django import forms
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Blog(models.Model):
    blog_title = models.CharField(max_length=200, unique=True)
    blog_content = models.TextField(blank=False)
    blog_author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    comment_content = models.TextField(verbose_name='comment')
    comment_author = models.CharField(default='Anonymous', max_length=100)
    comment_post_date = models.DateTimeField(default=timezone.now)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment_content