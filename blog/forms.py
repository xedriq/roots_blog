from django import forms
from django.contrib.auth.models import User

from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    
    # author = User.objects.all()
    # blog_author = forms.CharField(author)

    class Meta:
        model = Blog
        fields = ('blog_title',
            'blog_content',
            'blog_author',
            )
    

class CommentForm(forms.ModelForm):
    comment_content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':4,'placeholder': 'Write your comment here...'}))

    class Meta:
        model = Comment
        fields = [
            'comment_content',
        ]
    
       