from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(req):
    context = {
        'posts': Post.objects.all()
    }
    return render(req, 'blog/home.html', context)

def about(req):
    return render(req, 'blog/about.html', {
        'title': 'About'
    })

class BlogPostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class BlogPostDetailView(DetailView):
    model = Post

class BlogPostCreateView(LoginRequiredMixin, CreateView): 
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self) -> bool | None:
        return super().test_func() and self.get_object().author == self.request.user
    
class BlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self) -> bool | None:
        return super().test_func() and self.get_object().author == self.request.user