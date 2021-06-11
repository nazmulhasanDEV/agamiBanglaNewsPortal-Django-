from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from user.models import User
from django.contrib.auth import login, logout, authenticate


def register_user(request):

    if request.method == 'POST':
        first_name      = request.POST.get('register-firstname')
        last_name       = request.POST.get('register-lastname')
        user_name       = request.POST.get('register-username')
        email           = request.POST.get('register-email')
        password        = request.POST.get('register-password')
        verify_password = request.POST.get('register-password-verify')

        if len(password) >= 6:
            if len(User.objects.filter(user_name=user_name)) == 0 and len(User.objects.filter(email=email)) == 0:
                if len(User.objects.all()) <= 0:
                    user = User.objects.create_user(email=email, user_name=user_name, password=password)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.is_active = True
                    user.is_admin = True
                    user.is_Staff = True
                    user.save()
                    messages.success(request, "Account has been created successfully!")
                    return redirect('registerUser')
                else:
                    user = User.objects.create_user(email=email, user_name=user_name, password=password)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.is_active = False
                    user.is_admin = False
                    user.is_Staff = False
                    user.save()
                    messages.success(request, "You are under review! The account will be activated soon!")
                    return redirect('registerUser')
            else:
                messages.warning(request, "Email or Username already exists!")
                return redirect('registerUser')
        else:
            messages.warning(request, "Password must be at least 6 characters long!")
            return redirect('registerUser')

    return render(request, 'backEnd/login-register.html')

def login_user(request):

    if request.method == 'POST':
        email           = request.POST.get('login-email')
        user_name       = request.POST.get('login-username')
        password        = request.POST.get('login-password')

        user = User.objects.filter(user_name=user_name).first()

        if user:
            verify_user = authenticate(request, email=email, password=password)
            if verify_user is not None:
                login(request, verify_user)
                return redirect('adminPanelIndex')
            else:
                messages.warning(request, "Wrong email or password!!")
                return redirect('registerUser')
        else:
            messages.warning(request, "User not found! Try again!!!")
            return redirect('registerUser')

    return render(request, 'backEnd/login-register.html')

def logout_user(request):
    logout(request)
    redirect('loginUser')