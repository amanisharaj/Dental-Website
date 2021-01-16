from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',context={})

def about(request):
    return render(request,'about.html',context={})

def service(request):
    return render(request,'service.html',context={})

def pricing(request):
    return render(request,'pricing.html',context={})

def blog(request):
    return render(request,'blog.html',context={})

def blogDetails(request):
    return render(request,'blog-details.html',context={})

def contact(request):
    return render(request,'contact.html',context={})

def error_404(request,exception):
    return render(request,'contact.html',context={})
