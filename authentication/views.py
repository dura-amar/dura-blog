from django.shortcuts import render

from authentication.forms import UserLoginForm, UserRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import logout,login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


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

# For password reset email
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request, "password_reset.html", context={"password_reset_form":password_reset_form})


