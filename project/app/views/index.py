from django.shortcuts import render,redirect
from app.models import *

def index(request):
    # print(request.user.firstname)
    
    return render(request,'app/index.html')