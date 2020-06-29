from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
  return render_to_response('app/index.html')
    #return HttpResponse("./frontend/index.html")
def signup(request): 
    return HttpResponse("SignUP page")
def login(request): 
    return HttpResponse("Login PAGE ")
def dashboard(request):
    return HttpResponse("Dashboard of the user")
# Create your views here.
