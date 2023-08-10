from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from .models import  Contact, Menu, BookTable, Special
# Create your views here.

def index(request):
    menu=Menu.objects.all()
    specials=Special.objects.all()
    return render(request, "index.html",{"menu":menu,"specials":specials})

def contact(request):
    if request.method== "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST.get('message')
        contact = Contact.objects.create(name=name,subject=subject,email=email,message=msg)
        contact.save()
        messages.info(request, "Thank You for Contacting Us, We'll get back to you shortly")
        return redirect("/")
    return redirect("/")


def book_table(request):
    if request.method== "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        date = request.POST['date']
        sits=request.POST.get('sits')
        msg = request.POST.get('message')
        contact = BookTable.objects.create(name=name,phone_no=phone_no,email=email,date=date,message=msg,sits=sits)
        contact.save()
        messages.info(request, "Thank You for Booking!")
        return redirect("/")
    return redirect("/")

