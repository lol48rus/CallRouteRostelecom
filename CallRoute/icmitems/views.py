from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request, 'icmitems/icmitems.html')

def agent(request):
    return render(request, 'icmitems/agent.html')