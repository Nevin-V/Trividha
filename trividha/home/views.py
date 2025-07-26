from django.shortcuts import render
from .models import details

# Create your views here.

def index(request):
    det=details.objects.first()
    return render(request,'try.html',{"details":det})
def register(request):
    return render(request,'form.html')