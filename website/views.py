from django.shortcuts import render
from . import views
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def contact(request):
    return render(request, 'contact.html', {})  

def blog_single(request):
    return render(request, 'blog-single.html', {}) 

def blog(request):
    return render(request, 'blog.html', {})           