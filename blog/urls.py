from django.urls import path
from .views import (
    BlogPostListView, 
    BlogPostDetailView, 
    BlogPostCreateView, 
    BlogPostUpdateView, 
    BlogPostDeleteView
)
from . import views

urlpatterns = [
    path('', BlogPostListView.as_view(), name="blog-home"),
    path('about/', views.about, name="blog-about"),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name="blog-detail"),
    path('blog/create/', BlogPostCreateView.as_view(), name="blog-create"),
    path('blog/update/<int:pk>', BlogPostUpdateView.as_view(), name="blog-update"),
    path('blog/delete/<int:pk>', BlogPostDeleteView.as_view(), name="blog-delete")
]