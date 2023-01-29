from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def Contactus(request):
    return render(request,'Contactus.html')

def about(request):
    return render(request,'about.html')

def gallery(request):
    return render(request,'Gallery.html')

def retrieval(request):
    return render('admin.html')