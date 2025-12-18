from django.http import HttpResponse
from django.shortcuts import render

# def HomePage(request):
#     return HttpResponse("Hello Welcome to Home Page")

# def AboutPage(request):
#     return HttpResponse("Hello Welcome to About Page")

# def ServicePage(request):
#     return HttpResponse("Hello Welcome to Service Page")

# def BlogPage(request):
#     return HttpResponse("Hello Welcome to Blog Page")

# def PagesPage(request):
#     return HttpResponse("Hello Welcome to Pages Page")

# def ContactPage(request):
#     return HttpResponse("Hello Welcome to Contact Page")

def HomePage(request):
    return render(request,"index.html")

def AboutPage(request):
    return render(request,"about.html")

def BlogPage(request):
    return render(request,"blog.html")

def ServicePage(request):
    return render(request,"service.html")

def PagesPage(request):
    return render(request,"pages.html")

def ContactPage(request):
    return render(request,"contact.html")

def ourfeaturePage(request):
    return render(request,"ourfeature.html")

def ourcarsPage(request):
    return render(request,"ourcars.html")

def ourteamPage(request):
    return render(request,"ourteam.html")

def testimonialPage(request):
    return render(request,"testimonial.html")

def numpagePage(request):
    return render(request,"numpage.html")