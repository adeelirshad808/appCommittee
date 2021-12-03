from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        if(authenticate(username=username, password=password)):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    print(user.is_active)
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Account is deactivated')
            else:
                return render(request, 'app/authentication/login.html')
        else:
            return render(request, 'app/authentication/failed_login.html')

    else:
        print('running')
    return render(request, 'app/authentication/user_login.html')
