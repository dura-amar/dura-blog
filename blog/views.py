from django.shortcuts import redirect, render
from blog.forms import BlogPostForm, CategoryForm

from blog.models import BlogPost, Category

# Create your views here.

# View all the blogs
def view_allBlogs(request):
    blogs=BlogPost.objects.all()
    context={'page_title':'All Blogs','blogs':blogs}
    return render(request,'blogs.html',context)

# View a single blog by id
def view_aBlog(request,bId):
    blog=BlogPost.objects.get(id=bId)
    context={'page_title':blog.title,'blog':blog}
    return render(request,'blog.html',context)

# Create a new blog
def view_add_aBlog(request):
    form=BlogPostForm()
    if(request.method=='POST'):
        form=BlogPostForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('view_allBlogs')
    return render(request,'add_blog.html',{'form':form})


# View all the categories
def view_allCategory(request):
    categories=Category.objects.all()
    context={'page_title':'All Category','category':categories}
    return render(request,'categorys.html',context)

# View a single blog by id
def view_aCategory(request,cId):
    ctg=Category.objects.get(id=cId)
    blogs=BlogPost.objects.filter(category=ctg)
    context={'page_title':ctg.name,'blogs':blogs}
    return render(request,'blogs.html',context)

# Create a new blog
def view_add_aCategory(request):
    form=CategoryForm()
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_allCategory')
    return render(request,'add_category.html',{'form':form})

