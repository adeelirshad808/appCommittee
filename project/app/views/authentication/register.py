from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.forms import *


def register(request):
    context = {}
    registered = False
    if request.method == 'POST':
        user_form = UserRegisterationForm(data=request.POST)
        if user_form.is_valid(): 
            user = user_form.save()
            registered = True
            print('user registered')
            return redirect('user_login')
    else:
        user_form = UserRegisterationForm()
        context = {'UserRegisterationForm':UserRegisterationForm}

    return render(request,'app/authentication/register.html', context)  

