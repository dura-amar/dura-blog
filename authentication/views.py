from django.shortcuts import render

from authentication.forms import UserLoginForm, UserRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import logout,login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def view_user_register(request):
    if request.user.is_authenticated:
        redirect("view_allBlogs")
    form=UserRegistrationForm()
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'register.html',{'form':form})

def view_user_login(request):
    if request.user.is_authenticated:
        redirect("view_allBlogs")
    form=UserLoginForm()
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('view_allBlogs')
            else:
                return HttpResponse('this is wrong details')
    return render(request,'login.html',{'form':form})

@login_required
def view_user_logout(request):
    if not request.user.is_authenticated:
        redirect("view_allBlogs")
    logout(request)
    return redirect('view_allBlogs')

