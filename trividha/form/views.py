from django.shortcuts import render
from .models import events
# Create your views here.
def register(request):
    event_obj=events.objects.all
    return render(request,'form.html',{"events":event_obj})