from django.urls import path
from . import views

urlpatterns = [
   path('',views.index, name="index"),
   path('index.html',views.index, name="index"),
   path('contact.html', views.contact, name="contact"),
   path('blog-single.html', views.blog_single, name="blog-single"),
   path('blog.html', views.blog, name="blog"),
]
