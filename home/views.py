from django.shortcuts import render,redirect

# Create your views here.
def view_about_me(request):
    return render(request, 'about.html')

def view_fb(request):
    return redirect("https://www.facebook.com/du.ra.ad0/")
def view_ig(request):
    return redirect("https://www.instagram.com/du.ra.ad/")
def view_ln(request):
    return redirect("https://www.linkedin.com/in/amar-dura-404360171/")
def view_tw(request):
    return redirect("https://twitter.com/du_ra_ad")
def view_gh(request):
    return redirect("https://github.com/dura-amar")