from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.



@cache_page(60 * 15)
def home(request):
    return render(request, 'index.html')

@cache_page(60 * 15)
def about(request):
    return render(request, 'about.html')

@cache_page(60 * 15)
def detail(request):
    return render(request, 'detail.html')

@cache_page(60 * 15)
def blog(request):
    return render(request, 'blog.html')

@cache_page(60 * 15)
def contact(request):
    return render(request, 'contact.html')

@cache_page(60 * 15)
def testimonial(request):
    return render(request, 'testimonial.html')

@cache_page(60 * 15)
def service(request):
    return render(request, 'service.html')

@cache_page(60 * 15)
def team(request):
    return render(request, 'team.html')
