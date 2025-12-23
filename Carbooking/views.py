from django.http import HttpResponse
from django.shortcuts import render,redirect
from car_admin.models import Service,Cat,Blog,Review,Centalprocess,Centalfeatures,Numbering,BookingForm,ContactForm

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
    if request.method == "POST":
        BookingForm.objects.create(
            car_type= request.POST.get('car_type'),
            pickup_location= request.POST.get('pickup_location'),
            drop_location= request.POST.get('drop_location'),
            pickup_date= request.POST.get('pickup_date'),
            pickup_time= request.POST.get('pickup_time'),
            drop_date= request.POST.get('drop_date'),
            drop_time= request.POST.get('drop_time'),
        )
        return redirect('success')

    serviceData=Service.objects.all()
    CatData=Cat.objects.all()
    BlogData=Blog.objects.all()
    ReviewData=Review.objects.all()
    CentalprocessData=Centalprocess.objects.all()
    CentalfeaturesData=Centalfeatures.objects.all()
    NumberingData=Numbering.objects.all()
    data={
        'service_show':serviceData,
        'cat_show':CatData,
        'blog_show':BlogData,
        'review_show':ReviewData,
        'Centalprocess_show':CentalprocessData,
        'Centalfeatures_show':CentalfeaturesData,
        'Numbering_show':NumberingData,
    }
    return render(request,"index.html",data)

def AboutPage(request):
    NumberingData=Numbering.objects.all()
    CentalprocessData=Centalprocess.objects.all()
    data={
        'Numbering_show':NumberingData,
        'Centalprocess_show':CentalprocessData,
    }
    
    return render(request,"about.html",data)

def BlogPage(request):
    BlogData=Blog.objects.all()
    NumberingData=Numbering.objects.all()
    data={
        'blog_show':BlogData,
        'Numbering_show':NumberingData,
    }
    return render(request,"blog.html",data)

def ServicePage(request):
    serviceData=Service.objects.all()
    NumberingData=Numbering.objects.all()
    ReviewData=Review.objects.all()
    data={
        'service_show':serviceData,
        'Numbering_show':NumberingData,
        'review_show':ReviewData,
    }
    return render(request,"service.html",data)

def PagesPage(request):
    return render(request,"pages.html")



def ContactPage(request):
    if request.method == "POST":
        ContactForm.objects.create(
            your_name= request.POST.get('your_name'),
            email= request.POST.get('email'),
            your_phone= request.POST.get('your_phone'),
            your_projects= request.POST.get('your_projects'),
            subjects= request.POST.get('subjects'),
            msg= request.POST.get('msg')
        )
        return redirect('contact')
    
    return render(request,"contact.html")



def ourfeaturePage(request):
    NumberingData=Numbering.objects.all()
    data={
        'Numbering_show':NumberingData,
    }
    return render(request,"ourfeature.html",data)

def ourcarsPage(request):
    CatData=Cat.objects.all()
    CentalprocessData=Centalprocess.objects.all()
    data={
        'cat_show':CatData,
        'Centalprocess_show':CentalprocessData,
    }
    return render(request,"ourcars.html",data)

def ourteamPage(request):
    return render(request,"ourteam.html")

def testimonialPage(request):
    ReviewData=Review.objects.all()
    data={
        'review_show':ReviewData,
}
    return render(request,"testimonial.html",data)

def numpagePage(request):
    return render(request,"numpage.html")

def success(request):
    return render(request,"success.html")