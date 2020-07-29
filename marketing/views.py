from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Contact
from django.http import HttpResponse
from django.http import HttpResponseRedirect, request
from .forms import ContactForm
from django.contrib.auth import authenticate

# Create your views here.


def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            #cementry is a variable
            cemetery=form.save(commit=False)
            cemetery.name=request.POST.get('name')
            cemetery.email=request.POST.get('email')
            cemetery.phone=request.POST.get('phone')
            cemetery.address=request.POST.get('address')
            cemetery.msg=request.POST.get('msg')
            cemetery.save() 
            messages.success(request, 'You are messages submitted')
            return render(request, 'accounts/contact.html')  
        else:
            # If the request was not a POST, display the form to enter details.
            #messages.error(request, 'You are messages can not submitted.')
            return []

    else:
        form=ContactForm
    return render(request,'accounts/contact.html',{'form':form})









def about(request):
    return render(request, 'accounts/about.html')
def privacy(request):
    return render(request, 'accounts/privacy.html')