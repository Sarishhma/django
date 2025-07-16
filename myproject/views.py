from django.http import HttpResponse
from django.shortcuts import render
def home (request):
    return render (request,"website/index.html")
def about(request):
    return render(request,"this is about page")
def contact(request):
    return render(request,"this is contact page")