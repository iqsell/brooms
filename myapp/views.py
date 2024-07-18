from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def nov(request):
    return render(request, 'nov.html')

def opt(request):
    return render(request, 'opt.html')

def venik(request):
    return render(request, 'venik.html')
