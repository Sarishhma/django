from .models import item
from django.shortcuts import render
def new(request):
    images = item.objects.all()
    return render (request,'app/new.html',{'images':images}
                   )

  