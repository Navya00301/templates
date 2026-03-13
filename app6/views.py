from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home-02.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def forgotpassword(request):
    return render(request,'forgotpassword.html')

def resetpassword(request):
    return render(request,'reset-password.html')

def shopingcart(request):
    return render(request,'shoping-cart.html')

def product(request):
    return render(request,'product.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def confirmation(request):
    return render(request,'confirmation.html')

def checkout(request):
    return render(request,'checkout.html')
