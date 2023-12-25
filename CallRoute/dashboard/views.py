from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'dashboard/dashboard.html')

def test(request):
    return render(request, 'dashboard/charttest.html')