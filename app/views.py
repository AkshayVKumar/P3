from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def page1(request):
    return HttpResponse("<center><h1>Hello world</h1></center>")

def page2(request):
    return render(request,'sample.html')