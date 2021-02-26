from django.shortcuts import render
from blog.models import Contact


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def courses(request):
    return render(request, 'courses.html')


def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        desc = request.POST['desc']
        contact = Contact(first_name=first_name, last_name=last_name,
                          phone=phone, email=email, desc=desc)
        contact.save()
    return render(request, 'contact.html')
