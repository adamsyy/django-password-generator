from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    r=2,
    return render(request,'generator/home.html');