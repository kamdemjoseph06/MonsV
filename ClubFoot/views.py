from django.shortcuts import render

# Create your views here.

def inscription(request):
    return render(request,'../templates/Inscription.html')

def connexion(request):
    return render(request,'../templates/Connection.html')