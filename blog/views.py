from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Blog, Comment
from .forms import BlogForm, CommentForm

def index(request):
    template = 'blog/index.html'
    blogs = Blog.objects.order_by('-blog_post_date')
    comments = Comment.objects.all()

    context = {
        'blogs': blogs,
        'comments': comments
    }
    return render(request, template, context)

def add_blog(request):
    template = 'blog/add_blog.html'

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('blog:index'))
    else:
        context ={
            'blog_form': BlogForm,
        }
    return render(request, template, context)


def blog_detail(request, id):
    template = 'blog/blog_detail.html'
    blog = Blog.objects.get(id=id)
    context = {
        'blog':blog
    }
    return render(request, template, context)
    
def add_comment(request, id):
    template = 'blog/add_comment.html'
    blog = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse_lazy('blog:index'))
    else:
        form = CommentForm()
        context = {
            'comment_form': form,
            'blog': blog
            }
    return render(request, template, context)