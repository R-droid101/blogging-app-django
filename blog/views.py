from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog 1',
        'content': 'This is the content of blog 1',
        'date_posted': '2020-01-01'
    },
    {
        'author': 'John Doe 2',
        'title': 'Blog 2',
        'content': 'This is the content of blog 2',
        'date_posted': '2020-01-01'
    },
    {
        'author': 'John Doe 3',
        'title': 'Blog 3',
        'content': 'This is the content of blog 3',
        'date_posted': '2020-01-01'
    },
    {
        'author': 'John Doe 4',
        'title': 'Blog 4',
        'content': 'This is the content of blog 4',
        'date_posted': '2020-01-01'
    },
]

def home(req):
    context = {
        'posts': Post.objects.all()
    }
    return render(req, 'blog/home.html', context)

def about(req):
    return render(req, 'blog/about.html', {
        'title': 'About'
    })